Vamos começar por algo simples. Você lembra do operador `not` ? Ele é denominado operador de negação ou complemento lógico e serve para negar um valor booleano. Se tenho um booleano representado por `tem_fome`, o complemento será `not tem_fome`. :no_mouth:

Não parece uma ideia muito interessante, mas pode servir para reutilizar a lógica de uma função que já temos definida.

Por exemplo, se temos uma função `e_par`, basta negar a função para saber se um número é ímpar.

```python
def e_impar(numero):
  return not e_par(numero)

```

> Agora é a sua vez! Defina a função `e_maior_de_idade` e  logo `e_menor_de_idade` a partir dela.

