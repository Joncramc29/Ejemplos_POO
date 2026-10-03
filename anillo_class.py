class Anillo: 
    def __init__(self, tamaño, material, color, precio):
        self.tamaño = tamaño
        self.material = material
        self.color = color
        self.precio = precio

    def objeto(self):
        print(f"El anillo {self.tamaño}, de {self.material}, {self.color}, y de {self.precio} dolar es redondo")