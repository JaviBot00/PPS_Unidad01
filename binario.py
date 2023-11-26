# Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que
# introduzca un número binario e imprima por pantalla el número en formato decimal.
# Para desarrollar el programa, es necesario que desarrolles una función con la
# siguiente cabecera:

# def esBinario(strbinario)
# # Devuelve True o False si la cadena de caracteres (strbinario) que se ha pasado
# como parámetro contiene una cadena binaria.

# # Ejemplo de esBinario:
# print(esBinario(“1001”))
# True

# print(esBinario(“Hola”))
# False

def esBinario(strbinario):
    # for digito in strbinario:
    #     if digito not in '01':
    #         return False
    # return True

    # return all(caracter in '01' for caracter in strbinario)
    return not any(caracter not in "01" for caracter in strbinario)

def binario_a_decimal(strbinario):
    if not esBinario(strbinario):
        return "No es un número binario válido."
    
    # decimal = 0
    # longitud = len(strbinario)
    # for i in range(longitud):
    #     bit = int(strbinario[longitud - i - 1])
    #     decimal += bit * (2 ** i)
    
    # return decimal

    numero = 0
    for i, caracter in enumerate(strbinario[::-1]):
        numero += int(caracter) * (2**i)
    return numero

# Pedir al usuario que ingrese un número binario
numero_binario = input("Introduce un número binario: ")

# Convertir el número binario ingresado a decimal
resultado = binario_a_decimal(numero_binario)
print(f"El número binario {numero_binario} en decimal es: {resultado}")
