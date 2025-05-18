#LÓGICA DEL TABLERO DE JUEGO
import pygame
import random
from cell import Celda
from utils import FILAS, COLS, NUM_MINAS, ANCHO, ALTO, MARGEN_SUPERIOR, COLORES

class Tablero:
    def __init__(self):
        # Inicializar el tablero con celdas
        self.celdas = [[Celda(fila, col) for col in range(COLS)] for fila in range(FILAS)]
        self.primer_click = True
        self.juego_terminado = False
        self.victoria = False
        self.minas_marcadas = 0
        self.tiempo_inicio = 0
        self.tiempo_actual = 0
        # Cargar fuentes
        self.fuente = pygame.font.SysFont('Arial', 20)
        self.fuente_grande = pygame.font.SysFont('Arial', 40)
        # Rectángulo para el botón de reinicio
        self.boton_reinicio = pygame.Rect(ANCHO // 2 - 30, 30, 60, 40)
    
    def reiniciar_juego(self):
        """Reinicia todos los parámetros del juego"""
        self.celdas = [[Celda(fila, col) for col in range(COLS)] for fila in range(FILAS)]
        self.primer_click = True
        self.juego_terminado = False
        self.victoria = False
        self.minas_marcadas = 0
        self.tiempo_inicio = pygame.time.get_ticks()
        self.tiempo_actual = 0
    
    def colocar_minas(self, fila_inicial, col_inicial):
        """Coloca minas aleatoriamente evitando la primera celda clickeada"""
        minas_colocadas = 0
        while minas_colocadas < NUM_MINAS:
            fila = random.randint(0, FILAS - 1)
            col = random.randint(0, COLS - 1)
            
            # Evitar colocar en la primera celda clickeada o alrededor
            if (abs(fila - fila_inicial) <= 1 and abs(col - col_inicial) <= 1) or self.celdas[fila][col].es_mina:
                continue
                
            self.celdas[fila][col].es_mina = True
            minas_colocadas += 1
        
        # Calcular minas cercanas para cada celda
        for fila in range(FILAS):
            for col in range(COLS):
                if not self.celdas[fila][col].es_mina:
                    # Contar minas adyacentes
                    for df in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if df == 0 and dc == 0:
                                continue
                            
                            f, c = fila + df, col + dc
                            if 0 <= f < FILAS and 0 <= c < COLS and self.celdas[f][c].es_mina:
                                self.celdas[fila][col].minas_cercanas += 1
    
    def descubrir_celda(self, fila, col):
        """Descubre una celda y maneja la lógica de cascada"""
        # Si es el primer click, colocar minas
        if self.primer_click:
            self.colocar_minas(fila, col)
            self.primer_click = False
            self.tiempo_inicio = pygame.time.get_ticks()
        
        # Si la celda ya está descubierta o marcada, no hacer nada
        if not (0 <= fila < FILAS and 0 <= col < COLS) or self.celdas[fila][col].descubierta or self.celdas[fila][col].marcada:
            return
        
        # Descubrir la celda actual
        self.celdas[fila][col].descubierta = True
        
        # Si es una mina, terminar el juego
        if self.celdas[fila][col].es_mina:
            self.juego_terminado = True
            # Descubrir todas las minas
            self._mostrar_todas_minas()
            return
        
        # Si no hay minas cercanas, descubrir celdas adyacentes (flood fill)
        if self.celdas[fila][col].minas_cercanas == 0:
            for df in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if df == 0 and dc == 0:
                        continue
                    self.descubrir_celda(fila + df, col + dc)
    
    def _mostrar_todas_minas(self):
        """Muestra todas las minas al perder el juego"""
        for fila in range(FILAS):
            for col in range(COLS):
                if self.celdas[fila][col].es_mina:
                    self.celdas[fila][col].descubierta = True
    
    def marcar_celda(self, fila, col):
        """Marca o desmarca una celda como potencial mina"""
        # Si la celda ya está descubierta, no hacer nada
        if self.celdas[fila][col].descubierta:
            return
        
        # Alternar la marca
        self.celdas[fila][col].marcada = not self.celdas[fila][col].marcada
        
        # Actualizar contador de minas marcadas
        if self.celdas[fila][col].marcada:
            self.minas_marcadas += 1
        else:
            self.minas_marcadas -= 1
    
    def verificar_victoria(self):
        """Verifica si se ha ganado el juego"""
        # Verificar si todas las celdas que no son minas están descubiertas
        for fila in range(FILAS):
            for col in range(COLS):
                if not self.celdas[fila][col].es_mina and not self.celdas[fila][col].descubierta:
                    return False
        
        self.victoria = True
        self.juego_terminado = True
        return True
    
    def actualizar_tiempo(self):
        """Actualiza el contador de tiempo"""
        if not self.juego_terminado and not self.primer_click:
            self.tiempo_actual = (pygame.time.get_ticks() - self.tiempo_inicio) // 1000
    
    def manejar_click(self, x, y, boton):
        """Maneja los clicks del ratón en el tablero"""
        # Verificar si se hace clic en el botón de reinicio
        if self.boton_reinicio.collidepoint(x, y):
            self.reiniciar_juego()
            return
        
        # Si el juego ha terminado, reiniciar con cualquier clic
        if self.juego_terminado:
            self.reiniciar_juego()
            return
        
        # Convertir coordenadas de pantalla a índices de celda
        fila = (y - MARGEN_SUPERIOR) // (ALTO - MARGEN_SUPERIOR) * FILAS
        col = x // ANCHO * COLS
        
        # Verificar límites del tablero
        if 0 <= fila < FILAS and 0 <= col < COLS:
            if boton == 1:  # Clic izquierdo
                self.descubrir_celda(fila, col)
                self.verificar_victoria()
            elif boton == 3:  # Clic derecho
                self.marcar_celda(fila, col)
    
    def dibujar(self, pantalla):
        """Dibuja todo el tablero y la interfaz"""
        # Dibujar fondo del panel superior
        pygame.draw.rect(pantalla, COLORES['GRIS_OSCURO'], (0, 0, ANCHO, MARGEN_SUPERIOR))
        
        # Dibujar contador de minas
        minas_restantes = NUM_MINAS - self.minas_marcadas
        texto_minas = self.fuente.render(f"Minas: {minas_restantes}", True, COLORES['BLANCO'])
        pantalla.blit(texto_minas, (20, 30))
        
        # Dibujar cronómetro
        texto_tiempo = self.fuente.render(f"Tiempo: {self.tiempo_actual}", True, COLORES['BLANCO'])
        pantalla.blit(texto_tiempo, (ANCHO - 120, 30))
        
        # Dibujar botón de reinicio
        pygame.draw.rect(pantalla, COLORES['GRIS'], self.boton_reinicio)
        texto_reinicio = self.fuente.render("Reset", True, COLORES['NEGRO'])
        pantalla.blit(texto_reinicio, (ANCHO // 2 - 20, 40))
        
        # Dibujar celdas
        for fila in range(FILAS):
            for col in range(COLS):
                self.celdas[fila][col].dibujar(pantalla, self.fuente)
        
        # Si el juego ha terminado, mostrar mensaje
        if self.juego_terminado:
            s = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            s.fill((0, 0, 0, 128))  # Fondo semitransparente
            pantalla.blit(s, (0, 0))
            
            if self.victoria:
                texto = self.fuente_grande.render("¡VICTORIA!", True, COLORES['VERDE'])
            else:
                texto = self.fuente_grande.render("GAME OVER", True, COLORES['ROJO'])
                
            pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))
            
            texto_reiniciar = self.fuente.render("Haz clic para reiniciar", True, COLORES['BLANCO'])
            pantalla.blit(texto_reiniciar, (ANCHO // 2 - texto_reiniciar.get_width() // 2, ALTO // 2 + 50))