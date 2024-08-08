from colored import fore, style
from board import Board
from code_creator import CodeMaker
from player import Player
import random

class Juego:
    """
     esta clase es para gestionar el juego de adivinanza de código.
    """
    def __init__(self):
        """
        Inicializa una nueva instancia del juego.
        """
        self.codemaker = CodeMaker()
        self.jugador = Player("Jugador 1")
        self.tablero = Board()
        self.codigo_secreto = None
        self.intentos = 0
        self.max_intentos = 12
    
    def iniciar_juego(self):
        """
        esta funcion inicia el juego, solicitando al usuario su rol y estableciendo el código secreto.
        """
        print("Bienvenido al juego")
        rol = input("¿Quieres ser el creador del código o el adivinador? (C/A): ").strip().upper()
        
        if rol == "C":
            self.codemaker.establecer_codigo()
            self.codigo_secreto = self.codemaker.code
            print("Código secreto ha sido establecido.")
        elif rol == 'A':
            self.codemaker.generar_codigo_aleatorio()
            self.codigo_secreto = self.codemaker.code
            print("Código secreto generado aleatoriamente.")
        else:
            print("Rol inválido. Terminando el juego.")
            
            return
        
        while self.intentos < self.max_intentos:
            if rol == 'A':
                # Aquí el jugador adivina el código
                intento = self.jugador.adivinar_codigo()
            else:
                # La computadora adivina el código
                estrategia = random.choice(['aleatoria', 'fuerza_bruta'])
                intento = self.codemaker.adivinar_codigo(estrategia)
            
            if self.verificar_ganador(intento):
                break
        else:
            print(f"{fore.RED}¡Juego terminado! Has agotado todos los intentos.{style.RESET}")
            print(f"{fore.RED}El código secreto era: {self.codigo_secreto}{style.RESET}")


    def verificar_ganador(self, intento):
        """
        Verifica si el intento del jugador es correcto y actualiza el tablero 
        en consecuencia de la respuesta de la validacion.
        """
        if intento == self.codigo_secreto:
            self.tablero.actualizar_tablero(intento, ['✓']*4)
            print(f"{fore.GREEN}¡Felicidades! Has adivinado el código.{style.RESET}")
            return True
        else:
            self.intentos += 1
            retroalimentacion = self.dar_retroalimentacion(intento)
            self.tablero.actualizar_tablero(intento, retroalimentacion)
            self.tablero.mostrar()
            if self.intentos >= self.max_intentos:
                print(f"{fore.RED}¡Juego terminado! Has agotado todos los intentos.{style.RESET}")
                print(f"{fore.RED}El código secreto era: {self.codigo_secreto}{style.RESET}")
                return True
            else:
                print(f"{fore.YELLOW}Intento fallido. Te quedan {self.max_intentos - self.intentos} intentos.{style.RESET}")
                return False

    def dar_retroalimentacion(self, intento):
        """
        esta funcion proporciona retroalimentación sobre el intento del jugador comparado con el código secreto.
        """
        retroalimentacion = []
        for i in range(len(intento)):
            if intento[i] == self.codigo_secreto[i]:
                retroalimentacion.append(f"{fore.GREEN}✓{style.RESET}")
            elif intento[i] in self.codigo_secreto:
                retroalimentacion.append(f"{fore.YELLOW}✗{style.RESET}")
            else:
                retroalimentacion.append(f"{fore.RED}×{style.RESET}")
        return retroalimentacion
