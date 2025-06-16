class Passaro:
    def voar(self) -> None:
        pass


class Pardal(Passaro):
    def voar(self) -> None:
        print("Pardal voa")


class Avestruz(Passaro):
    def voar(self) -> None:
        print("Avestruz nao voa")


def plano_de_voo(Passaro) -> None:
    Passaro.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())
