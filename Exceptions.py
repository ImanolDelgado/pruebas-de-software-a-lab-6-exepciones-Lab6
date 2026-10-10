class MyException(Exception):
    """Excepción personalizada para reglas de negocio del usuario."""
    pass


class ExceptionsDemo:
    
    def divide(self, a, b):
        """Realiza la división entre dos números capturando ZeroDivisionError y TypeError."""
        try:
            result = a / b
            print("Division result:", result)
            return result
        except ZeroDivisionError as e:
            print(f"Error [ZeroDivisionError]: No es posible dividir entre cero. Detalle: {e}")
        except TypeError as e:
            print(f"Error [TypeError]: Ambos operandos deben ser numéricos. Detalle: {e}")
    
    def access_list(self, lst, index):
        """Accede a un elemento de la lista capturando IndexError y TypeError."""
        try:
            print("Element:", lst[index])
            return lst[index]
        except IndexError as e:
            print(f"Error [IndexError]: El índice {index} está fuera de rango. Detalle: {e}")
        except TypeError as e:
            print(f"Error [TypeError]: Tipo de dato no válido para lista o índice. Detalle: {e}")
    
    def access_dict(self, dic, key):
        """Accede al valor de una clave en un diccionario capturando KeyError y TypeError."""
        try:
            print("Value:", dic[key])
            return dic[key]
        except KeyError as e:
            print(f"Error [KeyError]: La clave '{key}' no existe en el diccionario. Detalle: {e}")
        except TypeError as e:
            print(f"Error [TypeError]: El objeto proporcionado no es un diccionario válido. Detalle: {e}")
    
    def read_file(self, filename):
        """Lee el contenido de un archivo capturando FileNotFoundError e IOError."""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
                print("File content:", content.strip())
                return content
        except FileNotFoundError as e:
            print(f"Error [FileNotFoundError]: El archivo '{filename}' no fue encontrado. Detalle: {e}")
        except IOError as e:
            print(f"Error [IOError]: Ocurrió un error al leer el archivo '{filename}'. Detalle: {e}")
    
    def access_attribute(self, obj):
        """Intenta acceder a un atributo inexistente capturando AttributeError."""
        try:
            print("Attribute value:", obj.tnonexistent_attribue)
        except AttributeError as e:
            print(f"Error [AttributeError]: El atributo 'tnonexistent_attribue' no existe en el objeto. Detalle: {e}")
    
    def check_positive(self, number):
        """Valida que un número sea positivo lanzando y capturando MyException y TypeError."""
        try:
            if not isinstance(number, (int, float)):
                raise TypeError("El valor proporcionado debe ser un número entero o flotante.")
            if number < 0:
                raise MyException("The number must be positive.")
            else:
                print("Valid number:", number)
                return number
        except MyException as e:
            print(f"Error [MyException]: Excepción personalizada capturada: {e}")
        except TypeError as e:
            print(f"Error [TypeError]: Error de tipo en validación: {e}")


if __name__ == "__main__":
    demo = ExceptionsDemo()

    print("==================================================")
    print("DEMOSTRACIÓN DE MANEJO DE EXCEPCIONES CONTROLADAS")
    print("==================================================")

    print("\n--- 1. Pruebas de División (divide) ---")
    demo.divide(10, 0)      # Provoca ZeroDivisionError
    demo.divide("10", 2)    # Provoca TypeError
    demo.divide(10, 2)      # Caso válido

    print("\n--- 2. Pruebas de Acceso a Listas (access_list) ---")
    demo.access_list([1, 2, 3], 5)   # Provoca IndexError
    demo.access_list(1, 0)          # Provoca TypeError
    demo.access_list([1, 2, 3], 1)   # Caso válido

    print("\n--- 3. Pruebas de Acceso a Diccionarios (access_dict) ---")
    demo.access_dict({"a": 1, "b": 2, "c": 3}, "d")  # Provoca KeyError
    demo.access_dict("not_a_dict", "b")              # Provoca TypeError
    demo.access_dict({"a": 1, "b": 2, "c": 3}, "b")  # Caso válido

    print("\n--- 4. Pruebas de Lectura de Archivos (read_file) ---")
    demo.read_file("text_2.txt")  # Provoca FileNotFoundError
    demo.read_file("text.txt")    # Caso válido (archivo existente)

    print("\n--- 5. Pruebas de Acceso a Atributos (access_attribute) ---")
    demo.access_attribute(object())  # Provoca AttributeError

    print("\n--- 6. Pruebas de Validación de Número Positivo (check_positive) ---")
    demo.check_positive(-5)          # Provoca MyException
    demo.check_positive("texto")     # Provoca TypeError
    demo.check_positive(10)          # Caso válido

    print("\n==================================================")
    print("¡El flujo del programa finalizó exitosamente sin detenerse!")
    print("==================================================")
