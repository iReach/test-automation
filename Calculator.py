
def add(a: int, b: int):
    """
    adds two numbers and returns the result. 
    :int a: number 1
    :int b: number 2
    """
    if type(a) != int or type(b) != int:
        raise TypeError("add only handles integers")
    return a+b

def mult(a: int, b: int):
    """
    multiplicates two numbers and returns the result. 
    :int a: number 1
    :int b: number 2
    """
    if type(a) != int or type(b) != int:
        raise TypeError("mult only handles integers")
    return a*b

def subtract(a: int,b: int):
    """
    subtracks the two numbers and returns the result. 
    :int a: number 1
    :int b: number 2
    """
    if type(a) != int or type(b) != int:
        raise TypeError("subtrack only handles integers")
    return a-b