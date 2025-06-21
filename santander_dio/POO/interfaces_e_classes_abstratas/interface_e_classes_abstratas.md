# Atributos de classe e Atributos do objeto

- Todos os objetos nascem com o mesmo numero de atributos de classe e de instancia.
- Atributos de instancia são diferentes para cada objeto (cada objeto tem uma copia).
- Atributos de classe sao compatilhados entre os objetos.

## Metodos de classe

- Metodos que em vez de apontar para a instância do objeto, apontam para a classe.
- Tem acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instnaica do objeto
- por convençao, recebem o parametro da classe como *cls*

## Metodos estaticos

- Nao recebem um primeiro argumento explicito.
- Metodo vinculado a classe e nao ao objeto da classe.
- Nao pode acessar ou modificar o estado da classe
- Esta presente em uma classe porque faz sentido que esteja presente na classe.

## Metodos de classe x metodos estaticos

- Metodo de classe:
  - recebe um primeiro parametro que aponta para a classe.
  - pode acessar ou modificar o estado da classe.
  - Geralmente usado para criar metodos de fabrica. -> (retorna uma nova instancia do objeto)
  - Geralmente usado para criar funcoes utilitarias -> (validadores, etc)

## Classes abstratas

### Interfaces

- Definem o que uma classe deve fazer e não como ela deve fazer.
- O conceito de interface pode ser entendido como um contrato, onde os metodos são declarados (o que deve ser feito) e suas respectivas assinaturas. Em Python, utilizamos classes abstratas para criar contratos, classes abstratas não podem ser instanciadas.

## ABC - *A*bstract *B*ase *C*lasses

- Por padrão, python não fornece classes abstratas. O módulo *ABC* fornece a base para definir as classes abstratas. Este, funciona decorando metodos da classe base como abstratos e, em seguida, registrando classes concretas como implementações da base abstrata. Um método se torna abstrato quando decorado com *@abstractmethod*

```python
from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto): # toda classe que estende uma classe abstrata deve implementar seus métodos
    def ligar(self):
        print("Ligando")

    def desligar(self):
        print("Desligando")

```
