from ClassPila import *
from ClassVehiculo import *

class Tubo(Pila):

    EtiquetaT = -1

    def __init__(self, capacidad, etiqueta = None):
        self.SetCapacidad(capacidad)
        self.SetOcupacion(0)
        self.SetEtiqueta(etiqueta)
        super().__init__()

    def SetCapacidad(self, capacidad):
        self.capacidad = capacidad

    def GetCapacidad(self):
        return self.capacidad

    def SetOcupacion(self, ocupacion):
        self.ocupacion = ocupacion

    def GetOcupacion(self):
        return self.ocupacion

    def SetEtiqueta(self, valor = None):
        if valor == None:
            Tubo.EtiquetaT += 1
            self.etiqueta = Tubo.EtiquetaT
        else:
            self.etiqueta = valor

    def GetEtiqueta(self):
        return self.etiqueta

    def GetEtiquetaT(self):
        return Tubo.EtiquetaT

    def Estacionar(self, vehiculo):
        if self.Cabe(vehiculo) == True:
            self.Empilar(vehiculo)
            self.SetOcupacion(self.GetOcupacion() + float(vehiculo.GetLongitud()))

    def Retirar(self):
        if not(self.GetOcupacion == 0):
            self.SetOcupacion(self.GetOcupacion() - float(self.GetTopeValor().GetLongitud()))
            self.Desempilar()

    def Cercano(self):
        return self.GetTopeValor()

    def Cabe(self, vehiculo):
        return ( self.GetCapacidad() - self.GetOcupacion() ) >= float(vehiculo.GetLongitud())

    def Existe(self, atributo, valor):
        
        existe = False
        nodoAuxiliar = self.GetTopeNodo()

        while (existe == False):
            if (atributo == "Longitud") and (nodoAuxiliar.GetValor().GetLongitud() == valor):
                existe = True
            elif (atributo == "Placa") and (nodoAuxiliar.GetValor().GetPlaca() == valor):
                existe = True
            elif (atributo == "Modelo") and (nodoAuxiliar.GetValor().GetModelo() == valor):
                existe = True
            elif (atributo == "Anho") and (nodoAuxiliar.GetValor().GetAnho() == valor):
                existe = True
            elif (atributo == "Color") and (nodoAuxiliar.GetValor().GetColor() == valor):
                existe = True
            
            if nodoAuxiliar.GetAnterior() != None:
                nodoAuxiliar = nodoAuxiliar.GetAnterior()
            else:
                break

        return existe