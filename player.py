#clase para la logica del jugador
class Player:
    def __init__(self, name):
        self.name = name
    #funcion para adivinar el codigo proporcionado
    def adivinar_codigo(self):
        while True:
            intento = input(f"{self.name}, introduce tu adivinanza (4 caracteres, por ejemplo 'RGBY'): ").strip().upper()
            if len(intento) == 4 and intento.isalpha():
                return intento
            else:
                print("Adivinanza inválida. Debe tener 4 caracteres alfabéticos.")
                
#          🔴 🟡 🟢 🔵