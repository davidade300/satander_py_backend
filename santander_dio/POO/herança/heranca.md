# O que é herança?

- Capacidade de uma classe filha derivar/ herdar caracteristicas ou comportamentos da classe pai.

## Benefícios da herança

- Representa bem relacionamentos do mundo real
- Fornece reutilização de codigo e adição de recursos a uma classe
- É de natureza transitiva, se *b* herda de *a*, todas as subclasses de *b* herdarão automaticamente de *a*

## Herança simples

- Quando a classe filha herda apenas de uma classe pai.

## Herança múltipla

- Quando a classe filha herda de varias classes pai.
- Não existe em todas as linguagens

```python
class A:
    pass

class B:
    pass

class C(A,B):
    pass
```
