#FUNCIÓN PARA IMPORTAR IMÁGENES MÁS CÓMODAMENTE
import pygame
import os
def cargar_imagen(nombre_archivo):
    ruta=os.path.join(os.path.dirname(__file__),assets,nombre_archivo)
    return pygame.image.load(ruta).convert_alpha()
