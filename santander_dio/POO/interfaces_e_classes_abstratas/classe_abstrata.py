from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    """classes abstratas não odem ser instanciadas apenas herdadas
    as classes que estendem uma ABC devem implementar todos os seus metodos
    (basicamente uma interface do java)

    para metodos serem considerados abstratos eles devem ser decorados como @abstractmethod
    Args:
        ABC (_type_): _description_
    """

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property  # type: ignore
    # @abstractproperty # -> deprecated
    @abstractmethod
    def marca(self):
        pass


class ControleTV(
    ControleRemoto
):  # toda classe que estende uma classe abstrata deve implementar seus métodos
    def ligar(self):
        print("Ligando")

    def desligar(self):
        print("Desligando")

    @property
    def marca(self):  # type: ignore
        return "LG"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("ligando ar")

    def desligar(self):
        print("desligando ar")

    @property
    def marca(self):  # type: ignore
        return "LG"


controle = ControleTV()

controle.ligar()
controle.desligar()

controle_ar = ControleArCondicionado()

controle_ar.ligar()
controle_ar.desligar()

print(controle.marca)
