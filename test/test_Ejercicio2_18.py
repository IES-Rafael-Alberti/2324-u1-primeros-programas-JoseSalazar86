from src.Ejercicio2_18 import nombreCompleto

def test_nombreCompleto():

    resultado = nombreCompleto("John Doe")
    assert(resultado[0], "john doe")  
    assert(resultado[1], "JOHN DOE")  
    assert(resultado[2], "John Doe")