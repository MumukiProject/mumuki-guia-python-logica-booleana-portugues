Na lógica booleana, é possível definir o comportamento de um operador com uma _tabela de verdade_ onde **A** e **B** são as expressões ou valores de verdade a ser operados e o símbolo **^** representa a conjunção.

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
	<th class ="text-center" style="width: 75px">A</th>
	<th class ="text-center" style="width: 75px">B</th>
	<th class ="text-center" style="width: 100px">A ^ B</th>
  </tr>
  <tr>
	<td>Verdadeiro</td>
	<td>Verdadeiro</td>
	<td>Verdadeiro</td>
  </tr>
  <tr>
	<td>Verdadeiro</td>
	<td>Falso</td>
	<td>Falso</td>
  </tr>
  <tr>
	<td>Falso</td>
	<td>Verdadeiro</td>
	<td>Falso</td>
  </tr>
  <tr>
	<td>Falso</td>
	<td>Falso</td>
	<td>Falso</td>
  </tr>
</table>

No mundo da lógica estas expressões são chamadas de _proposições_. Mas… que coisas podem ser uma proposição? :thought_balloon: Falta apenas que tenham um valor de verdade, ou seja, qualquer expressão booleana pode ser uma proposição.

> Para comprovar, teste no console a sua função `e_peripatetica` com os seguintes valores e confirme se ela se comporta como na tabela:
>
>``` python
ムe_peripatética("atletismo", "Argentina", 10)
```
>
>``` python
ムe_peripatética("filosofia", "Argentina", 3)
```
>
>``` python
ムe_peripatética("engenharia", "Canadá", 1)
```
>
>``` python
ムe_peripatética("filosofia", "Grécia", 5)
```
