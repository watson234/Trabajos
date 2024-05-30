import pygame
from pygame.math import Vector2 
from math import pi
from random import uniform, randint

class Agent:
    def __init__(self, window, x, y):
        self.window = window
        self.pos = Vector2(x, y)
        self.vel = Vector2(uniform(-1, 1), uniform(-1, 1))
        self.acc= Vector2(0,0)
        self.color = (randint(128, 255), randint(0, 128), randint(128, 255))
        self.r = randint(4, 7)
        self.masa=self.r**2*pi
        
    def draw(self):
        pygame.draw.circle(self.window, self.color, self.pos, self.r)
        
    def update(self):
        self.pos += self.vel
        self.vel+=self.acc
        self.acc*=0
    def borders(self):
        if self.pos.x <= self.r or self.pos.x >= self.window.get_width() - self.r:
            self.vel.x *= -0.8
        if self.pos.y <= self.r or self.pos.y >= self.window.get_height() - self.r:
            self.vel.y *= -0.8
        self.pos.x = min(self.pos.x, self.window.get_width() - self.r)
        self.pos.x = max(self.pos.x, self.r)
        self.pos.y = min(self.pos.y, self.window.get_height() - self.r)
        self.pos.y = max(self.pos.y, self.r)
    def apply_force(self, force):
        f=force/self.masa
        self.acc+=f
def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    loop = True
    agents = []
    window.fill((0, 0, 0))
    while loop:
        pygame.time.delay(16)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            x, y = pygame.mouse.get_pos()
            agents.append(Agent(window, x, y))

        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            for a in agents:
                a.apply_force(Vector2(0, -1))
        if keys[pygame.K_DOWN]:
            for a in agents:
                a.apply_force(Vector2(0, 1))
        if keys[pygame.K_LEFT]:
            for a in agents:
                a.apply_force(Vector2(-1, 0))
        if keys[pygame.K_RIGHT]:
            for a in agents:
                a.apply_force(Vector2(1, 0))
                
        window.fill((0, 0, 0))
        for a in agents:
            a.draw()
            a.update()
            a.borders()

        pygame.display.update()
    
    pygame.quit()

main()
