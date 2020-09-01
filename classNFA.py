import networkx as nx
import matplotlib.pyplot as plt
from os import system
from colorama import init, Fore, Back, Style
import numpy as np
import os
import json
from listaEnlazada import ListaNoOrdenada

class nfa:
    #Variables temporales en evaluar
    alphabet = []
    states = []
    initial_state =""
    accepting_states = [] 
    transitions = [[0,0,0]]
    #Variables temporales en graficar
    str_test = ""    
    actual = ""
    destino = ""
    pesoString = ""
    #Nodos de la lista enlazada
    TablaTransiciones = ListaNoOrdenada()
    #Lista para almacenar mi DFA
    ListaE = ListaNoOrdenada()
    ListaEstadoAcep = ListaNoOrdenada() 
    ListaTransicion = ListaNoOrdenada()
    
    
    '''  
    def definir_ejercicio(self):
        estados=0
        estadoFinal=0
        alfabeto=0
        print("\n *** A L F A B E T O ***")
        while(alfabeto != "-1"): 
            alfabeto = input("Ingrese un caracter Alfabeto (salir -1): ")
            if(alfabeto != "-1"):
                self.alphabet = np.append(self.alphabet , alfabeto)
            else:
                break

        print("\n *** E S T A D O  I N I C I A L ***")
        estadoInicial = input("Ingrese estado inicial: ")
        self.initial_state = estadoInicial

        print("\n *** E S T A D O S ***")
        while(estados != "-1"): 
            estados = input("Ingrese un estado (salir -1): ")
            if(estados != "-1"):
                self.states = np.append(self.states , estados)
            else:
                break

        print("\n *** E S T A D O S  F I N A L E S ***")
        while(estadoFinal != "-1"): 
            estadoFinal = input("Ingrese los estados finales (salir -1): ")
            if(estadoFinal != "-1"):
                self.accepting_states = np.append(self.accepting_states, estadoFinal)
            else:
                break
            
        opc= 0
        print("\n *** T R A N S I C I O N E S ***")
        while (opc != "-1"):
            if(opc == "-1"):
                break
            else:
                actual= input("Ingrese Estado Actual: ")
                peso= input("Ingrese peso de Transicion: ")
                destino= input("Ingrese Estado de destino: ")
                self.transitions = np.append(self.transitions , [[actual , peso , destino]] , axis=0)                
                opc = input("Otra transicion? (0 - si | -1 - no ): ")
        
        self.transitions = np.delete(self.transitions , 0 , axis=0)
'''  
    
    def definir_ejercicioJson(self):
        dir = 'C:\\Users\\David\\Desktop\\ProyectoTeoria' 
         
        print("\n *** N F A - e ***")
        file_name = input("Ingrese archivo .Json: ")
        file_name=(file_name+ '.json')
        with open(os.path.join(dir, file_name), "r") as f:  
            contenido = f.read()
            jsondecoded = json.loads(contenido)
       
        for x in jsondecoded["alphabet"]:
            self.alphabet = np.append(self.alphabet , x) 
        
        for x in jsondecoded["states"]:
            self.states = np.append(self.states , x) 
        
        for x in jsondecoded["initial_state"]:
            self.initial_state += x 
        
        for x in jsondecoded["accepting_states"]:
            self.accepting_states = np.append(self.accepting_states , x) 
        
        for x in jsondecoded["transitions"]:
            self.transitions = np.append(self.transitions , [x], axis = 0) 
        self.transitions = np.delete(self.transitions , 0 , axis = 0) #Eliminar los datos de la instancia [0,0,0]
        
    def NFAtoDFA(self):
        self.alphabet = np.delete(self.alphabet, 0)
        cE = []
        cD = []
        cEF = []
        #SACAR CERRADURRAS 
        for al in self.alphabet:
            if(al!="e"):
                #Cerradura Epsilon
                for es in self.states: 
                    cE = np.append(cE , [es])
                    for tra in self.transitions:
                        if(es == tra[0] and tra[1] == "e"):
                            cE = np.append(cE , tra[2])
                #Transicion de la Cerradura E
                    for est in cE:
                        for trs in self.transitions:
                            if(est == trs[0] and trs[1]==al):
                                cD = np.append(cD , [trs[2]] , axis=0)
                #Cerradura E de la transicion           
                        for estad in cD: 
                            cEF = np.append(cEF , [estad])
                            for tran in self.transitions:
                                if(estad == tran[0] and tran[1] == "e"):
                                    cEF = np.append(cEF , [tran[2]])
                     
                        if(cEF!=[]):
                            if not self.ListaE.buscar(cEF):
                                self.ListaE.agregar(cEF)
                            self.TablaTransiciones.agregar([[es],[al],list(cEF)]) 
                        cEF=[]
                    cE=[]    
                    cD=[]  
            else:
                print("-") 
                
        self.ListaE.agregar([self.initial_state])
        ListaTMP = ListaNoOrdenada()
       #Agregar nuevos estados de aceptacion
        for x in self.accepting_states:
            ListaTMP = self.ListaE.buscarEF(x)
            iterador = ListaTMP.tamano()
            ListaTMP.imprimir()
            while(iterador > 0):
                tmp = ListaTMP.Sacar() 
                self.ListaEstadoAcep.agregar(tmp)
                iterador = iterador - 1
                
        #Agregar trans que encuentro en mi tabla general
        tmp = self.TablaTransiciones.tamano()
        while(tmp > 0):
            aux = self.TablaTransiciones.Sacar()
            aux2 = np.array(aux)
            if not(aux[2] == []) and not(self.ListaTransicion.buscar(aux2)):
                aux2 = np.array(aux[0])
                if self.ListaE.buscar(aux2):
                    self.ListaTransicion.agregar(aux)
            tmp = tmp - 1
        
        #Agregar trans que voy encontrando en mi nueva tabla dfa
        tmp = self.ListaTransicion.tamano()
        ListaAux = self.ListaTransicion.devoLista()
        while(tmp > 0):
            #aux con tiene el valor del nodo en ese momento de la listaTransicion 
            aux = ListaAux.Sacar()
            #aux1 con tiene el valor de aux y lo convierte a array
            aux1 = np.array(aux)
            #aux1 le doy el valor de la posicion [2] osea el destino de la listaTransicion
            aux1 = np.array(aux1[2])
            if not(self.ListaTransicion.buscarUnoElemento(0,aux1)):
        #Este es cuando el estado actual tenga un tam mayor que 1
                if (len(aux1)>1):
                    arrayTMPDestino = []
                    for e in self.alphabet:
                        if(e!="e"):
                            for x in aux1:
                                for y in self.transitions:
                                    if y[0]==x and y[1] == e:
                                        arrayTMPDestino = np.append(arrayTMPDestino, y[2])
                            auxTMP = [list(aux1),e,list(arrayTMPDestino)] 
                            self.ListaTransicion.agregar(auxTMP)
                            arrayTMPDestino = []
        #Este es cuando estadoactual sea solo de tamano 1
                else:
                    for e in self.alphabet:
                        if(e!="e"):
                            for x in self.transitions:
                                if x[0]==aux1 and x[1] == e:
                                    auxTMP = [aux1,e,x[2]] 
                                    self.ListaTransicion.agregar(auxTMP)                                        
            tmp = tmp - 1 
        system("cls")

    def evaluar(self):
        system("cls")
        print("\n\t*** E V A L U A N D O  NFA-E to DFA ***")
        print("Alfabeto: ",self.alphabet)
        print("Estados: ")
        self.ListaE.imprimir()
        print("Estado inicial: ", self.initial_state)
        print("Estado final: ")
        self.ListaEstadoAcep.imprimir()   
        print("Transiciones: ")       
        self.ListaTransicion.imprimir()

        print("Evaluando NFA-e to DFA ")
        self.str_test = input("Ingrese test: ") 
        for index in range(len(self.str_test)):
            if self.str_test[index] not in self.alphabet:
                print(Fore.RED+"No existe en el alfabeto: ", self.str_test[index])
                os._exit(0)
            
        current_state = np.array(self.initial_state)
        self.transition_exists = True

        for char_index in range(len(self.str_test)):
            current_char = self.str_test[char_index]
            #Evular si existen mis transiciones
            AuxTransicion = self.ListaTransicion.devoLista()
            tam = self.ListaTransicion.tamano() 
            while(tam > 0):
                tmp = list(AuxTransicion.Sacar())
                tmp3 = np.array(current_char)
                tmp1 = np.array(tmp[0])
                if((tmp[0] == current_state).all() and tmp[1] == tmp3):
                    self.transition_exists = True
                    break
                else:
                    self.transition_exists = False
                tam = tam - 1
            next_state=[]
            
            #Evaluo en las transciones con el caracter del test
            AuxTransicion = self.ListaTransicion.devoLista()
            tam = self.ListaTransicion.tamano() 
            while(tam > 0):
                tmp = list(AuxTransicion.Sacar())
                tmp1 = np.array(tmp[0]) 
                tmp2 = np.array(tmp[2])
                tmp3 = np.array(current_char)
                if((tmp1 == current_state).all() and (tmp[1]==tmp3)):
                    next_state=np.array(tmp2)
                    break
                tam = tam - 1
            current_state = next_state
        current_state = np.array(current_state)

        if self.ListaEstadoAcep.buscar(current_state) and self.transition_exists:
            print(Fore.GREEN+"Pertenece a L(M)")
        else:
            print(Fore.RED+"No pertenece a L(M)")
            os._exit(0)   
            
    def graficar(self):
        AuxEstados  = self.ListaE.devoLista()
        tamEstados = self.ListaE.tamano() 
        
        AuxTransicion = self.ListaTransicion.devoLista()
        tamTransiciones = self.ListaTransicion.tamano() 
        
        Graph = nx.MultiDiGraph()
        Graph.add_node(self.initial_state)
        
        while(tamEstados > 0):
            AuxEst = AuxEstados.Sacar()
            AuxEst1 = np.array(AuxEst)
            if not (AuxEst1 == [self.initial_state]).all():
                Estados = ''.join(AuxEst)
                Graph.add_node(Estados)
            tamEstados = tamEstados - 1
            
        while(tamTransiciones > 0):
            AuxTrans = AuxTransicion.Sacar()
            actual = ''.join(AuxTrans[0])
            destino =  ''.join(AuxTrans[2])
            peso = ''.join(AuxTrans[1])       
            Graph.add_edge(actual, destino, element=peso)
            tamTransiciones = tamTransiciones - 1
        
        nx.draw_circular(Graph , with_labels=True, node_color='red', node_size=2000)
        #plt.tight_layout()
        plt.savefig("GrafoNFAtoDFA.png", format="PNG")
        plt.show()        
     
    def graficarNFA(self):   
        system("cls")
        print("\n\t*** G R A F I C A N D O  NFA *** \n")
        print("Alfabeto: ",self.alphabet)
        print("Estados: " , self.states)
        print("Estado inicial: ", self.initial_state)
        print("Estado final: ", self.accepting_states)   
        print("Transiciones: \n",self.transitions )   
        
        Graph = nx.MultiDiGraph()
        Graph.add_node(self.initial_state)

        for x in self.states:
            if(x != self.initial_state):
                Graph.add_node(x)

        for x in self.transitions:
            Graph.add_edge(x[0], x[2], element=x[1])
        
        nx.draw_circular(Graph , with_labels=True,node_color='blue', node_size=1500)
        plt.savefig("GrafoNFA.png", format="PNG")
        plt.show()
     