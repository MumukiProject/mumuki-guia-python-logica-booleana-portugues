 
  def test_e_possivel_concentrar_cha_95_true_e_verdadeiro(self):
    self.assertTrue(pode_se_concentrar("chá",95, True))

  def test_e_possivel_concentrar_cha_100_true_e_verdadeiro(self):
    self.assertTrue(pode_se_concentrar("chá",100, True))

  def test_e_possivel_concentrar_chimarrao_80_true_e_verdadeiro(self):
    self.assertTrue(pode_se_concentrar('chimarrão', 80, True))

  def test_e_possivel_concentrar_chimarrao_70_true_e_falso(self):
    self.assertFalse(pode_se_concentrar('chimarrão', 70, True))

  def test_E_possivel_concentrar_cha_94_true_e_falso(self):
    self.assertFalse(pode_se_concentrar("chá",94, True))

  def test_e_possivel_concentrar_cha_95_false_e_falso(self):
    self.assertFalse(pode_se_concentrar("chá",95, False))