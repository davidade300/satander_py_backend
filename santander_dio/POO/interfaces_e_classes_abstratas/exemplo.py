class Estudante:
    # atributo/variável de classe, o mesmo valor para todo objeto
    escola: str = "DIO"

    def __init__(self, nome, matricula) -> None:
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("david", 1)
aluno_2 = Estudante("oliveira", 2)

mostrar_valores(aluno_1, aluno_2)

aluno_1.matricula = 3
Estudante.escola = "asdf"
mostrar_valores(aluno_1, aluno_2)
