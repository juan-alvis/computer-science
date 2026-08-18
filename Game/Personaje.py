import pygame
import constantes
class Personaje():
    def __init__(self,x,y):
        self.shape =pygame.Rect(0,0,constantes.width_personaje,constantes.height_personaje)
        self .shape.center = (x,y)

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, constantes.color_personaje, self.shape)
    
    def movimiento(self, delta_x, delta_y):
        self.shape.x=self.shape.x + delta_x
        self.shape.y=self.shape.y + delta_y