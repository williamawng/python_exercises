def add(x, y):
    """ get the sum of a number
    """
    return x + y

def sub(x, y):
    """ get the difference of a number
    """
    return x - y

def multi(x, y):
    """ get the product of a number
    """
    return x * y

def divide(x, y):
    """ get the quotient of a number
    """
    return x / y

def pow(x, y):
    """ get the power of a number
    """
    return x * y

def root(x, y):
    """ get a root of a number
    """
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
