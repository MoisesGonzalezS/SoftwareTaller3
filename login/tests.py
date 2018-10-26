from django.test import TestCase
from .seguridad import Seguridad

# Create your tests here.
class TestFree(TestCase):

    def setUp(self):
        self.s = Seguridad()

    """Primer Ciclo TDD"""
    # Frontera.
    # verificamos que el correo cumpla con el RFC 822
    def test_verificar_correo_valido(self):
        correo_valido = "moises@correo.com"
        es_valido = self.s.validar_correo(correo_valido)
        self.assertTrue(es_valido)

    # Frontera.
    # El correo no cumple con el RFC 822 posee un caracter invalido
    def test_verificar_correo_no_valido3(self):
        correo_invalido = "<FrankZappa>@correo.com"
        es_valido = self.s.validar_correo(correo_invalido)
        self.assertFalse(es_valido)


    """Segundo Ciclo TDD"""
    # Frontera
    # Probamos que la clave introducida de 8 caracteres(minima cantidad permitida) sea valida y cumpla con los requisitos especificados en la 
    # tarea 3
    def test_verificar_clave_valida0(self):
        clave_valida = "Aaa12345"
        confirmacion = clave_valida
        es_valido = self.s.validar_clave(clave_valida, confirmacion)
        self.assertTrue(es_valido)

    # Frontera
    # Probamos que la clave introducida de 16 caracteres(maxima cantidad permitida) sea valida y cumpla con los requisitos especificados en la 
    # tarea 3
    def test_verificar_clave_valida1(self):
        clave_valida = "AAaaaa1234567890"
        confirmacion = clave_valida
        es_valido = self.s.validar_clave(clave_valida, confirmacion)
        self.assertTrue(es_valido)

    # Frontera
    # clave invalida ya que no posee digitos
    def test_verificar_clave_no_valida10(self):
        clave_valida = "PeachesEnRegalia"
        confirmacion = clave_valida
        es_valido = self.s.validar_clave(clave_valida, confirmacion)
        self.assertFalse(es_valido)

    # Frontera
    # clave invalida ya que no posee mayusculas
    def test_verificar_clave_no_valida11(self):
        clave_valida = "cosmikdebris15"
        confirmacion = clave_valida
        es_valido = self.s.validar_clave(clave_valida, confirmacion)
        self.assertFalse(es_valido)

    # Frontera
    # clave invalida ya que no posee minusculas
    def test_verificar_clave_no_valida11(self):
        clave_valida = "UNCLEREMMUS19"
        confirmacion = clave_valida
        es_valido = self.s.validar_clave(clave_valida, confirmacion)
        self.assertFalse(es_valido)

    # Frontera
    # clave invalida ya que no posee 3 letras
    def test_verificar_clave_no_valida11(self):
        clave_valida = "Aa1234567"
        confirmacion = clave_valida
        es_valido = self.s.validar_clave(clave_valida, confirmacion)
        self.assertFalse(es_valido)

    # Frontera
    # Probamos que la clave introducida sea valida con exactamente una mayuscula y cumpla con los requisitos especificados en la 
    # tarea 3
    def test_verificar_clave_valida2(self):
        clave_valida = "Aaaaaa123456"
        confirmacion = clave_valida
        es_valido = self.s.validar_clave(clave_valida, confirmacion)
        self.assertTrue(es_valido)

    # Frontera
    # Probamos que la clave introducida sea valida con exactamente una minuscula y cumpla con los requisitos especificados en la 
    # tarea 3
    def test_verificar_clave_valida3(self):
        clave_valida = "BLACKNAPKINs678"
        confirmacion = clave_valida
        es_valido = self.s.validar_clave(clave_valida, confirmacion)
        self.assertTrue(es_valido)

    # Frontera
    # Probamos que la clave introducida sea valida con exactamente un digito y cumpla con los requisitos especificados en la 
    # tarea 3
    def test_verificar_clave_valida4(self):
        clave_valida = "AAAAAaaa1"
        confirmacion = clave_valida
        es_valido = self.s.validar_clave(clave_valida, confirmacion)
        self.assertTrue(es_valido)

    # Frontera
    # Probamos que la clave introducida sea valida con exactamente 3 letras y cumpla con los requisitos especificados en la 
    # tarea 3
    def test_verificar_clave_valida5(self):
        clave_valida = "AAa123456"
        confirmacion = clave_valida
        es_valido = self.s.validar_clave(clave_valida, confirmacion)
        self.assertTrue(es_valido)

    # Frontera
    # Probamos que la clave introducida es invalida con 7 caracteres 
    def test_verificar_clave_no_valida(self):
        clave_invalida = "AAaa123"
        confirmacion = clave_invalida
        es_valido = self.s.validar_clave(clave_invalida, confirmacion)
        self.assertFalse(es_valido)

    # Frontera
    # Probamos que la clave introducida invalida con 17 caracteres 
    def test_verificar_clave_no_valida1(self):
        clave_invalida = "AAAAaaa1234567890"
        confirmacion = clave_invalida
        es_valido = self.s.validar_clave(clave_invalida, confirmacion)
        self.assertFalse(es_valido)


    """Tercer Ciclo TDD"""
    # Clave valida de 9 caracteres contiene 1 mayuscula,2 minusculas y 6 digitos
    # verificamos que se registra el usuario de manera satisfactoria
    def test_registrar_usuario_valido_clave_valida(self):
        correo_valido = "moises@correo.com"
        clave_valida = "Aaa123456"
        confirmacion = clave_valida
        self.s.registrarUsuario(correo_valido, clave_valida, confirmacion)
        self.assertEqual(self.s.diccionario[correo_valido], clave_valida[::-1])

    """Cuarto Ciclo TDD"""

    # Frontera
    # verificamos que la clave es valida, pero el correo no cumple con los requisitos necesarios
    def test_registrar_usuario_invalido_clave_valida(self):
        correo_invalido = "moises"
        clave_valida = "Aaa123456"
        confirmacion = clave_valida
        msj_list = self.s.registrarUsuario(correo_invalido, clave_valida, confirmacion)
        self.assertIn("Correo electrónico inválido", msj_list)

    # Frontera
    # verificamos que el correo cumple con el RFC822, pero la clave es invalida porque tiene 7 caracteres
    def test_registrar_usuario_valido_clave_invalida1(self):
        correo_invalido = "moises@correo.com"
        clave_valida = "Aaa1234"
        confirmacion = clave_valida
        msj_list = self.s.registrarUsuario(correo_invalido, clave_valida, confirmacion)
        self.assertIn("Clave inválida", msj_list)

    """Quinto ciclo TDD"""
    # Frontera, probamos que un usuario se registre satisfactoria
    def test_ingresar_usuario_valido_clave_valida1(self):
        correo_valido = "moises@correo.com"
        clave_valida = "Aaa12345"
        self.s.registrarUsuario(correo_valido, clave_valida, clave_valida)
        msj = self.s.ingresarUsuario(correo_valido, clave_valida)
        self.assertEqual(msj, "Usuario aceptado")

     # Frontera
    def test_ingresar_usuario_valido_clave_valida2(self):
        correo_invalido = "(moises)@correo.com"
        clave_valida = "Aaa12345"
        self.s.registrarUsuario(correo_invalido, clave_valida, clave_valida)
        msj = self.s.ingresarUsuario(correo_invalido, clave_valida)
        self.assertEqual(msj, "Usuario inválido")

    # Frontera 
    # la clave supera los 16 digitos
    def test_registrar_usuario_valido_clave_invalida2(self):
        correo_valido = "moises@correo.com"
        clave_invalida = "Aaa112233445566778899"
        confirmacion = clave_invalida
        msj_list = self.s.registrarUsuario(correo_valido, clave_invalida, confirmacion)
        self.assertIn("Clave inválida", msj_list)

    # Esquina 
    # correo invalido con caracteres no permitidos y clave invalida 7 digitos y caracter invalido 
    # y exactamente 3 letras
    def test_ingresar_usuario_invalido_clave_invalida3(self):
        correo_invalido = "Apostrophe()@correo.com"
        clave_invalida = "Aaa234$"
        self.s.registrarUsuario(correo_invalido, clave_invalida, clave_invalida)
        msj = self.s.ingresarUsuario(correo_invalido, clave_invalida)
        self.assertEqual(msj, "Usuario inválido")

    #Esquina 
    # correo invalido con caracteres no permitidos y clave invalida 7 digitos y caracter invalido
    # y 2 letras (1 mayuscula y 1 minuscula)
    def test_ingresar_usuario_invalido_clave_invalida4(self):
        correo_invalido = "Apostrophe()@correo.com"
        clave_invalida = "Aa1234$"
        self.s.registrarUsuario(correo_invalido, clave_invalida, clave_invalida)
        msj = self.s.ingresarUsuario(correo_invalido, clave_invalida)
        self.assertEqual(msj, "Usuario inválido")


    #Esquina correo invalido con caracteres no permitidos y clave invalida 17 digitos y caracter invalido
    def test_ingresar_usuario_invalido_clave_invalida5(self):
        correo_invalido = "Apostrophe()@correo.com"
        clave_invalida = "Aaaaaa1234567890$"
        self.s.registrarUsuario(correo_invalido, clave_invalida, clave_invalida)
        msj = self.s.ingresarUsuario(correo_invalido, clave_invalida)
        self.assertEqual(msj, "Usuario inválido")

    #Esquina 
    # correo invalido con caracteres no permitidos y clave invalida 17 digitos y caracter invalido
    # y 1 mayuscula
    def test_ingresar_usuario_invalido_clave_invalida6(self):
        correo_invalido = "Apostrophe()@correo.com"
        clave_invalida = "Aaaaaa1234567890$"
        self.s.registrarUsuario(correo_invalido, clave_invalida, clave_invalida)
        msj = self.s.ingresarUsuario(correo_invalido, clave_invalida)
        self.assertEqual(msj, "Usuario inválido")

    #Esquina
    # correo invalido tiene caracteres invalidos clave de  17 elementos con exactamente 3 letras 
    # y 1 mayuscula
    def test_ingresar_usuario_invalido_clave_invalida7(self):
        correo_invalido = "<WatermelonInEasterEgg>@correo.com"
        clave_invalida = "Aaa22334455667788"
        self.s.registrarUsuario(correo_invalido, clave_invalida, clave_invalida)
        msj = self.s.ingresarUsuario(correo_invalido, clave_invalida)
        self.assertEqual(msj, "Usuario inválido")

    #Esquina
    # correo valido (sin caracteres invalidos), clave de 8 elementos 
    # y 1 mayuscula y exactamente 3 letras
    def test_ingresar_usuario_valido_clave_valida01(self):
        correo_valido = "WatermelonInEasterEgg@correo.com"
        clave_valida = "Aaa12345"
        self.s.registrarUsuario(correo_valido, clave_valida, clave_valida)
        msj = self.s.ingresarUsuario(correo_valido, clave_valida)
        self.assertEqual(msj, "Usuario aceptado")

    #Esquina
    # correo valido (sin caracteres invalidos), clave de 8 elementos 
    # 1 minuscula y exactamente 3 letras
    def test_ingresar_usuario_valido_clave_valida02(self):
        correo_valido = "WatermelonInEasterEgg@correo.com"
        clave_valida = "AAa12345"
        self.s.registrarUsuario(correo_valido, clave_valida, clave_valida)
        msj = self.s.ingresarUsuario(correo_valido, clave_valida)
        self.assertEqual(msj, "Usuario aceptado")

    #Esquina
    # correo valido(sin caracteres invalidos), clave de 16 elementos  
    # 1 minuscula, 1 digitos
    def test_ingresar_usuario_valido_clave_valida03(self):
        correo_valido = "WatermelonInEasterEgg@correo.com"
        clave_valida = "AAAAAAAAAAAAAAa1"
        self.s.registrarUsuario(correo_valido, clave_valida, clave_valida)
        msj = self.s.ingresarUsuario(correo_valido, clave_valida)
        self.assertEqual(msj, "Usuario aceptado")

    #Esquina
    # correo valido(sin caracteres invalidos), clave de 16 elementos  
    # 1 mayuscula y 1 digitos
    def test_ingresar_usuario_valido_clave_valida04(self):
        correo_valido = "WatermelonInEasterEgg@correo.com"
        clave_valida = "Aaaaaaaaaaaaaaa4"
        self.s.registrarUsuario(correo_valido, clave_valida, clave_valida)
        msj = self.s.ingresarUsuario(correo_valido, clave_valida)
        self.assertEqual(msj, "Usuario aceptado")

    #Malicia
    # Usuario invalido, ya que agregaron una clave con un caracter especial
    def test_ingresar_usuario_valido_clave_invalida8(self):
        correo_valido = "moises@correo.com"
        clave_invalida = "Aa23456$"
        self.s.registrarUsuario(correo_valido, clave_invalida, clave_invalida)
        msj = self.s.ingresarUsuario(correo_valido, clave_invalida)
        self.assertEqual(msj, "Usuario inválido")

    #Malicia
    # Usuario invalido, ya que agregaron una clave con mas de 16 caracteres y 
    # un caracter especial
    def test_ingresar_usuario_valido_clave_invalida9(self):
        correo_valido = "moises@correo.com"
        clave_invalida = "Aa11223344556677889900$"
        self.s.registrarUsuario(correo_valido, clave_invalida, clave_invalida)
        msj = self.s.ingresarUsuario(correo_valido, clave_invalida)
        self.assertEqual(msj, "Usuario inválido")

    #Malicia
    # Usuario invalido, ya que agregaron una clave vacia, lo cual no es posible
    def test_ingresar_usuario_valido_clave_invalida10(self):
        correo_valido = "moises@correo.com"
        clave_invalida = ""
        self.s.registrarUsuario(correo_valido, clave_invalida, clave_invalida)
        msj = self.s.ingresarUsuario(correo_valido, clave_invalida)
        self.assertEqual(msj, "Usuario inválido")

    #Malicia
    # Usuario invalido, ya que agregaron un correo que no satisface el RFC822, lo cual no es posible
    def test_ingresar_usuario_valido_clave_invalida15(self):
        correo_invalido = "<FrankZappa>@correo.com"
        clave_valida = "Aaa123456"
        self.s.registrarUsuario(correo_invalido, clave_valida, clave_valida)
        msj = self.s.ingresarUsuario(correo_invalido, clave_valida)
        self.assertEqual(msj, "Usuario inválido")




