"""Codigos de heranca simples"""


class Veiculo:
    def __init__(self, cor: str, placa: str, numero_rodas: int) -> None:
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando o motor")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(
        self, cor: str, placa: str, numero_rodas: int, carregado: bool = False
    ) -> None:
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Nao'} esta carregado")


moto = Motocicleta("verde", "placa", 4)
moto.ligar_motor()

carro = Carro("branco", "xde", 4)
carro.ligar_motor()

caminhao = Caminhao("azul", "xcv", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(carro)
print(moto)
print(caminhao)
