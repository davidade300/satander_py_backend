# Proteção de acesso

- Encapsulamento descreve a ideia de agrupar dados e métodos que manipualam esses dados em uma unidade, impondo restrições ao acesso direto a variáveis e métodos, evitando a modificação acidental de dados, assim, a variável de um objeto só pode ser alterada pelo método desse objeto.

## Modificadores de acesso

- Em python não há palavras reservadas(keywords) para encapsulamento, usa-se convenções no nome do recurso para definir se a variável é pública ou privada.

  ### Definição

  - Público: Pode ser acessado de fora da classe.
  - Privado: Só Pode ser acessado pela classe.
  
  ```python
  class Conta:
    def __init__(self,saldo=0):
        self._saldo = saldo

    def depositar(self,valor):
        pass

    def sacar(self,valor):
        pass

  ```

## Propriedades

- com o `property()`. é possível criar atributos gerenciados(propriedades) em classes. Pode ser usado quando é preciso modificar a implementação interna sem alterar a API pública da classe.

```python
class Foo:
    def __init__(self, x=None):
        self._x = x

    @property # decorator pode ser entendido como uma função que executa antes da função
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0
        
foo = Foo(10)
print(foo.x) # >>> 10
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
```

- o decorator @property transforma um método em uma propriedade
