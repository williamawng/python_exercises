def biweekly_check(x, y):
    return (x * y) * 2

print("40 hours:", biweekly_check(40, 25))

def biweekly_check_over(x, y):
    if (x > 40):
        return ((x * y) + ((x - 40) * (y * 1.5))) * 2
    else:
        return biweekly_check(x, y)

print("60 hours:", biweekly_check_over(60, 25))

def taxes_to_government(x):
    return x * 0.07

print("TAX:", taxes_to_government(biweekly_check(40, 25)))