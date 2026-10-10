class MyException(Exception):
    pass


class ExceptionsDemo:
    
    def divide(self, a, b):
        try:
            result = a / b
            print("Division result:", result)
            return result
        except ZeroDivisionError as e:
            print(f"Error [ZeroDivisionError]: No es posible dividir entre cero. Detalle: {e}")
        except TypeError as e:
            print(f"Error [TypeError]: Ambos operandos deben ser numéricos. Detalle: {e}")
    
    def access_list(self, lst, index):
        try:
            print("Element:", lst[index])
            return lst[index]
        except IndexError as e:
            print(f"Error [IndexError]: El índice {index} está fuera de rango. Detalle: {e}")
        except TypeError as e:
            print(f"Error [TypeError]: Tipo de dato no válido para lista o índice. Detalle: {e}")
    
    def access_dict(self, dic, key):
        try:
            print("Value:", dic[key])
            return dic[key]
        except KeyError as e:
            print(f"Error [KeyError]: La clave '{key}' no existe en el diccionario. Detalle: {e}")
        except TypeError as e:
            print(f"Error [TypeError]: El objeto proporcionado no es un diccionario válido. Detalle: {e}")
    
    def read_file(self, filename):
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
        try:
            print("Attribute value:", obj.tnonexistent_attribue)
        except AttributeError as e:
            print(f"Error [AttributeError]: El atributo 'tnonexistent_attribue' no existe en el objeto. Detalle: {e}")
    
    def check_positive(self, number):
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

    demo.divide(10, 0)
    demo.divide("10", 2)
    demo.divide(10, 2)

    demo.access_list([1, 2, 3], 5)
    demo.access_list(1, 0)
    demo.access_list([1, 2, 3], 1)

    demo.access_dict({"a": 1, "b": 2, "c": 3}, "d")
    demo.access_dict("not_a_dict", "b")
    demo.access_dict({"a": 1, "b": 2, "c": 3}, "b")

    demo.read_file("text_2.txt")
    demo.read_file("text.txt")

    demo.access_attribute(object())

    demo.check_positive(-5)
    demo.check_positive("texto")
    demo.check_positive(10)
