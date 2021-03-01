# Importa los metodos del archivo Funciones
from Funciones import check_char
from Funciones import caps_switch


# Funcion de prueba unitaria para metodo check_char
def test_check_char(char1, expect):
    actual = check_char(char1)
    assert actual == expect


# Funcion de prueba unitaria para metodo caps_switch
def test_caps_switch(char1, expect):
    actual = caps_switch(char1)
    assert actual == expect


# Funcion que realiza pruebas unitarias para todos los casos
# de exito de check_char
def check_char_pruebasCorrect():
    # Prueba unitaria para check_char con todas las minúsculas
    for i in range(97, 123):
        char = chr(i)
        test_check_char(char, 0)

    # Prueba unitaria para check_char con todas las mayúsculas
    for i in range(65, 91):
        char = chr(i)
        test_check_char(char, 0)


# Funcion que realiza las pruebas unitarias para todos los casos
# de exito de caps_switch
def caps_switch_pruebasCorrect():
    # Prueba unitaria para caps_switch con todas las minúsculas
    for i in range(97, 123):
        char = chr(i)
        test_caps_switch(char, char.upper())

    # Prueba unitaria para caps_switch con todas las mayúsculas
    for i in range(65, 91):
        char = chr(i)
        test_caps_switch(char, char.lower())


# Funcion que hace una prueba unitaria a check_char para comprobar el codigo
# de error al insertar mas de un caracter
def check_char_pruebaExceso():
    test_check_char("ab", 102)


# Funcion que hace 2 pruebas unitarias a check_char para comprobar el codigo
# de error al insertar caracteres fuera de los rangos A-Z o a-z
def check_char_pruebaRango():
    test_check_char("3", 101)
    test_check_char("23",  102)


# Funcion que hace 3 pruebas unitaria a check_char para comprobar el codigo
# de error al insertar caracteres datos que no corresponde
# a caracteres o strings
def check_char_pruebaInvalid():
    test_check_char(34, 103)
    test_check_char(23.54, 103)
    test_check_char([1, 2, 3], 103)


# Funcion que llama las 3 pruebas de errores del metodo check_char
def check_char_pruebaErrores():
    check_char_pruebaExceso()
    check_char_pruebaRango()
    check_char_pruebaInvalid()


# Main para llamar a todas las funciones de pruebas
check_char_pruebasCorrect()
caps_switch_pruebasCorrect()
check_char_pruebaErrores()
