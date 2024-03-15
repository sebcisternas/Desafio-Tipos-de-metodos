# Desafio-Tipos-de-metodos


Desafio **Gran Fantasía**, un juego de rol simple desarrollado en **Python 3.8**.

## **Descripción del Desafío:**

En **Gran Fantasía**, el jugador puede a travez de la consola crear su propio personaje y enfrentarse contra poderosos orcos. Cada personaje comienza en el nivel 1 con 0 puntos de experiencia y puede subir de nivel ganando experiencia en las batallas,dependiendo de la probabilidad de esta misma.

## **Solución Implementada:**

- **`personaje.py`**: Define la clase `CrearPersonaje`, que permite crear y gestionar personajes. Contiene métodos para consultar y modificar el estado del personaje, calcular la probabilidad de ganar en una batalla y mostrar diálogos de enfrentamiento.

- **`juego.py`**: Utiliza la clase `CrearPersonaje` para ejecutar el juego. Solicita al jugador ingresar su nombre, crea un personaje, genera un orco y simula las batallas. Además, muestra el estado actual de los personajes y maneja las opciones de juego del usuario.


