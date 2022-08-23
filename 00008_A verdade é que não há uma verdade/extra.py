colores_claros = ["branco", "bege", "celeste", "rosa", "amarelo"]

def es_tono_claro(color):
  return color in colores_claros
  
def tem_contraste(letra, fondo):
  return es_tono_claro(letra) != es_tono_claro(fondo)