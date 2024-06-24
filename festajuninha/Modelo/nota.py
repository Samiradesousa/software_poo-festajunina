class Nota:
    
    # Método construtor
    def __init__(self, elegancia, desenvoltura, simpatia, item):
        self.elegancia = elegancia
        self.desenvoltura = desenvoltura
        self.simpatia = simpatia
        self.item = item

    # Método para retornar uma representação em string da nota
    def __str__(self):
        return f"Elegância: {self.elegancia}, Desenvoltura: {self.desenvoltura}, Simpatia: {self.simpatia}, Item: {self.item}"

    # Método para calcular a média das notas
    def media(self):
        return (self.elegancia + self.desenvoltura + self.simpatia + self.item) / 4
    