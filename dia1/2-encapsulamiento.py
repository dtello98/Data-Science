#ENCAPSULAMIENTO EN POO CON PYTHON
class Usuario:
    
    __usuario_email = 'admin@gmail.com'
    __usuario_password = '123'
    
    def __ini__(self):
        pass
    
    def login(self,email,password):
        if email == self.__usuario_email and password == self.__usuario_password:
            print('Login exitoso')
        else:
            print('Login fallido')
            
print("LOGIN DE USUARIO")
email = input('Ingrese su email: ')
password = input('Ingrese su password: ')

usuario = Usuario()
usuario.login(email, password)