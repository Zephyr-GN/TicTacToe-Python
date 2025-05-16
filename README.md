# 🎮 Tic Tac Toe en Python (Jugador vs Máquina)

Un clásico juego de **Tic Tac Toe** (Tres en línea / Gato) en consola, desarrollado en Python. Enfréntate contra una IA que utiliza el algoritmo **Minimax** para tomar decisiones óptimas.

---

## 🤖 Características

- 🧠 **IA inteligente** con Minimax: difícil de vencer.
- 🕹️ Juega como `'X'` o `'O'`, seleccionado aleatoriamente.
- 📟 Interfaz en consola simple y clara.
- 🔁 Ciclo de juego completo: turno del jugador y luego de la máquina.
- 🧠 Lógica robusta para detectar ganadores y empates.

---

## 📋 Cómo funciona

- El tablero es una lista de 9 posiciones (`0-8`) representando las casillas.
- El jugador humano elige manualmente su movimiento.
- La IA analiza todas las posibilidades con **Minimax** para escoger la mejor jugada.
- El juego finaliza cuando uno gana o hay empate.

---

## 📂 Estructura del Código

- `TicTacToe`: clase principal que controla la lógica del juego y el flujo de turnos.
- `humanPLayer`: gestiona la entrada del usuario.
- `ComputerPlayer`: contiene la IA y el algoritmo Minimax.
- Métodos clave:
  - `show_board()`: muestra el tablero actual.
  - `checkWinner()`: verifica si hay ganador o empate.
  - `minimax()`: lógica recursiva para la mejor jugada posible.

---

## 📝 Requisitos

- Python 3.7 o superior
- No requiere bibliotecas externas
