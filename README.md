# 💣 Buscaminas en Python

Este proyecto implementa una versión del clásico juego **Buscaminas**, desarrollado en **Python** como parte de la tarea semestral del curso *Introducción a la Programación* en la **Universidad de Concepción**.

---

## 🎯 Objetivo del Juego

Descubrir todas las celdas que no contienen bombas en un tablero de `n × m` celdas, usando pistas numéricas que indican cuántas bombas hay en las celdas adyacentes. El jugador pierde si descubre una celda que contiene una bomba.

---

## 🕹️ ¿Cómo funciona?

1. El programa solicita el tamaño del tablero (`n` filas y `m` columnas).
2. Calcula automáticamente una cantidad `b` de bombas (1 ≤ b ≤ n × m / 4).
3. Ubica aleatoriamente las bombas en el tablero.
4. Muestra un tablero inicial con todas las celdas ocultas (`#`).
5. El jugador ingresa coordenadas para descubrir celdas.
6. El juego se actualiza tras cada intento, y termina cuando:
   - Se pisa una bomba: **pierde el jugador**.
   - Se descubren todas las celdas sin bombas: **gana el jugador**.

---

## 🧾 Entradas esperadas

- Tamaño del tablero: dos enteros `n` y `m` (entre 3 y 15).
- Intentos del jugador: coordenadas bidimensionales (`fila columna`) en cada turno.

El programa valida cada entrada. Si algún valor está fuera de rango, solicitará reingreso.

---

## 🖥️ Salidas del programa

- Al comenzar, el tablero aparece con `#` en todas sus celdas.
- Si el jugador descubre una bomba:
  - El tablero muestra todas las bombas con `*` y el mensaje **"¡Gana el computador!"**
- Si el jugador acierta una celda adyacente a bombas:
  - Se muestra la cantidad de bombas cercanas en esa celda.
- Si no hay bombas en celdas adyacentes:
  - La celda muestra un `0`.

---

## ▶️ Cómo ejecutar

1. Asegúrate de tener **Python 3.x** instalado.
2. Descarga o clona este repositorio.
3. Ejecuta el archivo principal (por ejemplo, `buscaminas.py`) en una terminal o Jupyter Notebook:

```bash
python buscaminas.py
