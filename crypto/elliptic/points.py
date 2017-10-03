a = -7
b = 10

p = 19

for x in range(0,p):
    for y in range(0,p):
        if (y**2) % p == (x**3 + a*x + b) % p:
            print("({}, {})".format(x, y))
