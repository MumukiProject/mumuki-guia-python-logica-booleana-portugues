  
  def test_a_disjuncao_logica_exclusiva_entre_True_e_True_da_False(self):
    self.assertFalse(xor(True, True))
  
  
  def test_a_disjuncao_logica_exclusiva_entre_True_e_False_da_True(self):
    self.assertTrue(xor(True, False))
  
  
  def test_a_disjuncao_logica_exclusiva_entre_False_e_True_da_True(self):
    self.assertTrue(xor(False, True))
  
  
  def test_a_disjuncao_logica_exclusiva_entre_False_e_False_da_False(self):
    self.assertFalse(xor(False, False))
  
