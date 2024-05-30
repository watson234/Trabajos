import datetime
class Persona:
    def __init__(self, nombre, cedula, fecha_nac, fecha_ing):
        #inserte aqeí el chequeo de restricciones
        self.nombre= nombre
        self.cedula = cedula
        self.fecha_nac= fecha_nac
        self.fecha_ing = fecha_ing

    def get_nombre(self):
        return self.nombre
    def set_nombre(self,nombre):
        #chequeo de restricciones
        self.nombre=nombre
    def get_cedula(self):
        return self.cedula
    def set_cedula(self,cedula):
        #chequeo de restricciones
        self.cedula=cedula
    def get_fecha_nac(self):
        return self.fecha_nac
    def set_fecha_nac(self,fecha_nac):
        #chequeo de restricciones
        self.fecha_nac=fecha_nac
    def get_fecha_ing(self):
        return self.fecha_ing
    def set_fecha_ing(self,fecha_ing):
        #chequeo de restricciones
        self.fecha_ing=fecha_ing
    def __str__(self):
        return f"Persona: {self.nombre}, {self.cedula}"
    def __repr__(self):
        return self.__str__()
    def calcular_antigüedad(self):
        hoy =datetime.date.today()
        dif = hoy - self.fecha_ing
        return dif.days // 365
    def edad(self):
        hoy =datetime.date.today()
        edad = hoy - self.fecha_nac
        return edad.days // 365
 
p=Persona("Waos","1-1423-5423",datetime.date(2000, 2, 20),datetime.date(2021, 5, 28))
i=Persona("Weboz","1-0000-5423",datetime.date(2000, 2, 20),datetime.date(2021, 5, 28))
