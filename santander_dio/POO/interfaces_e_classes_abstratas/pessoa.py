class Pessoa:
    def __init__(
        self, nome: str | None = None, idade: int | None = None
    ) -> None:
        self.nome: str | None = nome
        self.idade: int | None = idade

    @classmethod  # metodo de classe, metodo do tipo fabrica
    def criar_apartir_dob(cls, ano: int, mes: int, dia: int, nome: str):
        idade: int = 2025 - ano
        return cls(nome, idade)

    @staticmethod
    def not_underage(idade: int):
        return idade >= 18


# p = Pessoa("David", 27)
# print(p.nome, p.idade)

p = Pessoa.criar_apartir_dob(1998, 4, 22, "David")
print(p.idade, p.nome)

print(Pessoa.not_underage(18))
print(Pessoa.not_underage(17))
