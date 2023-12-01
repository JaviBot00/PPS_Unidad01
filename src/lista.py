# Realiza, utilizando Python 3, el ejercicio 3 de la página 35 del libro “Introducción a
# Python” de Jon Vadillo e inclúyelo en un fichero llamado lista.py. Las funciones que
# debes usar en el ejercicio 3 deben utilizar OBLIGATORIAMENTE las siguientes
# cabeceras:

# def estaEnRango(valor, minimo, maximo)
# # Devuelve True o False determinando que valor se encuentra entre el mínimo y el
# máximo.

# def estaEnLista(valor, lista)
# # Devuelve True o False determinando si el valor está en la lista.

### EJERCICIO 3 ###
# Crea un programa que reciba un número del 1 al 20 introducido por el usuario y compruebe si está
# dentro de la siguiente lista: [6,14,11,3,2,1,15,19]. Implementa una función que se asegure que el
# número introducido por el usuario está en el rango indicado y otra que compruebe si está dentro
# de la lista. Trata de crear las funciones de forma que puedan ser reutilizadas lo máximo posible en
# otros programas.

__min = 1
__max = 20
__lista = [6, 14, 11, 3, 2, 1, 15, 19]

def estaEnRango(valor, minimo, maximo):
    return minimo <= valor <= maximo

def estaEnLista(valor, lista):
    return valor in lista

def comprobarNumero():
    numero_usuario = int(input(f"Introduce un número del {__min} al {__max}: "))
    
    if estaEnRango(numero_usuario, __min, __max):
        print(f"El número está dentro del rango del {__min} al {__max}.")
    else:
        print(f"El número está fuera del rango del {__min} al {__max}.")

    if not estaEnLista(numero_usuario, __lista):
        print(f"El número {numero_usuario} está en la lista.")
    else:
        print(f"El número {numero_usuario} no está en la lista.")

if __name__ == "__main__":
    comprobarNumero()