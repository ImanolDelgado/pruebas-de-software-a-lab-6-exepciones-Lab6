def process_number(x, y):
    result = 0
    if x > 0 and y > 0:
        result = x + y
    elif x < 0 or y < 0:
        result = x - y
    else:
        result = 0
    
    if result > 10:
        result = result * 2
    else:
        result = result + 5
        
    return result