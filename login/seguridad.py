class Seguridad():

    def __init__(self):
        self.diccionario = {}

    # Usamos librerias de django para saber si el correo es valido
    def validar_correo(self,correo):
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email( correo )
            return True
        except ValidationError:
            return False

    # Se asegura que coinciden y cumplen con los requisistos
    def validar_clave(self, clave, confirmacion):
        import re
        if clave != confirmacion:
            return False

        regex_clave  = re.compile('(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,16}$')
        return bool(regex_clave.match(clave))

    # Agrega un par clave-valor a diccionario. El correo y la clave invertida
    def registrarUsuario(self, correo, clave, confirmacion):
        if not ( self.validar_correo(correo) and self.validar_clave(clave, confirmacion) ):
            return False
        self.diccionario[correo] = clave[::-1]
