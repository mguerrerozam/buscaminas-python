#PUNTO DE ENTRADA DE LA APLICACIÓN, INICIALIZACIÓN Y BUCLE PRINCIPAL
import pygame
import sys
from pygame.locals import *
from board import Tablero
from utils import ANCHO, ALTO, COLORES

def main():
    # Inicialización de pygame
    pygame.init()
    
    # Configuración de la pantalla
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Buscaminas')
    reloj = pygame.time.Clock()
    
    # Crear el tablero
    tablero = Tablero()
    
    # Bucle principal del juego
    ejecutando = True
    while ejecutando:
        pantalla.fill(COLORES['BLANCO'])
        
        # Manejar eventos
        for evento in pygame.event.get():
            if evento.type == QUIT:
                ejecutando = False
            
            elif evento.type == MOUSEBUTTONDOWN:
                # Obtener posición del clic
                x, y = pygame.mouse.get_pos()
                # Manejar el clic según el botón presionado
                tablero.manejar_click(x, y, evento.button)
        
        # Actualizar el tiempo
        tablero.actualizar_tiempo()
        
        # Dibujar el tablero
        tablero.dibujar(pantalla)
        
        # Actualizar la pantalla
        pygame.display.update()
        reloj.tick(30)
    
    # Salir del juego
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()