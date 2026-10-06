"""Provedor de pagamentos falso (só para o exercício D10). Conta cada cobrança criada."""


class FakeProvider:
    def __init__(self):
        self.charges = []
        self._by_key = {}

    def create_charge(self, customer_ref, amount_cents, idempotency_key=None):
        """Cria uma cobrança. Com idempotency_key, repetir a chamada devolve a mesma cobrança."""
        if idempotency_key is not None and idempotency_key in self._by_key:
            return self._by_key[idempotency_key]
        charge = {"id": f"ch_{len(self.charges) + 1}", "customer_ref": customer_ref, "amount_cents": amount_cents}
        self.charges.append(charge)
        if idempotency_key is not None:
            self._by_key[idempotency_key] = charge
        return charge
