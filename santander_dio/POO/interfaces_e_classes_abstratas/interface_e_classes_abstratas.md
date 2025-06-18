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
