def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def divide(x, y):
    return x / y

def pow(x, y):
    return x * y

def root(x, y):
    return x ** (1/y)

def remn(x, y):
    """ get a remainder of a number
    """
    return x % y

def abs(z):
    """ get an absolute value of a number
    """
    if z < 0:
        z = z * -1
    return z

def cpi(z):
    """ check if a number is pi or not.
    """
    return z == 3.14
