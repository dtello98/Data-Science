# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# Las clases son plantillas para crear objetos (instancias)
# Una clase puede tener atributos (características) y métodos (funciones)
class Automovil:
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
        
    def encender(self):
        print(f"Encendiendo el automóvil {self.marca} con placa {self.placa}")
        
    def avanzar(self):
        print(f"El automóvil {self.marca} está avanzando")
        
    def acelerar(self):
        print(f"El automóvil {self.marca} está acelerando")
        
    def frenar(self):
        print(f"El automóvil {self.marca} está frenando")
        
vw = Automovil(1970,'CH-1234','Amarillo','Volkswagen')
vw.encender()
vw.avanzar()
vw.acelerar()
vw.frenar()

tico = Automovil(2005,'P-5678','Rojo','Tico')
tico.encender()
tico.avanzar()
tico.acelerar()
tico.frenar()