def to_celsius(t):
    return (t - 32.0) * 5.0 / 9.0

def above_freezing(t):
    return t > 0

def below_freezing(t):
    return t < 0

def at_freezing(t):
    return t == 0

if __name__ == "__main__":
    print("I am the main program")
