"""Handler do webhook 'payment.succeeded' (versão em produção durante o incidente).

Quando o pagamento da avaliação é confirmado, o handler:
  1. verifica a assinatura;
  2. cria a cobrança da assinatura de acompanhamento no provedor;
  3. registra a cobrança e marca o caso como pago;
  4. avisa o time de Ops (integração lenta: às vezes passa de 10 s).
O provedor considera a entrega falha se não receber 2xx em 10 s e reenvia o MESMO evento.
Só usa a biblioteca padrão (sqlite3) para rodar em qualquer máquina.
"""
import hashlib
import hmac
import json
import time

SECRET = b"whsec_exercicio_d10_fake"
FOLLOWUP_PRICE_CENTS = 4900


def init_db(conn):
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS cases (id TEXT PRIMARY KEY, customer_ref TEXT NOT NULL, status TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS charges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id TEXT NOT NULL,
            provider_charge_id TEXT NOT NULL,
            amount_cents INTEGER NOT NULL,
            provider_event_id TEXT NOT NULL
        );
        """
    )


def sign(payload: bytes, ts: int) -> str:
    mac = hmac.new(SECRET, f"{ts}.".encode() + payload, hashlib.sha256).hexdigest()
    return f"t={ts},v1={mac}"


def verify(payload: bytes, signature: str, tolerance_s: int = 300) -> bool:
    try:
        parts = dict(p.split("=", 1) for p in signature.split(","))
        ts = int(parts["t"])
    except (ValueError, KeyError):
        return False
    if abs(time.time() - ts) > tolerance_s:
        return False
    expected = sign(payload, ts).split("v1=")[1]
    return hmac.compare_digest(expected, parts.get("v1", ""))


def notify_ops(case_id, delay_s=0.0):
    """Simula a chamada síncrona para a fila de Ops (lenta em horário de pico)."""
    time.sleep(delay_s)


def handle_payment_succeeded(conn, provider, payload: bytes, signature: str, ops_delay_s=0.0) -> int:
    if not verify(payload, signature):
        return 400
    event = json.loads(payload)
    case_id = event["data"]["case_id"]
    row = conn.execute("SELECT customer_ref FROM cases WHERE id = ?", (case_id,)).fetchone()
    if row is None:
        return 404
    customer_ref = row[0]

    charge = provider.create_charge(customer_ref, FOLLOWUP_PRICE_CENTS)
    conn.execute(
        "INSERT INTO charges (case_id, provider_charge_id, amount_cents, provider_event_id) VALUES (?, ?, ?, ?)",
        (case_id, charge["id"], FOLLOWUP_PRICE_CENTS, event["id"]),
    )
    conn.execute("UPDATE cases SET status = 'paid' WHERE id = ?", (case_id,))
    conn.commit()

    notify_ops(case_id, ops_delay_s)
    return 200
