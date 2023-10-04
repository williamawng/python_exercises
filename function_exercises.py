def f_to_c(t):
    y = 3
    print(y)
    return (t - 32.0) * 5.0 / 9.0

w = f_to_c(233)
print(w)
# kilometers per liter = miles per gallon (US) × 0.425144
# mpg / 0.425144 = kpl
def mpg_to_lp100k(mpg):
    return (235.21 / mpg)
a = mpg_to_lp100k(24)
print(a)


def i_mpg_2_lp100k(mpg):
    return (282.48 / mpg)
b = i_mpg_2_lp100k(24)
print(b)


def litres_needed(dist_kilo, mpg):
    lp100k = mpg_to_lp100k(mpg)
    litres_needed = lp100k * (dist_kilo/100)
    return litres_needed
c = litres_needed(150, 30)
print(c)
d = litres_needed(100, 30)
print(d)

print(pow(2,3))