#LÓGICA DE CADA CASILLA INDIVIDUAL
import pygame

# Importamos constantes desde utils.py
from utils import TAMANO_CELDA, MARGEN_SUPERIOR, COLORES

class Celda:
    def __init__(self, fila, col):
        self.fila = fila
        self.col = col
        self.es_mina = False
        self.descubierta = False
        self.marcada = False
        self.minas_cercanas = 0
        self.rect = pygame.Rect(col * TAMANO_CELDA, 
                               fila * TAMANO_CELDA + MARGEN_SUPERIOR, 
                               TAMANO_CELDA, TAMANO_CELDA)

    def dibujar(self, pantalla, fuente):
        """Dibuja la celda en su estado actual"""
        if self.descubierta:
            # Celda descubierta
            pygame.draw.rect(pantalla, COLORES['GRIS_OSCURO'], self.rect)
            pygame.draw.rect(pantalla, COLORES['NEGRO'], self.rect, 1)
            
            if self.es_mina:
                # Dibujar mina
                pygame.draw.circle(pantalla, COLORES['NEGRO'], self.rect.center, TAMANO_CELDA // 3)
            elif self.minas_cercanas > 0:
                # Dibujar número
                colores_numeros = [COLORES['AZUL'], COLORES['VERDE'], COLORES['ROJO'], 
                                  COLORES['MORADO'], COLORES['MARRON'], COLORES['NEGRO'], 
                                  COLORES['GRIS'], COLORES['NEGRO']]
                color = colores_numeros[min(self.minas_cercanas - 1, len(colores_numeros) - 1)]
                texto = fuente.render(str(self.minas_cercanas), True, color)
                pos_texto = texto.get_rect(center=self.rect.center)
                pantalla.blit(texto, pos_texto)
        else:
            # Celda sin descubrir
            pygame.draw.rect(pantalla, COLORES['GRIS'], self.rect)
            pygame.draw.rect(pantalla, COLORES['NEGRO'], self.rect, 1)
            
            if self.marcada:
                # Dibujar bandera
                pygame.draw.polygon(pantalla, COLORES['ROJO'], [
                    (self.rect.centerx - 10, self.rect.centery + 7),
                    (self.rect.centerx - 10, self.rect.centery - 7),
                    (self.rect.centerx + 5, self.rect.centery)
                ])
                pygame.draw.line(pantalla, COLORES['NEGRO'], 
                                (self.rect.centerx - 10, self.rect.centery + 7),
                                (self.rect.centerx - 10, self.rect.centery + 10), 2)
    
    def contiene_punto(self, x, y):
        """Verifica si un punto (x,y) está dentro de esta celda"""
        return self.rect.collidepoint(x, y)