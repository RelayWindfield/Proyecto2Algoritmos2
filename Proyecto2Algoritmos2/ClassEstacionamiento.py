from ClassCola import *
from ClassTubo import *
from ClassVehiculo import *
from random import *

class Evento(object):

    Estacionamiento = ""
    Nombre = ""

    def __init__(self, args):
        self.SetArgs(args)
        self.SetResultado()

    def SetArgs(self, args):
        self.args = args.split()

    def GetArgs(self):
        return self.args

    def SetResultado(self, traza = ""):
        if traza == "":
            self.resultado = traza
        else:
            self.resultado = self.resultado + traza

    def GetResultado(self):
        return self.resultado

    def Procesar(self):
        if self.GetArgs()[0] == "C":
            self.EscribirArgumentos()
            Evento.Estacionamiento = Estacionamiento()
            self.SetResultado("--> Se Crea estacionamiento " + self.GetArgs()[1][0:-4] + "\n")
            Evento.Nombre = self.GetArgs()[1][0:-10]
            return self.GetResultado()
        elif self.GetArgs()[0] == "P":
            self.EscribirArgumentos()
            self.SetResultado("--> Entra Vehiculo " + self.GetArgs()[1] + " de longitud " + self.GetArgs()[2] + "\n")
            if Evento.Estacionamiento.GetPrimero() == None:
                self.SetResultado("--> No existe Tubo disponible\n")
                Evento.Estacionamiento.Generar()
                self.SetResultado("--> Se crea Tubo " + str(Evento.Estacionamiento.GetUltimoValor().GetEtiqueta()) + 
                                  " de capacidad " + str(Evento.Estacionamiento.GetUltimoValor().GetCapacidad()) + 
                                  " y ocupacion " + str(Evento.Estacionamiento.GetUltimoValor().GetOcupacion()) + "\n")
                self.SetResultado("--> Se coloca Tubo " + str(Evento.Estacionamiento.GetUltimoValor().GetEtiqueta()) + 
                                  " de ultimo en la cola de tubos de " + Evento.Nombre + "\n")
                self.SetResultado("--> Se corren los tubos hasta que Tubo " + str(Evento.Estacionamiento.GetUltimoValor().GetEtiqueta()) + 
                                    " es el Primero\n")
            if Evento.Estacionamiento.GetPrimeroValor().Cabe(Vehiculo(self.GetArgs()[2],self.GetArgs()[1],self.GetArgs()[3],self.GetArgs()[4],self.GetArgs()[5])) == False:
                self.SetResultado("--> Capacidad de Tubo " + str(Evento.Estacionamiento.GetPrimeroValor().GetEtiqueta()) + " Excedida\n")
                Evento.Estacionamiento.Generar()
                self.SetResultado("--> Se crea Tubo " + str(Evento.Estacionamiento.GetUltimoValor().GetEtiqueta()) + 
                                  " de capacidad " + str(Evento.Estacionamiento.GetUltimoValor().GetCapacidad()) + 
                                  " y ocupacion " + str(Evento.Estacionamiento.GetUltimoValor().GetOcupacion()) + "\n")
                self.SetResultado("--> Se coloca Tubo " + str(Evento.Estacionamiento.GetUltimoValor().GetEtiqueta()) + 
                                  " de ultimo en la cola de tubos de " + Evento.Nombre + "\n")
                Evento.Estacionamiento.Estacionar(Vehiculo(self.GetArgs()[2],self.GetArgs()[1],self.GetArgs()[3],self.GetArgs()[4],self.GetArgs()[5]))
                self.SetResultado("--> Se corren los tubos hasta que Tubo " + str(Evento.Estacionamiento.GetPrimeroValor().GetEtiqueta()) + 
                                    " es el Primero\n")
                self.SetResultado("--> Se estaciona Vehiculo " + Evento.Estacionamiento.GetPrimeroValor().GetTopeValor().GetPlaca() +
                                      " en Tubo " + str(Evento.Estacionamiento.GetPrimeroValor().GetEtiqueta()) + " (ocupacion " +
                                      str(Evento.Estacionamiento.GetPrimeroValor().GetOcupacion()) + ")\n\n")
            else:
                Evento.Estacionamiento.Estacionar(Vehiculo(self.GetArgs()[2],self.GetArgs()[1],self.GetArgs()[3],self.GetArgs()[4],self.GetArgs()[5]))
                self.SetResultado("--> Se estaciona Vehiculo " + Evento.Estacionamiento.GetPrimeroValor().GetTopeValor().GetPlaca() +
                                      " en Tubo " + str(Evento.Estacionamiento.GetPrimeroValor().GetEtiqueta()) + " (ocupacion " +
                                      str(Evento.Estacionamiento.GetPrimeroValor().GetOcupacion()) + ")\n\n")
            return self.GetResultado()
        elif self.GetArgs()[0] == "B":
            if Evento.Estacionamiento.GetPrimero() != None:
                self.EscribirArgumentos()
                self.SetResultado("--> Vehiculos de " + self.GetArgs()[1] + " " + self.GetArgs()[2] + "\n")
                for iteracion in range(Evento.Estacionamiento.GetPrimeroValor().GetEtiquetaT()+1):
                    if Evento.Estacionamiento.GetPrimeroValor().Existe(self.GetArgs()[1], self.GetArgs()[2]) == True:
                        self.auxiliarnodo = Evento.Estacionamiento.GetPrimeroValor().GetTopeNodo()
                        while self.auxiliarnodo.GetAnterior() != None:
                            if (self.GetArgs()[1] == "Longitud"):
                                if self.auxiliarnodo.GetValor().GetLongitud() == self.GetArgs()[2]:
                                    self.SetResultado("--> ... " + str(Evento.Estacionamiento.GetPrimeroValor().GetEtiquetaT()) + " " + 
                                                      self.auxiliarnodo.GetValor().GetPlaca() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetLongitud() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetModelo() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetAnho() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetColor() + "\n")
                            elif (self.GetArgs()[1] == "Placa"):
                                if self.auxiliarnodo.GetValor().GetPlaca() == self.GetArgs()[2]:
                                    self.SetResultado("--> ... " + str(Evento.Estacionamiento.GetPrimeroValor().GetEtiquetaT()) + " " + 
                                                      self.auxiliarnodo.GetValor().GetPlaca() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetLongitud() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetModelo() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetAnho() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetColor() + "\n")
                            elif (self.GetArgs()[1] == "Modelo"):
                                if self.auxiliarnodo.GetValor().GetModelo() == self.GetArgs()[2]:
                                    self.SetResultado("--> ... " + str(Evento.Estacionamiento.GetPrimeroValor().GetEtiquetaT()) + " " + 
                                                      self.auxiliarnodo.GetValor().GetPlaca() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetLongitud() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetModelo() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetAnho() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetColor() + "\n")
                            elif (self.GetArgs()[1] == "Anyo"):
                                if self.auxiliarnodo.GetValor().GetAnho() == self.GetArgs()[2]:
                                    self.SetResultado("--> ... " + str(Evento.Estacionamiento.GetPrimeroValor().GetEtiquetaT()) + " " + 
                                                      self.auxiliarnodo.GetValor().GetPlaca() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetLongitud() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetModelo() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetAnho() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetColor() + "\n")
                            elif (self.GetArgs()[1] == "Color"):
                                if self.auxiliarnodo.GetValor().GetColor() == self.GetArgs()[2]:
                                    self.SetResultado("--> ... " + str(Evento.Estacionamiento.GetPrimeroValor().GetEtiquetaT()) + " " + 
                                                      self.auxiliarnodo.GetValor().GetPlaca() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetLongitud() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetModelo() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetAnho() + "\t" +
                                                      self.auxiliarnodo.GetValor().GetColor() + "\n")
                            self.auxiliarnodo = self.auxiliarnodo.GetAnterior()
                    Evento.Estacionamiento.Encolar((Evento.Estacionamiento.GetPrimeroValor))
                    Evento.Estacionamiento.Desencolar()
                return self.GetResultado()
        else:
            return ""
    
    def EscribirArgumentos(self):
        for indice in range(len(self.GetArgs())):
            if indice < (len(self.GetArgs()) - 1):
                self.SetResultado(self.GetArgs()[indice] + "\t")
            else:
                self.SetResultado(self.GetArgs()[indice] + "\n")

