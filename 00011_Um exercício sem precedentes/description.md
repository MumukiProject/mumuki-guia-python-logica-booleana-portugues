Se você prestou atenção na função anterior, deve ter notado que a operação com maior precedência é a negação `!`, seguida da conjunção `&&` e  por último a disjunção `||`. Mas o que acontece se eu quero alterar a ordem em que se resolvem? :thought_balloon:

Assim como na matemática, podemos usar parênteses para agrupar as operações que queremos fazer primeiro.

Delfi pode se concentrar ao programar e tomar infusões, mas não qualquer infusão.Tem que ser chimarrão :mate: a exatamente 80ºC ou chá :tea: que esteja a pelo menos 95ºC.

> Defina a função `pode_se_concentrar` que recebe uma bebida, temperatura e um booleano que nos diz se Delfi está programando:
>
``` python
>ム pode_se_concentrar('chá', 100, True)
>True
>
>ム pode_se_concentrar('chimarrão', 70, True)
False
>
>ム pode_se_concentrar('chá', 95, False)
>False
```
> Tente resolver em uma única função! Depois vamos ver como ficaria se delegamos.
