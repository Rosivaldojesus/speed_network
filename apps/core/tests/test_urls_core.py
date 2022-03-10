from django.test import TestCase
from django.urls import reverse
from django.test import Client

# Create your tests here.

class CoreUrlsTest(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_core_index_url_is_correct(self):
        url = reverse('core:core_index')
        self.assertEqual(url, '/')

    def test_core_login_url_is_correct(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_core_logout_url_is_correct(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)

    def test_core_login_submit_url_is_correct(self):
        urls = reverse('core:login_submit')
        self.assertEqual(urls, '/login/submit')

    def test_core_senhas_url_is_correct(self):
        url = reverse('core:senhas_gerais')
        self.assertEqual(url, '/senhas/')

    def test_core_manuais_urls_is_correct(self):
        url = reverse('core:manuais_gerais')
        self.assertEqual(url, '/manuais/')

    def test_core_manuais_visualizacao_urls_is_correct(self):
        url = reverse('core:manuais_visualizacao')
        self.assertEqual(url, '/manuais/manuais-visualizacao/')

    def test_core_senha_por_equipamento_urls_is_correct(self):
        url = reverse('core:senhas_por_equipamento')
        self.assertEqual(url, '/senhas-por-equipamento/')

    def test_core_cadastro_senhas_equipamentos_urls_is_correct(self):
        url = reverse('core:cadastro_senhas_equipamentos')
        self.assertEqual(url, '/cadastro-senhas-equipamentos/')

    def test_core_editar_senhas_equipamentos_urls_is_correct(self):
        url = reverse('core:editar_senhas_equipamentos', kwargs={'id': 1})
        self.assertEqual(url, '/editar-senhas-equipamentos/1')
