Agora vamos mudar as proposições `a letra tem tom claro` e `o fundo tem tom claro` por proposições genéricas **A** e **B**. Além disso, vamos representar a operação que realiza `tem contraste` com o símbolo **⊻**. O que vamos obter é... uma nova tabela! :tada:

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
	<th class ="text-center" style="width: 75px">A</th>
	<th class ="text-center" style="width: 75px">B</th>
	<th class ="text-center" style="width: 100px">A ⊻ B</th>
  </tr>
  <tr>
	<td>V</td>
	<td>V</td>
	<td>F</td>
  </tr>
  <tr>
	<td>V</td>
	<td>F</td>
	<td>V</td>
  </tr>
  <tr>
	<td>F</td>
	<td>V</td>
	<td>V</td>
  </tr>
  <tr>
	<td>F</td>
	<td>F</td>
	<td>F</td>
  </tr>
</table>

Este comportamento existe como um operador dentro da lógica e é denominado `xor` ou disjunção lógica exclusiva.
 
Diferente dos `and`, `or` e `not`, o `xor` normalmente não está definido nas linguagens de programação. :cry: Mas, agora que você sabe como funciona, se em algum momento você necessitar, poderá defini-lo à mão. :wink:

> Vamos ver se você entendeu: defina uma função genérica `xor` que utilize dois booleanos e retorne o valor de verdade correspondente.

