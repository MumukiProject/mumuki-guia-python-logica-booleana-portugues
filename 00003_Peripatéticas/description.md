Outro dos operadores com o qual você já se encontrou é a conjunção lógica (também chamada _and_), que retorna apenas verdadeiro quando as duas expressões que operam são verdadeiras.

Podemos amarrar várias delas por meio do operador `and` e se alguma é falsa toda a expressão resultará falsa.

Por exemplo, se tenho a função...

```python
 def e_cantor_prolífico(cds_editados, shows_realizados, gravou_algum_dvd):
  return cds_editados >= 10 and shows_realizados > 25 and gravou_algum_dvd
```

...basta que um cantor não tenha gravado um DVD para não ser considerado prolífico, mesmo que já tenha editado mais de 10 CDs e  dado mais de 25 shows. :guitar:

> Defina uma função `e_peripatetica` que utilize a área em que uma pessoa se desenvolve profissionalmente, seu país de origem e a quantidade de quilômetros que caminha por dia. Uma pessoa é peripatética quando se desenvolve em filosofia, seu país de origem é a Grécia e  gosta de passear (caminha mais de 2 quilômetros por dia). Exemplo:
>
> ```python
> ム é_peripatetica("filosofia", "Grécia", 5)
True
> ム é_peripatetica("engenharia", "Uruguai", 1)
False
> ```

