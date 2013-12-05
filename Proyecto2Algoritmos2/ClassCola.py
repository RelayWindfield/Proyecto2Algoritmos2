class NodoCola(Object):

    def __init__(self, valor):
        self.SetValor(valor)
        self.SetSiguiente(None)
        self.SetAnterior(None)

    def SetSiguente(self, nodo):
        self.siguiente = nodo

    def SetValor(self, valor):
        self.valor = valor

    def GetSiguiente(self):
        return self.siguiente

    def GetValor(self):
        return self.valor

class Cola(Object):

    def __init__(self):
        self.SetPrimero(None)
        self.SetUltimo(None)

    def SetPrimero(self, nodo):
        self.primero = nodo

    def SetUltimo(self, nodo):
        self.ultimo = nodo

    def GetPrimero(self):
        return self.primero

    def GetUltimo(self):
        return self.ultimo

    def GetPrimeroValor(self):
        return self.primero.GetValor()

    def GetUltimoValor(self):
        return self.ultimo.GetValor()

    def Encolar(self, valor):

        aux = NodoCola(valor)

        if self.GetPrimero() == None:
            self.SetPrimero(aux)
            self.SetUltimo(aux)
        elif self.GetPrimero() != None:
            self.GetUltimo().SetSiguente(aux)
            self.SetUltimo(aux)

    def Desencolar(self):
        if self.GetPrimero() != None:
            self.SetPrimero(Self.GetPrimero().GetSiguiente())

    def Primero(self):
        return self.GetPrimeroValor()

    def vacia(self):
        return self.GetPrimero() != None


            