class Estacionamiento(Cola):
    
    EtiquetaE = -1

    def __init__(self):
        self.SetEtiqueta()
        seed(0.101101)
        super().__init__()

    def SetEtiqueta(self):
        Estacionamiento.EtiquetaE += 1
        self.etiqueta = Estacionamiento.EtiquetaE

    def GetEtiqueta(self):
        return self.etiqueta

    def Estacionar(self, vehiculo):
        if self.GetPrimeroValor().Cabe(vehiculo) == True:
            self.GetPrimeroValor().Estacionar(vehiculo)
        else:
            while self.GetPrimeroValor().GetOcupacion() != 0:
                self.Encolar(self.GetPrimeroValor())
                self.Desencolar()
            if self.GetPrimeroValor().Cabe(vehiculo) == True:
                self.GetPrimeroValor().Estacionar(vehiculo)

    def Retirar(self, placa, ticket):
        if self.Existe(placa, ticket) == True:
            while self.GetPrimeroValor().GetEtiqueta() != ticket:
                self.Encolar(self.GetPrimeroValor())
                self.Desencolar()
            TuboAuxiliar = Tubo(self.GetPrimeroValor().GetCapacidad(),self.GetPrimeroValor().GetEtiqueta())
            while self.GetPrimeroValor().GetOcupacion() > 0:
                if self.GetPrimeroValor().GetTopeValor().GetPlaca() != placa:
                    TuboAuxiliar.Estacionar(self.GetPrimeroValor().GetTopeValor())
                    self.GetPrimeroValor().Desempilar()
                else:
                    VehiculoAuxliar = self.GetPrimeroValor().GetTopeValor()
                    self.GetPrimeroValor().Desempilar()
            self.Destruir()
            self.Encolar(TuboAuxiliar)
            return VehiculoAuxiliar

    def Existe(self, placa, ticket):
        if self.GetPrimero() != None:
            for ciclo in range(self.GetPrimeroValor().GetEtiquetaT()):
                if self.GetPrimeroValor().GetEtiqueta() == ticket:
                    return self.GetPrimeroValor().Existe("placa", placa)
                self.Encolar(self.GetPrimeroValor())
                self.Desencolar()
        return False

    def Generar(self):
        self.Encolar(Tubo(randint(5, 25)))

    def Destruir(self):
        self.Desencolar()

    @staticmethod
    def ProcesarLlegadas(nombreArchivo):
        with open(nombreArchivo,"r") as instrucciones:
            for linea in instrucciones:
                if len(linea.split()) > 0:
                    if linea.split()[0] == "C":
                        MalvadaTrazaDeInserteLenguajeSoez = open(linea.split()[1], "a")
                    EventoActual = Evento(linea)
                    MalvadaTrazaDeInserteLenguajeSoez.write(EventoActual.Procesar())
                    if linea.split()[0] == "K":
                        MalvadaTrazaDeInserteLenguajeSoez.close()
                else:
                    MalvadaTrazaDeInserteLenguajeSoez.write("\n")

Estacionamiento.ProcesarLlegadas("Tolon_Andromeda.txt")