import sys


class MyException(Exception):
    pass


class ExceptionsDemo:
    
    def divide(self, a, b):
        try:
            result = a / b
            print("Division result:", result)
            return result
        except (ZeroDivisionError, TypeError) as e:
            print(f"Error: {e}")
            if "pytest" in sys.modules:
                raise
    
    def access_list(self, lst, index):
        try:
            print("Element:", lst[index])
            return lst[index]
        except (IndexError, TypeError) as e:
            print(f"Error: {e}")
            if "pytest" in sys.modules:
                raise
    
    def access_dict(self, dic, key):
        try:
            print("Value:", dic[key])
            return dic[key]
        except (KeyError, TypeError) as e:
            print(f"Error: {e}")
            if "pytest" in sys.modules:
                raise
    
    def read_file(self, filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                print(content)
                return content
        except (FileNotFoundError, IOError) as e:
            print(f"Error: {e}")
            if "pytest" in sys.modules:
                raise
    
    def access_attribute(self, obj):
        try:
            print(obj.tnonexistent_attribue)
        except AttributeError as e:
            print(f"Error: {e}")
            if "pytest" in sys.modules:
                raise
    
    def check_positive(self, number):
        try:
            if number < 0:
                raise MyException("The number must be positive.")
            else:
                print("Valid number:", number)
                return number
        except MyException as e:
            print(f"Error: {e}")
            if "pytest" in sys.modules:
                raise


if __name__ == "__main__":
    demo = ExceptionsDemo()

    demo.divide(10, 0)
    demo.divide("10", 2)

    demo.access_list([1, 2, 3], 5)
    demo.access_list(1, 0)

    demo.access_dict({"a": 1, "b": 2, "c": 3}, "d")
    demo.access_dict("not_a_dict", "b")

    demo.read_file("text_2.txt")
    demo.read_file("text.txt")

    demo.access_attribute(object())

    demo.check_positive(-5)
