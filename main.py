from classDFA import dfa
from classNFA import nfa
from classER import er
from colorama import init, Fore, Back, Style
from os import system
from time import time

d = dfa()
n = nfa()
e = er()
#Variables temporales de opcioanes
opc = ""
opc1 = ""
opc2 = ""
opc3 = ""

#MENU
system("cls")
print(Fore.BLUE+"** M E N U  A U T O M A T A S **")
print("a. DFA")
print("b. NFA-e")
print("c. ER")
print("salir")
opc = input("Ingrese una opcion: ")
print("\n")

#DFA
if opc == "a":
    print("** D F A **")
    print("a. Evaluar")
    print("b. Graficar")

    opc1 = input("Ingrese una opcion: ") 
    print("\n")

if opc1 == "a":
    start_time = time() 
    d.definir_ejercicioJson() 
    d.evaluar()
    elapsed_time = time() - start_time
    print("Tiempo de Ejecucion: %.10f segundos." % elapsed_time)  
    d.graficar()
    
if opc1 == "b":
    d.definir_ejercicioJson() 
    d.graficar()

#NFA    
if opc == "b":
    print("** N F A - e **")
    print("a. Evaluar NFA-E to DFA")
    print("b. Graficar NFA")
    opc2 = input("Ingrese una opcion: ") 
    print("\n")
    
if opc2 == "a":
    start_time = time() 
    n.definir_ejercicioJson() 
    n.NFAtoDFA()
    n.evaluar()
    elapsed_time = time() - start_time
    print("Tiempo de Ejecucion: %.10f segundos." % elapsed_time) 
    n.graficar()
    
if opc2 == "b":
    n.definir_ejercicioJson() 
    n.graficarNFA()


#ER
if opc == "c":
    print("** Expresion Regular **")
    print("a. Evaluar")
    print("b. Graficar ER to NFA")
    opc3 = input("Ingrese una opcion: ") 
    print("\n")
    
if opc3 == "a":
    start_time = time() 
    e.ERtoNFA()
    e.NFAtoDFA()
    e.evaluar()
    elapsed_time = time() - start_time
    print("Tiempo de Ejecucion: %.10f segundos." % elapsed_time) 
    e.graficar()
    
if opc3 == "b":
    e.ERtoNFA()
    e.graficarNFA()

if opc == "salir":
    exit
