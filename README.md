
# 🕹️ example_pygame

Este repositorio contiene varios ejemplos de videojuegos simples desarrollados con [Pygame](https://www.pygame.org/), diseñados para enseñar conceptos básicos de programación en Python como listas enlazadas, sprites y demás.


### 🔹 Battle/
Contiene un prototipo de RPG por turnos dividido en dos pasos de desarrollo:

- `step1/` y `step2/`: incluyen enemigos, jugadores, sprites, y fondos.
- Archivos clave: `enemy.py`, `player.py`, `main.py`, `settings.py`.

### 🔹 LinkedList/
Implementación del juego Snake usando una lista enlazada:

- `LinkedList.py`: implementación de la lista.
- `Node.py`: definición del nodo.
- `Snake.py`: lógica del juego.

## ▶️ Cómo ejecutar

1. Instala Pygame:
   ```bash
   pip install pygame
   ```

2. Ejecuta uno de los juegos:
   - Snake:
     ```bash
     python LinkedList/main.py
     ```
   - RPG:
     ```bash
     python Battle/step1/main.py
     # o
     python Battle/step2/main.py
     ```

## ✅ Requisitos

- Python 3.x
- Pygame
