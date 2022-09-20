  
  def test_uma_segunda_feriado_às_14hs_o_banco_não_está_aberto(self):
    self.assertFalse(esta_aberto(True, "lunes", 14))
  
  
  def test_uma_quarta_feriado_às_20hs_o_banco_não_está_aberto(self):
    self.assertFalse(esta_aberto(True, "miércoles", 20))
  
  
  def test_uma_quinta_comum_às_13hs_o_banco_está_aberto(self):
    self.assertTrue(esta_aberto(False, "jueves", 13))
  
  
  def test_um_sábado_comum_às_11hs_o_banco_não_está_aberto(self):
    self.assertFalse(esta_aberto(False, "sábado", 11))
  
  
  def test_um_domingo_comum_às_19hs_o_banco_não_está_aberto(self):
    self.assertFalse(esta_aberto(False, "domingo", 19))
  
  
  def test_uma_terça_comum_às_16hs_o_banco_não_está_aberto(self):
    self.assertFalse(esta_aberto(False, "martes", 16))
  
