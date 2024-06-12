import pygame
from pygame.math import Vector2
from math import pi
from random import uniform, randint
import pickle
from os.path import getsize
import easygui

q = 2.0
o = 0.1
p = False

class Agent:
    """
    Clase que crea agentes y tiene sus metodos
    Entradas y restricciones:
    ninguna
    salida:
    agentes y sus metdodos
    """
    def __init__(self, window, x:float, y:float):
        """
        Funcion que constructora que crea los agentes
        entradas y restricciones:
        Self: agente
        window: ventana de pygame
        x:valor flotante de la cordenada x
        y:valor flotante de la cordenada y
        salidas:
        ninguna
        """
        self.window = window
        self.pos = Vector2(x, y)
        self.vel = Vector2(uniform(-q, q),uniform(-q, q))
        self.acc = Vector2(uniform(-o, o),uniform(-o, o))
        self.color = (randint(150,255), randint(50,255), randint(0,125))
        self.r = randint(10, 30)
        self.masa = pi * self.r**2
        self.damp = 1.0

    def __getstate__(self):
        """
        obtiene el estado del programa
        entradas y restricciones:
        Self: agente
        salidas:
        devuelve el estado actual
        """
        state = self.__dict__.copy()
        del state["window"]
        return state

    def __setstate__(self, state):
        """
        restaura el estado del programa
        entradas y restricciones:
        Self: agente
        salidas:
        carga el estado del programa
        """
        self.__dict__.update(state)
        self.window = pygame.display.set_mode((720,480))
        
    def draw(self):
        """
        metodo que que dibuja al agente
        entradas y restricciones:
        Self: agente
        salidas:
        dibuja al agente
        """
        #dibuja los elementos en pantalla
        pygame.draw.circle(self.window, self.color, (int(self.pos.x), int(self.pos.y)), self.r)
    def update(self):
        """
        metodo que que actualiza losa gentes en pantalla
        entradas y restricciones:
        Self: agente
        salidas:
        refresco de la pantalla
        """
        #cambia la pocisión de los agentes
        self.pos += self.vel
        self.vel += self.acc
        self.acc *= 0

    def borders(self):
        """
        metodo que verifica si un agente esta tocando con los bordes de la pantalla
        entradas y restricciones:
        Self: agente
        salidas:
        cambia la posiciony velocidad del agente si este esta tocando o tras pasando el borde
        """
        #reducción de velocidad al tocar los bordes
        if self.pos.x <= self.r+0 or self.pos.x>=self.window.get_width()-self.r:
            self.vel.x*=-0.8
        if self.pos.y <= self.r+0 or self.pos.y>=self.window.get_height()-self.r:
            self.vel.y*=-0.8
            
        self.pos.x=min(self.pos.x, self.window.get_width()-self.r)
        self.pos.x=max(self.pos.x, self.r)
        self.pos.y=min(self.pos.y, self.window.get_height()-self.r)
        self.pos.y=max(self.pos.y, self.r)

    def apply_force(self, force):
        """
        metodo de aplica una fuerza
        entradas y restricciones:
        Self: agente
        force: fuerza aplicada
        salidas:
        aplica la fuerza aplicada al agente
        """
        #cos cambios en la aceleración de un objeto van ligadods a su tamaño
        f = force / self.masa
        self.acc += f
        
    def apply_gravity(self,force):
        """
        metodo de aplica la gravedad
        entradas y restricciones:
        Self: agente
        force: fuerza aplicada
        salidas:
        aplica la fuerza de gravedad
        """
        self.acc += force
        
    def touch(self, a):
        """
        metodo de verifica si dos agentes se estan tocando
        entradas y restricciones:
        Self: agente
        a: agente
        salidas:
        true si estan tocando y false sino
        """
        self.damp = self.pos.distance_to(a.pos)
        radius = self.r+a.r

        if self.damp <= radius:
            return True
        else:
            return False

    def check_collisions(self,i):
        """
        metodo de verifica la colicion de dos agentes
        entradas y restricciones:
        Self: agente
        i: agente
        salidas:
        acciones aplicadas
        """
        if self.touch(i):
            self.change_velocities(i)
            self.separate(i)

    def change_velocities(self, a):
        """
        metodo de que cambia la velocidad de dos agentes en colisión
        entradas y restricciones:
        Self: agente
        a: agente
        salidas:
        nuevas velocidades
        """
        self_vel2 = ((self.masa - a.masa) / (self.masa + a.masa) * self.vel +
                     2 * a.masa / (self.masa + a.masa) * a.vel)
        new_vel2=((a.masa - self.masa) / (a.masa + self.masa) * a.vel +
                  (2 * self.masa / (a.masa + self.masa))* self.vel)
        self.vel=self_vel2
        a.vel=new_vel2

    def separate(self, a):
        """
        metodo de que cambia la posicion de dos agentes en colisión
        entradas y restricciones:
        Self: agente
        a: agente
        salidas:
        nuevas posiciones
        """
        try:
            difV = self.pos - a.pos
            difV = difV.normalize() * ((self.r + a.r)- self.pos.distance_to(a.pos))
            self.pos += difV/2
            a.pos -= difV/2

        except ValueError:
            pass


