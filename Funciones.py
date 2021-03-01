# Definicion de errores
# Error 101: "Argumento fuera de rango" (fuera de rango de A-Z o a-z)
# Error 102: "Exceso de caracteres" (más de 1 caracter)
# Error 103: "Argumento invalido"
# El parametro no corresponde a un caracter o string

# Funcion que recibe como parámetro un caracter y retorna 0 si
# el caracter esta dentro del rango de A-Z o a-z, si el insertan más de
# 1 caracter, retorna un código de error asi mismo si el caracter esta
# fuera de los rangos, retorna un código de error
def check_char(char):
    if (type(char) is str):
        newChar = char.lower()  # convierte a minuscula
        if (len(newChar) == 1):  # comprueba que haya solo un caracter
            if(97 <= ord(newChar) <= 122):  # recorre el abecedario
                return 0
            else:
                return 101  # codigo de error unico
        else:
            return 102  # codigo de error unico
    else:
        return 103

# Funcion que recibe como parametro un caracter y si este se encuentra
# en un rango de A-Z o a-z retorna el caracter en minuscula
# si estaba en mayuscula o viceversa, si se inserta mas de un
# caracter o esta fuera de rango se devuelve codigos de error
def caps_switch(caracter):
    resultado = check_char(caracter)  # se llama el metodo de check_char
    if (resultado != 0):  # si no retorna 0 significa hay un error
        return resultado
    else:
        if (97 <= ord(caracter) <= 122):
            return caracter.upper()  # convierte a mayuscula
        elif (65 <= ord(caracter) <= 90):
            return caracter.lower()  # convierte a minuscula
