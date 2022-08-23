  
  def test_alguien_de_20_anios_es_mayor_de_edad(self):
    self.assertTrue(e_maior_de_idade(20))
  
  
  def test_alguien_de_18_anios_es_mayor_de_edad(self):
    self.assertTrue(e_maior_de_idade(18))
  
  
  def test_alguien_de_17_anios_no_es_mayor_de_edad(self):
    self.assertFalse(e_maior_de_idade(17))
  
  
  def test_alguien_de_16_anios_no_es_mayor_de_edad(self):
    self.assertFalse(e_maior_de_idade(16))
  
  
  def test_alguien_de_20_anios_no_es_menor_de_edad(self):
    self.assertFalse(e_menor_de_idade(20))
  
  
  def test_alguien_de_18_anios_no_es_menor_de_edad(self):
    self.assertFalse(e_menor_de_idade(18))
  
  
  def test_alguien_de_17_anios_es_menor_de_edad(self):
    self.assertTrue(e_menor_de_idade(17))
  
  
  def test_alguien_de_16_anios_es_menor_de_edad(self):
    self.assertTrue(e_menor_de_idade(16))
  
