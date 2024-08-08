import random
from itertools import product

class CodeMaker:
    def __init__(self):
        self.code = None
    def establecer_codigo(self):
        while True:
            codigo = input("Introduce el código secreto (4 caracteres, por ejemplo 'RGBY'): ").strip().upper()
            if len(codigo) == 4 and codigo.isalpha():
                self.code = codigo
                break
            else:
                print("Código inválido debe tener 4 caracteres alfabéticos.")

    def generar_codigo_aleatorio(self):
        colores = ['R', 'G', 'B', 'Y', 'O', 'P']
        self.code = ''.join(random.choice(colores) for _ in range(4))
        print(f"El código secreto generado es: {self.code}")
        return self.code

    def adivinar_codigo(self, estrategia='aleatoria'):
        """
        Adivina el código usando la estrategia especificada
        """
        colores = ['R', 'G', 'B', 'Y', 'O', 'P']
        
        if estrategia == 'aleatoria':
            return ''.join(random.choice(colores) for _ in range(4))
        
        elif estrategia == 'fuerza_bruta':
            posibles_combinaciones = [''.join(p) for p in product(colores, repeat=4)]
            return posibles_combinaciones.pop(0)  
        
        else:
            raise ValueError("Estrategia no válida debe ser 'aleatoria', 'fuerza_bruta'.")
