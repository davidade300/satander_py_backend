from datetime import date


class Pessoa:
    def __init__(self, nome: str, ano_nascimento: date) -> None:
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self) -> int:
        return date.today().year - self._ano_nascimento.year


p = Pessoa("David", date(1998, 4, 22))

print(f"Nome: {p.nome}\tIdade: {p.idade}")
