class Conta:
    def __init__(self, nro_agencia: str, saldo: float = 0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor: float) -> None:
        self._saldo += valor

    def sacar(self, valor: float) -> None:
        self._saldo -= valor

    def mostrar_saldo(self) -> float:
        return self._saldo


conta = Conta("001", 100)

conta.depositar(100)
print(conta._saldo)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
