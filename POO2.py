class Autor:
    def __init__(self,nombre,nacionalidad):
        if type(nombre)!=str or str=="":
            raise Exception("nombre debe ser un string válido")
        if type(nacionalidad)!=str or str=="":
            raise Exception("nacionalidad debe ser un string válido")
        self.nombre=nombre
        self.nacionalidad=nacionalidad
    def get_nombre(self):
        return self.nombre
    def set_nombre(self,nombre):
        if type(nombre)!=str or str=="":
            raise Exception("nombre debe ser un string válido")
        self.nombre=nombre
    def get_nacionalidad(self):
        return self.nacionalidad
    def set_nacionalidad(self,nacionalidad):
        if type(nacionalidad)!=str or str=="":
            raise Exception("nacionalidad debe ser un string válido")
        self.nacionalidad=nacionalidad

    def __repr__(self):
        return f"Autor: ( {self.nombre}, {self.nacionalidad})"
class Libro:
    def __init__(self,titulo,ISBN,idioma,año):
        if type(titulo)!=str or str=="":
            raise Exception("Titulo debe ser un string válido")
        if type(idioma)!=str or str=="":
            raise Exception("Idioma debe ser un string válido")
        if type(ISBN)!=str or str=="":
            raise Exception("ISBN debe ser un string válido")
        if type(año)!=int:
                raise Exception("año debe ser un string válido")
        self.titulo = titulo
        self.ISBN = ISBN
        self.idioma = idioma
        self.año = año
        self.autores=[]
    def self_titulo(self):
        return self.titulo
    
    def self_titulo(self,titulo):
        if type(titulo)!=str or str=="":
            raise Exception("Titulo debe ser un string válido")
        self.titulo = titulo
        
    def self_ISBN(self):
        return self.ISBN
    
    def self_ISBN(self,ISBN):
        if type(ISBN)!=str or str=="":
            raise Exception("ISBN debe ser un string válido")
        self.ISBN = ISBN
        
    def self_idioma(self):
        return self.idioma
    
    def self_idioma(self,idioma):
        if type(idioma)!=str or str=="":
            raise Exception("Idioma debe ser un string válido")
        self.idioma = idioma
        
    def self_año(self):
        return self.año
    
    def self_año(self,año):
        if type(año)!=int:
            raise Exception("año debe ser un string válido")
        self.año = año

    def agregar_autor(self,autor):
        if not isinstance(autor,Autor):
            raise Exception("autor debe ser un tipo Autor.")
        self.autores.append(autor)

    def borrar_autor(self,autor):
        if not isinstance(autor,Autor):
            raise Exception("autor debe ser un tipo Autor.")
        if autor not in self.autores:
            raise Exception("el autor no se encuentra en la lista.")
        self.autores.remove(autor)
        
    def __repr__(self):
        s = f"Libro({self.titulo}, {self.ISBN}, {self.año}\n"
        for a  in self.autores:
            s+="\t" + str(a) + "\n"
        return s
        
