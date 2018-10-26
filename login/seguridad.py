# Clase seguridad la cual se encarga de verificar si un usuario es valido para registrarse o ingresar
#  Los requisitos son : 
#           El correo cumple con el formato RFC822
#           La clave debe poseer entre 8 y 16 caracteres (ambos incluidos)
#           La clave debe tener al menos 3 letras
#           La clave debe poseer al menos una letra mayuscula
#           La clave debe poseer al menos una letra minuscula
#           La clave debe poseer al menos un digito
#           La clave no debe poseer elementos distintos a letras y numeros
class Seguridad():

    def __init__(self):
        self.diccionario = {}

    # Usamos librerias de django para saber si el correo cumple con el RFC822
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

        regex_clave  = re.compile('(?=.*[A-Z]+)(?=.*[a-z]+)(?=.*[a-zA-z]{3})(?=.*\d+)[A-Za-z\d]{8,16}$')
        return bool(regex_clave.match(clave))

    # Agrega un par clave-valor a diccionario. El correo y la clave invertida
    def registrarUsuario(self, correo, clave, confirmacion):
        msg_list = []
        if not  self.validar_correo(correo):
            msg_list.append("Correo electrónico inválido")
        if not self.validar_clave(clave, confirmacion):
            msg_list.append("Clave inválida""")
        if self.validar_clave(clave, confirmacion) and self.validar_correo(correo):
            self.diccionario[correo] = clave[::-1]

        return msg_list

    # Log usuario
    def ingresarUsuario(self, correo, clave):
        msg = "Usuario inválido"
        if correo in self.diccionario:
            if clave[::-1] == self.diccionario[correo]:
                msg = "Usuario aceptado"
                return msg
            else :
                msg = "Clave inválida"
                return msg

        return msg