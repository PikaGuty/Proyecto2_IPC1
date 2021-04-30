class Receta:
    def __init__(self,padecimiento):
        self.padecimiento = padecimiento
        

    # METODOS GET
    def getPadecimiento(self):
        return self.padecimiento

    # METODOS SET
    def setPadecimiento(self, padecimiento):
        self.padecimiento = padecimiento