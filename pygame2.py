import pygame
from pygame.math import Vector2
from random import uniform,randint

class  Agent:
    def __init__(self,window,x,y):
        self.window=window
        self.pos=Vector2(x, y)
        self.vel=Vector2(uniform(-2,2),uniform(-2,2))
        self.color=(randint(0,255),randint(0,255),randint(0,255))
        self.r=randint(3,15)
    def draw(self):
        pygame.draw.circle(self.window, self.color, self.pos,self.r)

    def update(self):
        self.pos += self.vel

    def borders(self):
        if self.pos.x <= self.r+0 or self.pos.x>=self.window.get_width()-self.r:
            self.vel.x*=-1
            self.color=(randint(0,255),randint(0,255),randint(0,255))
            self.r=randint(3,15)
        if self.pos.y <= self.r+0 or self.pos.y>=self.window.get_height()-self.r:
            self.vel.y*=-1
            self.color=(randint(0,255),randint(0,255),randint(0,255))
            self.r=randint(3,15)
            
        self.pos.x=min(self.pos.x, self.window.get_width()-self.r)
        self.pos.x=max(self.pos.x, self.r)
        self.pos.y=min(self.pos.y, self.window.get_height()-self.r)
        self.pos.y=max(self.pos.y, self.r)
def main():
    pygame.init()
    window=pygame.display.set_mode((720,480))
    loop=True
    agents=[]
    
    while loop:
        pygame.time.delay(16)
        window.fill((0,0,0))
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                loop=False
            if e.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                agents.append(Agent(window,x,y))
        for a in agents:
            a.draw()
            a.borders()
            a.update()
        
        pygame.display.update()
    pygame.quit()

main()
