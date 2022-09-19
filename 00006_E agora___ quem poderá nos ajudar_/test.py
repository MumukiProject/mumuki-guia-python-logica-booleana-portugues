  
  def test_uma_segunda_feriado_as_14hs_o_banco_nao_esta_aberto(self):
    self.assertFalse(esta_aberto(True, "lunes", 14))
  
  
  def test_uma_quarta_feriado_as_20hs_o_banco_nao_esta_aberto(self):
    self.assertFalse(esta_aberto(True, "miércoles", 20))
  
  
  def test_uma_quinta_comum_as_13hs_o_banco_esta_aberto(self):
    self.assertTrue(esta_aberto(False, "jueves", 13))
  
  
  def test_um_sabado_comum_as_11hs_o_banco_nao_esta_aberto(self):
    self.assertFalse(esta_aberto(False, "sábado", 11))
  
  
  def test_um_domingo_comum_as_19hs_o_banco_nao_esta_aberto(self):
    self.assertFalse(esta_aberto(False, "domingo", 19))
  
  
  def test_uma_terca_comum_as_16hs_o_banco_nao_esta_aberto(self):
    self.assertFalse(esta_aberto(False, "martes", 16))
  
