 
  def test_é_possível_concentrar_chá_95_true_é_verdadeiro(self):
    self.assertTrue(pode_se_concentrar("chá",95, True))

  def test_é_possível_concentrar_chá_100_true_é_verdadeiro(self):
    self.assertTrue(pode_se_concentrar("chá",100, True))

  def test_é_possível_concentrar_chimarrão_80_true_é_verdadeiro(self):
    self.assertTrue(pode_se_concentrar('chimarrão', 80, True))

  def test_é_possível_concentrar_chimarrão_70_true_é_falso(self):
    self.assertFalse(pode_se_concentrar('chimarrão', 70, True))

  def test_é_possível_concentrar_chá_94_true_é_falso(self):
    self.assertFalse(pode_se_concentrar("chá",94, True))

  def test_é_possível_concentrar_chá_95_false_é_falso(self):
    self.assertFalse(pode_se_concentrar("chá",95, False))