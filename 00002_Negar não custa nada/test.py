  
  def test_alguém_de_20_anos_é_maior_de_idade(self):
    self.assertTrue(e_maior_de_idade(20))
  
  
  def test_alguém_de_18_anos_é_maior_de_idade(self):
    self.assertTrue(e_maior_de_idade(18))
  
  
  def test_alguém_de_17_anos_não_é_maior_de_idade(self):
    self.assertFalse(e_maior_de_idade(17))
  
  
  def test_alguém_de_16_anos_não_é_maior_de_idade(self):
    self.assertFalse(e_maior_de_idade(16))
  
  
  def test_alguém_de_20_anos_não_é_menor_de_idade(self):
    self.assertFalse(e_menor_de_idade(20))
  
  
  def test_alguém_de_18_anos_não_é_menor_de_idade(self):
    self.assertFalse(e_menor_de_idade(18))
  
  
  def test_alguém_de_17_anos_é_menor_de_idade(self):
    self.assertTrue(e_menor_de_idade(17))
  
  
  def test_alguém_de_16_anos_é_menor_de_idade(self):
    self.assertTrue(e_menor_de_idade(16))
  
