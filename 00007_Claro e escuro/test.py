  
  def test_tem_contraste_branco_preto_e_verdadeiro(self):
    self.assertTrue(tem_contraste("blanco","negro"))

  def test_tiene_contraste_beige_rosa_es_falso(self):
    self.assertFalse(tem_contraste("beige","rosa"))

  def test_tiene_contraste_rojo_azul_es_falso(self):
    self.assertFalse(tem_contraste("rojo","azul"))

  def test_tiene_contraste_negro_amarillo_es_verdadero(self):
    self.assertTrue(tem_contraste("negro","amarillo"))