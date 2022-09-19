  
  def test_uma_pessoa_que_mede_1_5m_nao_esta_acompanhada_por_um_adulto_e_nao_tem_problemas_cardiacos_pode_subir_para_a_atracao(self):
    self.assertTrue(pode_subir(1.5, False, False))
  
  def test_uma_pessoa_que_mede_1_7m_nao_esta_acompanhada_por_um_adulto_e_tem_problemas_cardiacos_nao_pode_subir_para_a_atracao(self):
    self.assertFalse(pode_subir(1.7, False, True))
  
  def test_uma_pessoa_que_mede_1_2m_esta_acompanhada_por_um_adulto_e_nao_tem_problemas_cardiacos_pode_subir_para_a_atracao(self):
    self.assertTrue(pode_subir(1.2, True, False))
  
  def test_uma_pessoa_que_mede_1_2m_nao_esta_acompanhada_por_um_adulto_e_nao_tem_problemas_cardiacos_nao_pode_subir_para_a_atracao(self):
    self.assertFalse(pode_subir(1.2, False, False))
  
  def test_uma_pessoa_que_mede_1_1m_esta_acompanhada_por_um_adulto_e_nao_tem_problemas_cardiacos_nao_pode_subir_para_a_atracao(self):
    self.assertFalse(pode_subir(1.1, True, False))
  
