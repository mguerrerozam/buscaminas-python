#ARCHIVO CREADO ÚNICAMENTE PARA PROBAR LA CLASE "BUTTON" DEFINIDA RECIENTEMENTE (FECHA 21-05)
import pygame
import sys
from src.game.utils import COLORES
from src.ui.button import Button

pygame.init()
pantalla=pygame.display.set_mode((800,600))
pygame.display.set_caption('BUTTON TESTING')
reloj=pygame.time.Clock()
fuente=pygame.font.SysFont(None, 40)
def test_boton():
    print('BOTÓN PULSADO CORRECTAMENTE')

botón=Button('TESTING', (325,225),(150,150),fuente,COLORES['NEGRO'],COLORES['BLANCO'],COLORES['GRIS'], test_boton)
ejecutando=True
while ejecutando:
    eventos=pygame.event.get()
    for evento in eventos:
        if evento.type==pygame.QUIT:
            ejecutando=False

    pantalla.fill(COLORES['BLANCO'])

    botón.actualizar(eventos)
    botón.dibujar(pantalla)

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