class AgentSystem:
    """
    clase del sistema de agentes quien hace las llamadas
    entradas y restricciones:
    ninguna
    salidas:
    metodos
    """
    def __init__(self, window):
        """
        metodo principal
        Entradas y restricciones: 
        window: ventana de pygame
        self: agente
        salidas:
        ninguna
        """
        self.agents = []
        self.window = window

    def draw(self):
        """
        metodo que llama para dibujar al agente
        entradas y restricciones:
        Self: agente
        salidas:
        dibuja al agente
        """
        for a in self.agents:
            a.draw()
            a.borders()

    def update(self):
        """
        metodo que llama para actualizar los agentes en pantalla
        entradas y restricciones:
        Self: agente
        salidas:
        refresco de la pantalla
        """
        for a in self.agents:
            a.update()

    def apply_force(self, force):
        """
        metodo  que llama para aplicar una fuerza
        entradas y restricciones:
        Self: agente
        force: fuerza aplicada
        salidas:
        aplica la fuerza aplicada al agente
        """
        for a in self.agents:
            a.apply_force(force)

    def apply_gravity(self, gravity):
        """
        metodo que llama para aplicar una fuerza gravitatoria
        entradas y restricciones:
        Self: agente
        gravity: fuerza de gravedad aplicada
        salidas:
        aplica la fuerza de gravedad aplicada  al agente
        """
        for a in self.agents:
            a.apply_gravity(gravity)

    def add_agent(self, x:float, y:float):
        """
        Funcion que constructora que agrega los agentes
        entradas y restricciones:
        Self: agente
        x:valor flotante de la cordenada x
        y:valor flotante de la cordenada y
        """
        nuevoAgente = Agent(self.window, x, y)
        self.agents.append(nuevoAgente)
        return nuevoAgente

    def touch_any(self, agente:Agent):
        """
        Funcion de llamada que verifica si dos agentes se estan tocando
        entradas y restricciones:
        Self: agente
        agente: agente
        salidas:
        true si estan tocando y false sino
        """
        for a in self.agents:
            if a.touch(agente):
                 return True
            else:
                return False

agentSys = AgentSystem(pygame.display.set_mode((720,480)))

def guardar():
    """
    Funcion que guarda el estado actual del programa
    Entradas y restricciones:
    ninguna
    salida
    True
    """
    with open("datos.pickle", "wb") as archivo:
        datos = agentSys.agents, p
        print(p)
        pickle.dump(datos, archivo)

    return True

def cargar():
    """
    Funcion que carga  el estado guardado del programa
    Entradas y restricciones:
    ninguna
    salida
    lo guardado
    """
    global p

    with open('datos.pickle', 'rb') as archivo:
        if getsize(archivo.name) > 0:
            datos = pickle.load(archivo)
            agentSys.agents = datos[0]
            p = datos[1]
        else:
            print("¡No hay datos a mostrar!")

    agentSys.draw()
    agentSys.update()


def main():
    """
    Funcion primcipal que carga el programa
    Entradas y restricciones:
    ninguna
    salida
    lo guardado
    """
    global agents, p
    pygame.init()
    window = pygame.display.set_mode((720,480))
    loop = True
    

    
    while loop:
        pygame.time.delay(16)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    p = not p
                if event.key == pygame.K_g:
                    guardar()

                if event.key == pygame.K_c:
                    cargar()

        if not p:
            buttons = pygame.mouse.get_pressed()
            if buttons[0]:
                x, y = pygame.mouse.get_pos()
                agentSys.agents.append(agentSys.add_agent(x, y))

            keys = pygame.key.get_pressed()
            #cambios en la gravedad
            if keys[pygame.K_UP]:
                agentSys.apply_force(Vector2(0,-200))

            if keys[pygame.K_DOWN]:
                agentSys.apply_force(Vector2(0,100))

            if keys[pygame.K_LEFT]:
                agentSys.apply_force(Vector2(-100,0))

            if keys[pygame.K_RIGHT]:
                agentSys.apply_force(Vector2(100,0))

            agentSys.apply_gravity(Vector2(0, 0.01))
            window.fill((0, 0, 0))
            h = 0

            agentSys.draw()

            h=0
            for a in agentSys.agents:
                h += 1
                for i in agentSys.agents[h:]:
                    a.check_collisions(i)
                a.update()

        pygame.display.update()
        
    pygame.quit()
    
main()
