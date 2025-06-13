from typing import Any


class Foo:
    def __init__(self, x=None):
        self._x = x

    @property  # decorator pode ser entendido como uma função que executa antes da função
    def x(self) -> Any | int:
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0
        # del self._x # -> fara com que código executado apos retorne erro


foo = Foo(10)
print(foo.x)  # >>> 10
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
