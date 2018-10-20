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

    """Cuarto Ciclo TDD"""

    # Frontera
    def test_registrar_usuario_invalido_clave_valida(self):
        correo_invalido = "moises"
        clave_valida = "Aaa12345"
        confirmacion = clave_valida
        msj_list = self.s.registrarUsuario(correo_invalido, clave_valida, confirmacion)
        self.assertIn("Correo electrónico inválido", msj_list)

    # Frontera
    def test_registrar_usuario_valido_clave_invalida(self):
        correo_invalido = "moises@correo.com"
        clave_valida = "Aaa1234"
        confirmacion = clave_valida
        msj_list = self.s.registrarUsuario(correo_invalido, clave_valida, confirmacion)
        self.assertIn("Clave inválida", msj_list)

    """Quinto ciclo TDD"""
    def test_ingresar_usuario_valido_clave_valida(self):
        correo_valido = "moises@correo.com"
        clave_valida = "Aaa12345"
        self.s.registrarUsuario(correo_valido, clave_valida, clave_valida)
        msj = self.s.ingresarUsuario(correo_valido, clave_valida)
        self.assertEqual(msj, "Usuario aceptado")