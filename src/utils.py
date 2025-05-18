#FUNCIONES DE UTILIDAD Y CONSTANTES
# Constantes del juego

# Dimensiones de la ventana
ANCHO = 400
ALTO = 500
TAMANO_CELDA = 30
FILAS = 10
COLS = 10
NUM_MINAS = 15
MARGEN_SUPERIOR = 100  # Espacio para mostrar contadores

# Colores
COLORES = {
    'BLANCO': (255, 255, 255),
    'GRIS': (192, 192, 192),
    'GRIS_OSCURO': (128, 128, 128),
    'NEGRO': (0, 0, 0),
    'AZUL': (0, 0, 255),
    'VERDE': (0, 128, 0),
    'ROJO': (255, 0, 0),
    'MORADO': (128, 0, 128),
    'MARRON': (128, 64, 0),
}

def obtener_indices_celda(pos_x, pos_y):
    """
    Convierte una posición en píxeles a índices de celda en el tablero
    
    Args:
        pos_x: Posición x en píxeles
        pos_y: Posición y en píxeles
        
    Returns:
        tuple: (fila, columna) o (None, None) si está fuera del tablero
    """
    # Verificar si está en el área del tablero
    if pos_y < MARGEN_SUPERIOR:
        return None, None
        
    fila = (pos_y - MARGEN_SUPERIOR) // TAMANO_CELDA
    col = pos_x // TAMANO_CELDA
    
    # Verificar límites
    if 0 <= fila < FILAS and 0 <= col < COLS:
        return fila, col
    else:
        return None, None

def dentro_del_tablero(fila, col):
    """
    Verifica si unos índices de fila/columna están dentro del tablero
    
    Args:
        fila: Índice de fila
        col: Índice de columna
        
    Returns:
        bool: True si está dentro del tablero, False en caso contrario
    """
    return 0 <= fila < FILAS and 0 <= col < COLS