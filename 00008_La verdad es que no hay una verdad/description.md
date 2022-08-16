Ahora pensemos cómo sería la tabla de verdad que representa el comportamiento de la función que acabás de hacer.
 
La proposición es `es_tono_claro`, y el valor de verdad que porte dependerá de cada color que esté evaluando.

El booleano final resultará de operar estos colores mediante `tiene_contraste`:

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
    <th class ="text-center" style="padding: 5px 8px">la letra tiene tono claro</th>
    <th class ="text-center" style="padding: 5px 8px">el fondo tiene tono claro</th>
    <th class ="text-center" style="padding: 5px 8px">tiene contraste</th>
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

> Probá tu función `tiene_contraste` con los siguientes valores y comprobá si se comporta como la tabla:
>
>``` python
ムtiene_contraste("amarillo", "beige")
```
>
>``` python
ムtiene_contraste("azul", "violeta")
``` 
>
>``` python
ムtiene_contraste("blanco", "negro")
```