¿Y si delegamos? Podríamos separar la lógica de la siguiente manera:
 
```python
def se_puede_concentrar(infusion, temperatura, estaProgramando):
  return infusion_a_temperatura_correcta(infusion, temperatura) and estaProgramando
```

**Al delegar correctamente**, hay veces en las que no es necesario alterar el orden de precedencia, ¡otro punto a favor de la delegación! :muscle: