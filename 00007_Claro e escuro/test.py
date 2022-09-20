  
  def test_tem_contraste_branco_preto_é_verdadeiro(self):
    self.assertTrue(tem_contraste("branco","preto"))

  def test_tem_contraste_bege_rosa_é_falso(self):
    self.assertFalse(tem_contraste("bege","rosa"))

  def test_tem_contraste_vermelho_azul_é_falso(self):
    self.assertFalse(tem_contraste("vermelho","azul"))

  def test_tem_contraste_preto_amarelo_é_verdadeiro(self):
    self.assertTrue(tem_contraste("preto","amarelo"))