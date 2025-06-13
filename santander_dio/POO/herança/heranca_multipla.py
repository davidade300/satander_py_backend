"""Codigos de heranca multipla"""


class Animal:
    def __init__(self, nro_patas: int) -> None:
        self.nro_patas = nro_patas

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo: str, **kw) -> None:
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico: str, **kw) -> None:
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo: str, cor_bico: str, nro_patas: int) -> None:
        print(Ornitorrinco.__mro__)  # method resolution order
        super().__init__(
            cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas
        )


ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="vermelho", cor_bico="preto")
print(ornitorrinco)

gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)
