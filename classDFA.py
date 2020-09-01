import networkx as nx
import matplotlib.pyplot as plt
from os import system
from colorama import init, Fore, Back, Style
import numpy as np
import json
import os

# no 2 transciones de un estado
class dfa:
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
    valid = True
    
    '''   
    Manera manual
    def definir_ejercicio(self):
        estados=0
        estadoFinal=0
        alfabeto=0
        print("\n *** A L F A B E T O ***")
        while(alfabeto != "-1"): 
            alfabeto = input("Ingrese un caracter Alfabeto (salir -1): ")
            if(alfabeto != "e"):
                if(alfabeto != "-1"):
                    self.alphabet = np.append(self.alphabet , alfabeto)
                else:
                    break
            else:
                print("\n EPSILON no esta permitodo en DFA \n")

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
        self.definir_transiciones()    
        
            
    def definir_transiciones(self):   
        opc= 0
        print("\n *** T R A N S I C I O N E S ***")
        while (opc != "-1"):
            if(opc == "-1"):
                break
            else:
                actual= input("Ingrese Estado Actual: ")
                peso= input("Ingrese peso de Transicion: ")
                if(peso != "e"): 
                    destino= input("Ingrese Estado de destino: ")           
                else:
                    print("\n EPSILON no esta permitodo en DFA \n")
                    print(peso, "\n No pertene al alfabeto \n")
                    peso= input("Ingrese peso de Transicion: ")     
                    destino= input("Ingrese Estado de destino: ")
                self.transitions = np.append(self.transitions , [[actual , peso , destino]] , axis=0)          
                opc = input("Otra transicion? (0 - si | -1 - no ): ")   
        self.transitions = np.delete(self.transitions , 0 , axis=0)
        
        tmp = self.transitions
        for entity in self.transitions:
            for x in tmp:
                if(entity[0]==x[0]  and entity[1]==x[1] and entity[2]!= x[2]):
                    self.cumple=False
                    break        
            
        if(self.cumple!=True):
            self.transitions = [[0,0,0]]  
            print("No cumple con DFA")
            self.definir_transiciones()
'''  

    def definir_ejercicioJson(self):
        dir = 'C:\\Users\\David\\Desktop\\ProyectoTeoria' 
         
        print("\n *** D F A ***")
        file_name = input("Ingrese archivo .Json: ")
        file_name=(file_name+ '.json')
        with open(os.path.join(dir, file_name), "r") as f:  
            contenido = f.read()
            jsondecoded = json.loads(contenido)
       
        for x in jsondecoded["alphabet"]:
            if(x=="e"):
                print("\n EPSILON no esta permitodo en DFA \n")
                break
            self.alphabet = np.append(self.alphabet , x) 
        
        for x in jsondecoded["states"]:
            self.states = np.append(self.states , x) 
        
        for x in jsondecoded["initial_state"]:
            self.initial_state += x 
        
        for x in jsondecoded["accepting_states"]:
            self.accepting_states = np.append(self.accepting_states , x) 
        
        for x in jsondecoded["transitions"]:
            if(x[1]=="e"):
                print("\n EPSILON no esta permitodo en DFA \n")
                self.valid=False
                break
            self.transitions = np.append(self.transitions , [x], axis = 0) 
        self.transitions = np.delete(self.transitions , 0 , axis = 0) #Eliminar los datos de la instancia [0,0,0]
              
    def evaluar(self):
        #self.definir_ejercicio() De manera manual
        #self.definir_ejercicioJson() Manera dinamica
        
        #Definicion del Automata
        print("Evaluando DFA \n")
        
        #Ingreso de la expresion a evaluar con el automata definido
        self.str_test = input("Ingrese test: ") 
        
        system("cls")
        print("\n\t*** E V A L U A N D O *** \n")
        print("TEST: ", self.str_test)
        print("Alfabeto: ",self.alphabet)
        print("Estados: " , self.states)
        print("Estado inicial: ", self.initial_state)
        print("Estado final: ", self.accepting_states)   
        print("Transiciones: \n",self.transitions )   
        
        
        current_state = self.initial_state
        trans_exists = True

        for index in range(len(self.str_test)):
            #Obtengo un caracter del str_test
            current_char = self.str_test[index]
            for x in self.transitions:
                if(x[0] == current_state and x[1] == current_char):
                    trans_exists = True
                    break
                else:
                    trans_exists = False
            next_state=""
            for x in self.transitions:
                if((x[0]==current_state) and (x[1]==current_char)):
                    next_state=x[2]
            current_state = next_state

        #If para evaluar si la transicion menciona que contiene el estado actual, esta dentro de la lista de
        #mis estados de aceptacion, de no ser lo se manda en consola el que el test que se ingreso no pertenece al L(M)
        if trans_exists and current_state in self.accepting_states:
            print(Fore.GREEN+"Pertenece a L(M) \n\n")
        else:
            print(Fore.RED+"No pertenece a L(M) \n\n")
            os._exit(0)         
    
    def graficar(self): 
        Graph = nx.MultiDiGraph()
        Graph.add_node(self.initial_state)

        for x in self.states:
            if(x != self.initial_state):
                Graph.add_node(x)

        for x in self.transitions:
            Graph.add_edge(x[0], x[2], element=x[1])
        
        nx.draw_circular(Graph , with_labels=True, node_color='blue', node_size=1500)
        plt.savefig("GrafoDFA.png", format="PNG")
        plt.show()