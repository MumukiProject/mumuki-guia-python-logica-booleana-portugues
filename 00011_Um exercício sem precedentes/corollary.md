E se _delegarmos_, ou seja, dividirmos nosso problema principal em várias funções mais pequenas? Poderíamos separar a lógica da seguinte forma: 
 
```python
def pode_se_concentrar(infusao, temperatura, estaProgramando):
  return infusao_a_temperatura_correta(infusao, temperatura) and estaProgramando
```

**Ao delegar corretamente**, há momentos em que não é necessário alterar a ordem de precedência, outro ponto a favor da delegação! :muscle:
