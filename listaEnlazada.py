from classNodo import Nodo

class ListaNoOrdenada:

    def __init__(self):
        self.cabeza = None
        
    def estaVacia(self):
        return self.cabeza == None
    
    def agregar(self,item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
        
    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()

        return contador
    
    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if ((actual.obtenerDato() == item).all()):
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()

        return encontrado
    
    def buscarAux(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if (list(actual.obtenerDato()) == list(item)):
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()

        return encontrado
    
    def imprimir(self):
        actual = self.cabeza
        while (actual!= None):
            print(actual.obtenerDato())
            actual = actual.obtenerSiguiente()    
    
    def remover(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())
            
    def buscarEF(self,item):
        actual = self.cabeza
        Lista = ListaNoOrdenada()
        EFtmp = [] 
        while actual != None:
            EFtmp = actual.obtenerDato()
            for x in EFtmp:
                if (x == item):
                    Lista.agregar(actual.obtenerDato())
                    break
            actual = actual.obtenerSiguiente()
        return Lista
    
    def Sacar(self):
        if self.cabeza == None:
            return None
        actual = self.cabeza
        self.cabeza = actual.obtenerSiguiente()
        return actual.obtenerDato()
    
    def devoLista(self):
        actual = self.cabeza
        ListaAux = ListaNoOrdenada()
        while (actual != None):
            ListaAux.agregar(actual.obtenerDato())
            actual = actual.obtenerSiguiente()
        return ListaAux
    
    def buscarUnoElemento(self,pos,val):
        actual = self.cabeza
        encontrado = False
        while (actual != None and not encontrado):
            aux = actual.obtenerDato()
            if (aux[pos] == val).all():
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
        return encontrado
    
    def buscarUnoElementoAux(self,pos,val):
        actual = self.cabeza
        encontrado = False
        while (actual != None and not encontrado):
            aux = actual.obtenerDato()
            if (list(aux[pos]) == list(val)):
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
        return encontrado
    