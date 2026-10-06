"""Testes existentes (passam). Sua tarefa: escrever o teste de regressão que FALHA com o código atual.

Rodar:  python -m unittest -v   (dentro desta pasta)   ou   python -m pytest
"""
import json
import sqlite3
import time
import unittest

from fake_provider import FakeProvider
from handler import handle_payment_succeeded, init_db, sign


def evento(event_id="evt_1", case_id="case_1"):
    return json.dumps({"id": event_id, "type": "payment.succeeded", "data": {"case_id": case_id}}).encode()


class HandlerTest(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        init_db(self.conn)
        self.conn.execute("INSERT INTO cases VALUES ('case_1', 'cus_fake_1', 'opened')")
        self.provider = FakeProvider()

    def test_assinatura_invalida_retorna_400(self):
        status = handle_payment_succeeded(self.conn, self.provider, evento(), "t=1,v1=errada")
        self.assertEqual(status, 400)
        self.assertEqual(self.provider.charges, [])

    def test_caminho_feliz_cobra_e_marca_pago(self):
        payload = evento()
        status = handle_payment_succeeded(self.conn, self.provider, payload, sign(payload, int(time.time())))
        self.assertEqual(status, 200)
        self.assertEqual(len(self.provider.charges), 1)
        (st,) = self.conn.execute("SELECT status FROM cases WHERE id = 'case_1'").fetchone()
        self.assertEqual(st, "paid")

    # TODO (exercício D10): teste de regressão que reproduz o incidente.


if __name__ == "__main__":
    unittest.main()
