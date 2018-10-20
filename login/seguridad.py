class Seguridad():

    def __init__(self):
        pass

    # Método para validar una dirección de correo
    def validar_correo(self,correo):
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email( correo )
            return True
        except ValidationError:
            return False
