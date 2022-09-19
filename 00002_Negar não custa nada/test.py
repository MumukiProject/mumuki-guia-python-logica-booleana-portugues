  
  def test_alguem_de_20_anos_e_maior_de_idade(self):
    self.assertTrue(e_maior_de_idade(20))
  
  
  def test_alguem_de_18_anos_e_maior_de_idade(self):
    self.assertTrue(e_maior_de_idade(18))
  
  
  def test_alguem_de_17_anos_nao_e_maior_de_idade(self):
    self.assertFalse(e_maior_de_idade(17))
  
  
  def test_alguem_de_16_anos_nao_e_maior_de_idade(self):
    self.assertFalse(e_maior_de_idade(16))
  
  
  def test_alguem_de_20_anos_nao_e_menor_de_idade(self):
    self.assertFalse(e_menor_de_idade(20))
  
  
  def test_alguem_de_18_anos_nao_e_menor_de_idade(self):
    self.assertFalse(e_menor_de_idade(18))
  
  
  def test_alguem_de_17_anos_e_menor_de_idade(self):
    self.assertTrue(e_menor_de_idade(17))
  
  
  def test_alguem_de_16_anos_e_menor_de_idade(self):
    self.assertTrue(e_menor_de_idade(16))
  
