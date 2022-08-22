Quando uma expressão matemática possui vários operadores, sabemos que as multiplicações e divisões serão realizadas antes das adições e subtrações:

```python
5 * 3 + 8 / 4 - 3 = 14
```

Como na matemática, quando usamos operadores lógicos, as expressões são avaliadas em uma determinada ordem chamada _precedência_.

Qual é essa ordem? :thinking:

Tendo a função definida:

```python
def paga_com_cartao(cobra_se_juros, cartao, a vista_disponivel):
  return not cobra_se_juros and parcelas(cartao) >= 3 or a vista_disponivel < 100
```

> Tente descobrir qual é a precedência das operações booleanas. Damos alguns exemplos de tentativas...
>
>``` python
ムpaga_com_cartao(True, "visa", 320)
```
>
>``` python
ムpaga_com_cartao(False, "visa", 80)
```
>
>``` python
ムpaga_com_cartao(True, "mastercard", 215)
```
>
>``` python
ムpaga_com_cartao(True, "mastercard", 32)
```
> ... mas você pode tentar com os quais você desejar.

> Quando terminar, escreva `pronto()`.
