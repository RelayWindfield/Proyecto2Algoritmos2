class Vehiculo(object):

    def __init__(self, longitud, placa, modelo, anho, color):
        self.SetLongitud(longitud)
        self.SetPlaca(placa)
        self.SetModelo(modelo)
        self.SetAnho(anho)
        self.SetColor(color)

    def SetLongitud(self, longitud):
        if longitud.find(",") != -1:
            auxiliar = ""
            for letra in longitud:
                if letra == ",":
                    auxiliar += "."
                else:
                    auxiliar += letra
            self.longitud = auxiliar
        else:
            self.longitud = longitud
        

    def SetPlaca(self, placa):
        self.placa = placa

    def SetModelo(self, modelo):
        self.modelo = modelo

    def SetAnho(self, anho):
        self.anho = anho

    def SetColor(self, color):
        self.color = color

    def GetLongitud(self):
        return self.longitud

    def GetPlaca(self):
        return self.placa

    def GetModelo(self):
        return self.modelo

    def GetAnho(self):
        return self.anho

    def GetColor(self):
        return self.color