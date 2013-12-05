class Evento(object):
    
    def __init__(self, codigo, *args):
        if codigo == "C":
            self.SetCodigo(codigo)
            print(args[0])

    
    def SetCodigo(self, codigo):
        self.codigo = codigo

#   def SetNombre(self

evento1 = Evento("C", 2, 5, 6, "3462", "ABC", 90)