  
  def test_é_necessário_que_grécia_tenha_acento_e_esteja_em_letras_maiúsculas_para_saber_se_a_pessoa_é_peripatética(self):
    self.assertFalse(e_peripatetica("filosofia", "Grecia", 3))
    self.assertTrue(e_peripatetica("filosofia", "Grécia", 3))
  
  def test_uma_pessoa_que_tem_bom_desempenho_em_filosofia_é_da_grécia_e_caminha_3km_por_dia_é_peripatética(self):
    self.assertTrue(e_peripatetica("filosofia", "Grécia", 3) or e_peripatetica("filosofía", "Grécia", 3))
  
  def test_uma_pessoa_que_tem_bom_desempenho_em_filosofia_é_da_grécia_e_caminha_2km_por_dia_não_é_peripatética(self):
    self.assertFalse((e_peripatetica("filosofia", "Grécia", 2) or e_peripatetica("filosofía", "Grécia", 2)))
  
  def test_uma_pessoa_que_tem_bom_desempenho_em_filosofia_é_da_argentina_e_caminha_5km_por_dia_não_é_peripatética(self):
    self.assertFalse(e_peripatetica("filosofia", "Argentina", 5))
  
  def test_uma_pessoa_que_tem_bom_desempenho_em_atletismo_é_da_grécia_e_caminha__10km_por_dia_não_é_peripatética(self):
    self.assertFalse(e_peripatetica("atleta", "Grecia", 10))
  
  def test_uma_pessoa_que_tem_bom_desempenho_em_engenharia_é_da_colômbia_e_caminha_1km_por_dia_não_é_peripatética(self):
    self.assertFalse(e_peripatetica("profesor", "Colombia", 1))
  
