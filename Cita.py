class Cita:
    def __init__(self,usuarioP,fecha,hora,motivo,estado,doc,nom):
        self.usuarioP = usuarioP
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo 
        self.estado = estado
        self.doc = doc
        self.nom = nom

    # METODOS GET
    def getUsuarioP(self):
        return self.usuarioP

    def getFecha(self):
        return self.fecha
    
    def getHora(self):
        return self.hora
    
    def getMotivo(self):
        return self.motivo

    def getEstado(self):
        return self.estado

    def getDoc(self):
        return self.doc

    def getNom(self):
        return self.nom

    # METODOS SET
    def setUsuarioP(self, usuarioP):
        self.usuarioP = usuarioP

    def setFecha(self, fecha):
        self.fecha = fecha
    
    def setHora(self, hora):
        self.hora = hora
    
    def setMotivo(self,motivo):
        self.motivo = motivo

    def setEstado(self,estado):
        self.estado = estado

    def setDoc(self,doc):
        self.doc = doc
    
    def setNom(self,nom):
        self.nom = nom