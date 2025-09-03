import unittest
from app import app

class TestFormulario(unittest.TestCase):

    def setUp(self):
        """Configurar cliente de teste"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_pagina_inicial(self):
        """Testar se a página inicial carrega corretamente"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Formulário de Requisitos', response.get_data(as_text=True))
    
    def test_formulario_vazio(self):
        """Testar envio de formulário vazio"""
        response = self.app.post('/', data={})
        self.assertEqual(response.status_code, 200)
        self.assertIn('obrigatório', response.get_data(as_text=True))
    
    def test_formulario_completo(self):
        """Testar envio de formulário completo"""
        dados_formulario = {
            'disponibilidade': '24 horas por dia',
            'registro': 'Banco de dados',
            'hospedagem': 'VPS (Servidor Virtual)',
            'estrutura': 'Tabela produtos com campos id, nome, estoque',
            'estoque': 'Valor fixo de 5 unidades',
            'produto_novo': 'Campo status com valores novo/usado',
            'email_config': 'Já tenho conta configurada',
            'responsavel': 'Álvaro - alvarodudadahoradh@gmail.com'
        }
        
        response = self.app.post('/', data=dados_formulario)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
