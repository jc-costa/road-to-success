-- D04 — Diagnóstico de SQL/PostgreSQL (60 min). Dados 100% fictícios e determinísticos (200 mil casos; carga leva ~10-30 s).
-- Como carregar:  psql -d <seu_banco> -f diagnostico/d04-schema.sql
-- Tudo fica no schema d04 (pode rodar de novo: ele é recriado).

DROP SCHEMA IF EXISTS d04 CASCADE;
CREATE SCHEMA d04;
SET search_path TO d04;

CREATE TABLE cases (
    id          bigserial PRIMARY KEY,
    patient_ref text        NOT NULL,   -- pseudônimo; nunca dado real
    reason      text        NOT NULL,   -- categoria do motivo do afastamento
    status      text        NOT NULL CHECK (status IN ('opened', 'paid', 'scheduled', 'documented', 'closed', 'cancelled')),
    opened_at   timestamptz NOT NULL
);

CREATE TABLE case_events (
    id       bigserial PRIMARY KEY,
    case_id  bigint      NOT NULL REFERENCES cases (id),
    type     text        NOT NULL,      -- opened, paid, scheduled, documented, closed, cancelled
    at       timestamptz NOT NULL
);

CREATE TABLE payments (
    id           bigserial PRIMARY KEY,
    case_id      bigint      NOT NULL REFERENCES cases (id),
    provider_ref text        NOT NULL,  -- id do pagamento no provedor (fictício)
    amount_cents int         NOT NULL,
    created_at   timestamptz NOT NULL
);

CREATE TABLE slots (
    id        bigserial PRIMARY KEY,
    clinician text        NOT NULL,
    starts_at timestamptz NOT NULL,
    case_id   bigint REFERENCES cases (id)   -- NULL = horário livre
);

-- ---------------------------------------------------------------- dados
SELECT setseed(0.42);

INSERT INTO cases (patient_ref, reason, status, opened_at)
SELECT 'P' || lpad(g::text, 5, '0'),
       (ARRAY ['back_pain', 'surgery_recovery', 'mental_health', 'pregnancy', 'injury', 'chronic_condition'])[1 + floor(random() * 6)::int],
       'opened',
       timestamptz '2026-01-01 00:00+00' + random() * interval '180 days'
FROM generate_series(1, 200000) AS g;

CREATE TEMP TABLE draw AS
SELECT id, opened_at, random() AS r1, random() AS r2, random() AS r3, random() AS r4, random() AS r5, random() AS r6
FROM cases;

INSERT INTO case_events (case_id, type, at)
SELECT id, 'opened', opened_at FROM draw;

INSERT INTO case_events (case_id, type, at)
SELECT id, 'paid', opened_at + r6 * interval '72 hours' FROM draw WHERE r1 < 0.80;

INSERT INTO case_events (case_id, type, at)
SELECT id, 'scheduled', opened_at + interval '72 hours' + r6 * interval '5 days' FROM draw WHERE r1 < 0.80 AND r2 < 0.85;

INSERT INTO case_events (case_id, type, at)
SELECT id, 'documented', opened_at + interval '9 days' + r3 * interval '4 days' FROM draw WHERE r1 < 0.80 AND r2 < 0.85 AND r3 < 0.90;

INSERT INTO case_events (case_id, type, at)
SELECT id, 'closed', opened_at + interval '14 days' + r4 * interval '3 days' FROM draw WHERE r1 < 0.80 AND r2 < 0.85 AND r3 < 0.90 AND r4 < 0.95;

INSERT INTO case_events (case_id, type, at)
SELECT id, 'cancelled', opened_at + interval '4 days' FROM draw WHERE r1 >= 0.95;

UPDATE cases c
SET status = last.type
FROM (SELECT DISTINCT ON (case_id) case_id, type FROM case_events ORDER BY case_id, at DESC) AS last
WHERE last.case_id = c.id;

INSERT INTO payments (case_id, provider_ref, amount_cents, created_at)
SELECT id, 'pi_' || left(md5(id::text), 16), CASE WHEN r5 < 0.30 THEN 14900 ELSE 9900 END, opened_at + r6 * interval '72 hours'
FROM draw WHERE r1 < 0.80;

-- cobranças duplicadas plantadas (mesmo caso, mesmo valor, ~40 s depois)
INSERT INTO payments (case_id, provider_ref, amount_cents, created_at)
SELECT id, 'pi_' || left(md5(id::text || 'dup'), 16), CASE WHEN r5 < 0.30 THEN 14900 ELSE 9900 END,
       opened_at + r6 * interval '72 hours' + interval '40 seconds'
FROM draw WHERE r1 < 0.80 AND r5 > 0.98;

INSERT INTO slots (clinician, starts_at)
SELECT 'clinician_' || (1 + g % 10), timestamptz '2026-07-01 09:00+00' + (g / 10) * interval '1 hour'
FROM generate_series(0, 299) AS g;

ANALYZE;

-- ---------------------------------------------------------------- tarefas
-- T1. Quantos casos há em cada status? Ordene do maior para o menor.
--
-- T2. Painel de Ops: liste os casos com evento 'paid' a partir de 2026-06-24 00:00 UTC que
--     ainda NÃO têm evento 'scheduled' (anti-join), do pagamento mais antigo para o mais novo.
--     Quantos são?
--
-- T3. Para cada mês de abertura, tempo médio e p90 entre 'opened' e 'paid'.
--     Use uma window function (ex.: LAG sobre os eventos de cada caso).
--
-- T4. Encontre cobranças duplicadas: mesmo caso, mesmo valor, 2+ pagamentos com menos de
--     5 minutos de diferença. Retorne case_id, quantidade e total cobrado a mais.
--
-- T5. Top 3 motivos (reason) por mês de abertura, por número de casos (CTE + RANK).
--     Explique como você trata empates.
--
-- T6. Crie o(s) índice(s) que aceleram a T2. Mostre EXPLAIN (ANALYZE, BUFFERS) antes e depois e
--     explique, em 2-3 frases, por que o plano mudou. Bônus de raciocínio: por que um índice
--     NÃO ajudaria se a T2 listasse todos os casos pagos sem consulta (sem filtro de data)?
--
-- BÔNUS. Escreva a transação que reserva o primeiro horário livre de 'clinician_3' para o
--     caso 42 sem dupla reserva quando duas sessões rodam ao mesmo tempo (teste com 2 psql).
--     Garanta também que um caso não ocupe dois horários.
