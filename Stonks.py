class Stonks:
    def __init__(self,medicamento,cantidad):
        self.medicamento = medicamento
        self.cantidad = cantidad
        

    # METODOS GET
    def getMedicamento(self):
        return self.medicamento

    def getCantidad(self):
        return self.cantidad

    # METODOS SET
    def setMedicamento(self, medicamento):
        self.medicamento = medicamento

    def setCantidad(self, cantidad):
        self.cantidad = cantidad