Decifrou a precedência das operações booleanas? :thinking: Por via das dúvidas aqui temos um quadro com a precedência delas e de algumas operações que já vimos (e outras que não):


<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
	<th class ="text-center" style="width: 10px">Prioridade</th>
	<th class ="text-center" style="width: 75px">Operações</th>
	<th class ="text-center" style="width: 75px">Descrição</th>
  </tr>
  <tr>
	<td>1</td>
	<td>**</td>
	<td>Exponenciação</td>
  </tr>
  <tr>
	<td>2</td>
	<td>*,  /,  %</td>
	<td>Multiplicação, divisão, resto</td>
  </tr>
  <tr>
	<td>3</td>
	<td>+,  -</td>
	<td>Soma, subtração</td>
  </tr>
  <tr>
	<td>4</td>
	<td>in,  <,  <=,  >,  >=,  ==,  !=</td>
	<td>Adesão, comparações</td>
  </tr>
  <tr>
	<td>5</td>
	<td>not</td>
	<td>Negação lógica</td>
  </tr>
  <tr>
	<td>6</td>
	<td>and</td>
	<td>Conjunção lógica</td>
  </tr>
  <tr>
	<td>7</td>
	<td>or</td>
	<td>Disjunção lógica</td>
  </tr>
</table>

Nesta  tabela a precedência vai do maior para o menor, ou seja, a prioridade 1 é a  maior e a prioridade 7 é a menor. Por exemplo, se fazemos...

``` python
8 + 2 * 3 < 15 and not 5 == 4
```

... obteremos `True` já que as operações são resolvidas nessa ordem:

1. `2 * 3` que retorna `6` então: `8 + 6 < 15 and not 5 == 4`
2. `8 + 6` que retorna `14` então: `14 < 15 and not 5 == 4`
3. `14 < 15` que retorna `True` então: `True and not 5 == 4`
4. `5 == 4` que retorna `False` então: `True and not False`
5. `not False` que retorna `True` então: `True and True`
6. `True and True` que finalmente retorna `True`.
