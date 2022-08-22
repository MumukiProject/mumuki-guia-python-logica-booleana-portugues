E se fosse suficiente que apenas uma das várias condições se cumprissem para afirmar que uma expressão é verdadeira? Podemos utilizar outro dos operadores que você já conhece, a disjunção lógica `or`! :bulb:

No famoso jogo T.E.G., um jogador pode ganhar de duas formas: por cumprir seu objetivo secreto ou por alcançar o objetivo geral de conquistar 30 países:

```python
def ganhou(cumpriu_objetivo_secreto, quantidade_de_paises_conquistados):
  return cumpriu_objetivo_secreto ou quantidade_de_paises_conquistados >= 30

```

> Teste no console as seguintes expressões:
>
>``` python
ムganhou(True, 25)
```
>
>``` python
ムganhou(False, 30)
```
>
>``` python
ムganhou(False, 20)
```
>
>``` python
ムganhou(True, 31)
```
> Você se anima a construir a tabela de verdade da disjunção lógica?

