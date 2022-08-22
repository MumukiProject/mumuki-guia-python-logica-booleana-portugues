Agora vamos pensar como seria a tabela de verdade que representa o comportamento da função que você acabou de fazer.
 
A proposição é `e_tom_claro`, e o valor de verdade que leve dependerá de cada cor que estiver avaliando.

O booleano final resultará de operar estas cores por meio de `tem_contraste`:

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
	<th class ="text-center" style="padding: 5px 8px">a letra tem tom claro</th>
	<th class ="text-center" style="padding: 5px 8px">o fundo tem tom claro</th>
	<th class ="text-center" style="padding: 5px 8px">tem contraste</th>
  </tr>
  <tr>
	<td>True</td>
	<td>True</td>
	<td>False</td>
  </tr>
  <tr>
	<td>True</td>
	<td>False</td>
	<td>True</td>
  </tr>
  <tr>
	<td>False</td>
	<td>True</td>
	<td>True</td>
  </tr>
  <tr>
	<td>False</td>
	<td>False</td>
	<td>False</td>
  </tr>
</table>

> Teste a sua função `tem_contraste` com os seguintes valores e comprove se comporta-se como a tabela:
>
>``` python
ムtem_contraste("amarelo", "bege")
```
>
>``` python
ムtem_contraste("azul", "violeta")
```
>
>``` python
ムtem_contraste("branco", "preto")
```
