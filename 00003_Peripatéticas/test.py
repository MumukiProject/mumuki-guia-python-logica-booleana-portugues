  
  def test_e_necessario_que_grecia_tenha_acento_e_esteja_em_letras_maiusculas_para_saber_se_a_pessoa_e_peripatetica(self):
    self.assertFalse(e_peripatetica("filosofia", "Grecia", 3))
    self.assertTrue(e_peripatetica("filosofia", "Grécia", 3))
  
  def test_uma_pessoa_que_tem_bom_desempenho_em_filosofia_e_da_grecia_e_caminha_3km_por_dia_e_peripatetica(self):
    self.assertTrue(e_peripatetica("filosofia", "Grécia", 3) or e_peripatetica("filosofía", "Grécia", 3))
  
  def test_uma_pessoa_que_tem_bom_desempenho_em_filosofia_e_da_grecia_e_caminha_2km_por_dia_nao_e_peripatetica(self):
    self.assertFalse((e_peripatetica("filosofia", "Grécia", 2) or e_peripatetica("filosofía", "Grécia", 2)))
  
  def test_uma_pessoa_que_tem_bom_desempenho_em_filosofia_e_da_argentina_e_caminha_5km_por_dia_nao_e_peripatetica(self):
    self.assertFalse(e_peripatetica("filosofía", "Argentina", 5))
  
  def test_uma_pessoa_que_tem_bom_desempenho_em_atletismo_e_da_grecia_e_caminha__10km_por_dia_nao_e_peripatetica(self):
    self.assertFalse(e_peripatetica("atleta", "Grecia", 10))
  
  def test_uma_pessoa_que_tem_bom_desempenho_em_engenharia_e_da_colombia_e_caminha_1km_por_dia_nao_e_peripatetica(self):
    self.assertFalse(e_peripatetica("profesor", "Colombia", 1))
  
