from ClassPila import *
from ClassVehiculo import *

class Tubo(Pila):

    def __init__(self, capacidad):
        self.SetCapacidad(capacidad)
        self.SetOcupacion(0)
        super().__init__()

    def SetCapacidad(self, capacidad):
        self.capacidad = capacidad

    def GetCapacidad(self):
        return self.capacidad

    def SetOcupacion(self, ocupacion):
        self.ocupacion = ocupacion

    def GetOcupacion(self):
        return self.ocupacion

    def Estacionar(self, vehiculo):
        if self.Cabe(vehiculo) == True:
            self.Empilar(vehiculo)
            self.SetOcupacion(self.GetOcupacion() + vehiculo.GetLongitud())

    def Retirar(self):
        if not(self.GetOcupacion == 0):
            self.SetOcupacion(self.GetOcupacion() - self.GetTopeValor().GetLongitud())
            self.Desempilar()

    def Cercano(self):
        return self.GetTopeValor()

    def Cabe(self, vehiculo):
        return ( self.GetCapacidad() - self.GetOcupacion() ) >= vehiculo.GetLongitud()

    def Existe(self, atributo, valor):
        
        existe = False
        nodoAuxiliar = self.GetTopeNodo()

        while (existe == False):
            if (atributo == "longitud") and (nodoAuxiliar.GetValor().GetLongitud() == valor):
                existe = True
            elif (atributo == "placa") and (nodoAuxiliar.GetValor().GetPlaca() == valor):
                existe = True
            elif (atributo == "modelo") and (nodoAuxiliar.GetValor().GetModelo() == valor):
                existe = True
            elif (atributo == "anho") and (nodoAuxiliar.GetValor().GetAnho() == valor):
                existe = True
            elif (atributo == "color") and (nodoAuxiliar.GetValor().GetColor() == valor):
                existe = True
            
            if not(nodoAuxiliar.GetAnterior() == None) :
                nodoAuxiliar = nodoAuxiliar.GetAnterior()
            else:
                break

        return existe