import pytest
# Para las pruebas de Actividad 1 (pytest.raises) se utiliza Exceptions2, que contiene
# las operaciones sin try-except para validar que las excepciones se disparen adecuadamente.
from Exceptions2 import ExceptionsDemo as RawExceptionsDemo, MyException

# Para las pruebas de Actividad 2 se importa Exceptions, verificando que los métodos
# con bloques try-except manejen los errores sin romper el flujo del programa.
from Exceptions import ExceptionsDemo as HandledExceptionsDemo

raw_demo = RawExceptionsDemo()
handled_demo = HandledExceptionsDemo()


# ==============================================================================
# ACTIVIDAD 1: Pruebas unitarias de detección de excepciones con pytest.raises
# ==============================================================================

# 1. Pruebas para división (divide)
def test_divide_zero():
    """Verifica que se lance ZeroDivisionError al dividir entre cero."""
    with pytest.raises(ZeroDivisionError):
        raw_demo.divide(10, 0)

def test_divide_type_error():
    """Verifica que se lance TypeError al pasar tipos de datos no numéricos."""
    with pytest.raises(TypeError):
        raw_demo.divide("10", 2)


# 2. Pruebas para acceso a listas (access_list)
def test_access_list_index_error():
    """Verifica que se lance IndexError cuando el índice está fuera del rango de la lista."""
    with pytest.raises(IndexError):
        raw_demo.access_list([1, 2, 3], 5)

def test_access_list_type_error():
    """Verifica que se lance TypeError cuando el parámetro no es una lista válida."""
    with pytest.raises(TypeError):
        raw_demo.access_list(1, 0)


# 3. Pruebas para acceso a diccionarios (access_dict)
def test_access_dict_key_error():
    """Verifica que se lance KeyError cuando una clave no existe en el diccionario."""
    with pytest.raises(KeyError):
        raw_demo.access_dict({"a": 1, "b": 2, "c": 3}, "d")

def test_access_dict_type_error():
    """Verifica que se lance TypeError cuando el objeto no es un diccionario válido."""
    with pytest.raises(TypeError):
        raw_demo.access_dict("not_a_dict", "b")


# 4. Pruebas para lectura de archivos (read_file)
def test_read_file_not_found():
    """Verifica que se lance FileNotFoundError al intentar abrir un archivo inexistente."""
    with pytest.raises(FileNotFoundError):
        raw_demo.read_file("text_2.txt")


# 5. Pruebas para acceso a atributos (access_attribute)
def test_access_attribute_error():
    """Verifica que se lance AttributeError al acceder a un atributo inexistente."""
    with pytest.raises(AttributeError):
        raw_demo.access_attribute(object())


# 6. Pruebas para validación de números positivos con excepción personalizada (check_positive)
def test_check_positive_my_exception():
    """Verifica que se lance MyException cuando se ingresa un número negativo."""
    with pytest.raises(MyException):
        raw_demo.check_positive(-5)


# ==============================================================================
# ACTIVIDAD 2: Verificación de manejo controlado de excepciones (Exceptions.py)
# ==============================================================================

def test_handled_exceptions_do_not_crash():
    """
    Verifica que en Exceptions.py las funciones capturan las excepciones
    internamente con try-except, permitiendo que el flujo continúe sin detenerse.
    """
    # Ninguna de estas llamadas debe propagar una excepción no controlada
    handled_demo.divide(10, 0)
    handled_demo.divide("10", 2)
    handled_demo.access_list([1, 2, 3], 5)
    handled_demo.access_list(1, 0)
    handled_demo.access_dict({"a": 1, "b": 2}, "c")
    handled_demo.access_dict("no_es_dict", "a")
    handled_demo.read_file("text_2.txt")
    handled_demo.access_attribute(object())
    handled_demo.check_positive(-5)
    handled_demo.check_positive("invalido")
