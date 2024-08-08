# mi proyecto de python 
# monica fabiola barrios gonzalez
# para iniciar el juego colocar python main.py
# en el archivo board.py esta la Clase `Board`: Para gestionar y mostrar el tablero de intentos.
**Métodos**:
   - `actualizar_tablero(intento, retroalimentacion)`: Añade un nuevo intento y su retroalimentación al tablero.
   - `mostrar()`: Muestra el estado actual del tablero utilizando emojis de colores.

# en code_creador se encuentra la clase CodeMaker: es una clase para crear y gestionar códigos secretos y adivinarlos.
**Métodos**:

   - `establecer_codigo()`: Permite al usuario establecer un código secreto.
   - `generar_codigo_aleatorio()`: Genera un código secreto aleatorio.
   - `adivinar_codigo(estrategia='aleatoria')`: Adivina el código usando una estrategia especificada.

# en el archivo gampe.py esta la Clase `Juego`: Para gestionar el juego de adivinanza de código.
**Métodos**:
   - `iniciar_juego()`: Inicia el juego, solicitando el rol del usuario y estableciendo el código secreto.
   - `verificar_ganador(intento)`: Verifica si el intento es correcto y actualiza el tablero.
   - `dar_retroalimentacion(intento)`: Proporciona retroalimentación sobre el intento en comparación con el código secreto.
   - `Retorna:`
            `list` Una lista de caracteres que representan la retroalimentación para cada posición en el intento.
                  Los caracteres pueden ser:
                  - `✓` en verde si el carácter está en la posición correcta.
                  - `✗` en amarillo si el carácter está en el código pero en una posición incorrecta.
                  - `×` en rojo si el carácter no está en el código secreto.
# en archivo player.py esta la Clase `Player`: Para gestionar la lógica del jugador.
**Métodos**:
   - `adivinar_codigo()`: Permite al jugador introducir una adivinanza válida para el código secreto.




