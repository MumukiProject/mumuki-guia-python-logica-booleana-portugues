  
  def test_uma_pessoa_que_mede_1_5m_não_está_acompanhada_por_um_adulto_e_não_tem_problemas_cardíacos_pode_subir_para_a_atração(self):
    self.assertTrue(pode_subir(1.5, False, False))
  
  def test_uma_pessoa_que_mede_1_7m_não_está_acompanhada_por_um_adulto_e_tem_problemas_cardíacos_não_pode_subir_para_a_atração(self):
    self.assertFalse(pode_subir(1.7, False, True))
  
  def test_uma_pessoa_que_mede_1_2m_está_acompanhada_por_um_adulto_e_não_tem_problemas_cardíacos_pode_subir_para_a_atração(self):
    self.assertTrue(pode_subir(1.2, True, False))
  
  def test_uma_pessoa_que_mede_1_2m_não_está_acompanhada_por_um_adulto_e_não_tem_problemas_cardíacos_não_pode_subir_para_a_atração(self):
    self.assertFalse(pode_subir(1.2, False, False))
  
  def test_uma_pessoa_que_mede_1_1m_está_acompanhada_por_um_adulto_e_não_tem_problemas_cardíacos_não_pode_subir_para_a_atração(self):
    self.assertFalse(pode_subir(1.1, True, False))
  
