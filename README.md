# Proyecto Pygame: Ejemplos y Videojuego

## Descripción

Este repositorio contiene varios ejemplos desarrollados en Python utilizando la biblioteca Pygame. Su objetivo es aprender los fundamentos de la programación de videojuegos, incluyendo ventanas gráficas, figuras, movimiento, sonido y detección de colisiones.

También incluye un pequeño videojuego llamado "Atrapa la estrella".

## Objetivos

- Conocer las funciones básicas de Pygame.
- Aprender a crear ventanas y dibujar figuras.
- Controlar objetos mediante el teclado.
- Utilizar sonidos en un programa.
- Crear un videojuego sencillo con puntuación.
- Practicar la organización de proyectos en Python y GitHub.

## Archivos del proyecto

### 1. `01_ventana.py`

Crea una ventana de 800 por 600 píxeles con fondo azul. Inicializa Pygame, establece el título de la ventana y detecta el evento de cierre.

### 2. `02_dibujos.py`

Muestra cómo dibujar figuras geométricas utilizando `pygame.draw`. Incluye un rectángulo rojo, un círculo verde, una línea azul y una elipse negra.

### 3. `03_movimiento.py`

Crea un cuadrado azul que se mueve con las flechas del teclado. Limita su movimiento para que no salga de la ventana y utiliza un reloj para controlar la velocidad de actualización.

### 4. `04_sonido.py`

Genera un tono de audio mediante código. Permite reproducirlo al presionar la barra espaciadora y demuestra el uso del mezclador de sonido de Pygame.

### 5. `05_videojuego.py`

Contiene el videojuego "Atrapa la estrella". El jugador controla un cuadrado azul y debe tocar una estrella amarilla para ganar puntos. La estrella cambia de posición cada vez que se recoge.

### 6. `requirements.txt`

Contiene la dependencia necesaria para instalar Pygame.

## Requisitos

- Python 3.10 o una versión compatible.
- Pygame.
- Teclado para controlar los programas.
- Salida de audio para probar el ejemplo de sonido.

## Instalación

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```

También puedes instalar la biblioteca directamente:

```bash
pip install pygame
```

## Cómo ejecutar los programas

Ejecuta cada archivo desde la terminal con Python. Por ejemplo:

```bash
python 01_ventana.py
```

Para probar los demás ejemplos, cambia el nombre del archivo:

```bash
python 02_dibujos.py
python 03_movimiento.py
python 04_sonido.py
python 05_videojuego.py
```

En algunos equipos puede ser necesario utilizar `python3` en lugar de `python`.

## Controles del videojuego

- Flecha izquierda: mover al jugador a la izquierda.
- Flecha derecha: mover al jugador a la derecha.
- Flecha arriba: mover al jugador hacia arriba.
- Flecha abajo: mover al jugador hacia abajo.
- Cerrar la ventana: terminar el juego.

## Funcionalidades de Pygame utilizadas

- `pygame.init()`: inicializa los módulos de Pygame.
- `pygame.display.set_mode()`: crea la ventana.
- `pygame.display.set_caption()`: establece el título.
- `pygame.draw`: dibuja figuras geométricas.
- `pygame.event.get()`: obtiene los eventos.
- `pygame.key.get_pressed()`: detecta las teclas presionadas.
- `pygame.Rect`: representa áreas rectangulares.
- `colliderect()`: detecta colisiones entre rectángulos.
- `pygame.time.Clock()`: controla la frecuencia de actualización.
- `pygame.mixer.Sound()`: permite reproducir sonidos.

## Conclusión

Este proyecto demuestra cómo utilizar las herramientas principales de Pygame para desarrollar aplicaciones gráficas y videojuegos sencillos. Los ejemplos permiten aprender progresivamente desde la creación de una ventana hasta el control de un personaje, la reproducción de sonidos y la detección de colisiones.

## Autor

Proyecto educativo realizado para practicar Python, Pygame y GitHub.
