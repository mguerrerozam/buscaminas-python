#CÓDIGO DEL MENÚ PRINCIPAL
import pygame
import os 
from game.utils import ALTO, ANCHO, COLORES 

pygame.init()
pantalla=pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('Menú Principal')
fps=pygame.time.Clock()

