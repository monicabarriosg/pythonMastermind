from colored import fore, style

class Board:
    """
    Clase para gestionar y mostrar el tablero de intentos en el juego de adivinanza de código.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia del tablero de intentos.
        """
        self.intentos = []
    
    def actualizar_tablero(self, intento, retroalimentacion):
        """
        Actualiza el tablero añadiendo un nuevo intento y su retroalimentación.
        """
        self.intentos.append((intento, retroalimentacion))

    def mostrar(self):
        """
        Muestra el estado actual del tablero, incluyendo todos los intentos realizados y su retroalimentación.
        Utiliza emojis de colores para representar los intentos.
        """
      
        color_map = {
            'R': '🔴',  # Rojo
            'G': '🟢',  # Verde
            'B': '🔵',  # Azul
            'Y': '🟡',  # Amarillo
            'O': '🟠',  # Naranja
            'P': '🟣'   # morado
        }
        
        print(f"{fore.CYAN}Tablero de Intentos:{style.RESET}")
        for intento, retroalimentacion in self.intentos:
            intento_display = ' '.join(color_map.get(c, '?') for c in intento)
            retroalimentacion_display = ' '.join(retroalimentacion)
            print(f"Intento: {intento_display} | Retroalimentación: {retroalimentacion_display}")
