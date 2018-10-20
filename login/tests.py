from django.test import TestCase
from .seguridad import Seguridad

# Create your tests here.
class TestFree(TestCase):

    def setUp(self):
        self.s = Seguridad()

    """Primer Ciclo TDD"""
    # Frontera.
    def test_verificar_correo_valido(self):
        correo_valido = "moises@correo.com"
        es_valido = self.s.validar_correo(correo_valido)
        self.assertTrue(es_valido)


    """Segundo Ciclo TDD"""
    # Frontera
    def test_verificar_clave_valida(self):
        clave_valida = "Aaa12345"
        confirmacion = clave_valida
        es_valido = self.s.validar_clave(clave_valida, confirmacion)
        self.assertTrue(es_valido)

    """Tercer Ciclo TDD"""
    def test_registrar_usuario_valido_clave_valida(self):
        correo_valido = "moises@correo.com"
        clave_valida = "Aaa12345"
        confirmacion = clave_valida
        self.s.registrarUsuario(correo_valido, clave_valida, confirmacion)
        self.assertEqual(self.s.diccionario[correo_valido], clave_valida[::-1])
