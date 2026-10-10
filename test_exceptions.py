import pytest
from Exceptions2 import ExceptionsDemo, MyException

demo = ExceptionsDemo()

@pytest.mark.divide
def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        demo.divide(10, 0)

@pytest.mark.divide
def test_divide_type_error():
    with pytest.raises(TypeError):
        demo.divide("10", 2)

@pytest.mark.access_list
def test_access_list_index_error():
    with pytest.raises(IndexError):
        demo.access_list([1, 2, 3], 5)

@pytest.mark.access_list
def test_access_list_type_error():
    with pytest.raises(TypeError):
        demo.access_list(1, 0)

@pytest.mark.access_dict
def test_access_dict_key_error():
    with pytest.raises(KeyError):
        demo.access_dict({"a": 1, "b": 2, "c": 3}, "d")

@pytest.mark.access_dict
def test_access_dict_type_error():
    with pytest.raises(TypeError):
        demo.access_dict("not_a_dict", "b")

@pytest.mark.read_file
def test_read_file_not_found():
    with pytest.raises(FileNotFoundError):
        demo.read_file("text_2.txt")

@pytest.mark.access_attribute
def test_access_attribute_error():
    with pytest.raises(AttributeError):
        demo.access_attribute(object())

@pytest.mark.check_positive
def test_check_positive_my_exception():
    with pytest.raises(MyException):
        demo.check_positive(-5)
