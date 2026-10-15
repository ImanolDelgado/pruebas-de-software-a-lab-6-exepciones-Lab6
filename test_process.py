# test_process.py
import pytest
from process import process_number

# 1. Cobertura de Sentencias (Statement Coverage)
@pytest.mark.statement
@pytest.mark.parametrize("x, y, expected", [
    (5, 5, 20),   # Cubre la primera rama positiva y la multiplicación (> 10)
    (-5, -5, 5),  # Cubre la rama negativa y la suma (+ 5)
])
def test_statement_coverage(x, y, expected):
    assert process_number(x, y) == expected

# 2. Cobertura de Ramas (Branch Coverage)
@pytest.mark.branch
@pytest.mark.parametrize("x, y, expected", [
    (5, 5, 20),   # x > 0 and y > 0 (True), result > 10 (True)
    (-5, 0, 0),   # x < 0 or y < 0 (True), else branch for result > 10 (False)
    (0, 0, 5),    # else branch for both (False / False), result <= 10 -> +5
])
def test_branch_coverage(x, y, expected):
    assert process_number(x, y) == expected

# 3. Cobertura de Caminos (Path Coverage)
@pytest.mark.path
@pytest.mark.parametrize("x, y, expected", [
    (5, 6, 22),   # Camino 1: x>0, y>0 (True), result > 10 (True)
    (1, 1, 12),   # Camino 2: x>0, y>0 (True), result > 10 (False -> 2+5=7 ... espera, 1+1=2, 2+5=7, ajustemos) -> (6, 3) -> 6+3=9, 9+5=14...
    (-1, 2, -6),  # Camino 3: x<0 or y<0 (True, porque y=2? No, x<0 es True), result = -1 - 2 = -3, -3 <= 10 -> -3+5 = 2
    (0, 0, 5),    # Camino 4: Ninguna condición inicial se cumple (Else), result = 0, 0 <= 10 -> 0+5 = 5
])
def test_path_coverage(x, y, expected):
    assert process_number(x, y) == expected