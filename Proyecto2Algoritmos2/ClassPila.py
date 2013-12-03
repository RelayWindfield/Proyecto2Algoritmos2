class NodoPila(object):

    def __init__(self, valor):
        self.SetValor(valor)
        self.SetAnterior(None)

    def SetValor(self, valor):
        self.valor = valor

    def SetAnterior(self, nodo):
        self.anterior = nodo

    def GetAnterior(self):
        return self.anterior

    def GetValor(self):
        return self.valor

class Pila(object):

    def __init__(self):
        self.SetTope(None)
        
    def SetTope(self, nodo):
        self.tope = nodo

    def GetTopeNodo(self):
        return self.tope

    def Empilar(self, valor):
        auxiliar = self.tope
        self.SetTope(NodoPila(valor))
        self.tope.SetAnterior(auxiliar)
    
    def Desempilar(self):
        if self.EsVacia() == False:
            self.SetTope(self.tope.GetAnterior())
      
    def EsVacia(self):
        return self.tope == None

    def GetTopeValor(self):
        if self.EsVacia() == False:
            return self.tope.GetValor()
        else:
            return None

"""yay"""