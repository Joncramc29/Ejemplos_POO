class Ventilador:
    def __init__(self, marca, color, tamaño, forma):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño
        self.forma = forma
        
    def encender(self):
        print(f"El ventilador {self.marca}, {self.color}, {self.tamaño}, y {self.forma} esta encendido.")