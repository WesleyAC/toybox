import math

# rotate point 1 about point 2 by `angle` radians
def rotate(x1, y1, x2, y2, angle):
    x1 -= x2
    y1 -= y2
    xn = x1 * math.cos(angle) - y1 * math.sin(angle)
    yn = x1 * math.sin(angle) + y1 * math.cos(angle)
    xn += x2
    yn += y2
    return (xn, yn)

def rot_point(x1, y1, x2, y2, angle):
    x, y = rotate(x1, y1, x2, y2, angle)
    print(f"PA {int(x)}, {int(y)};")

def shape(size, x, y, angle, sidelength):
    print("PU;")
    rot_point((x-(size/2)), (y+(size/2)*sidelength), x, y, angle)
    print("PD;")
    rot_point((x-(size/2)*sidelength), (y+(size/2)), x, y, angle)
    rot_point((x+(size/2)*sidelength), (y+(size/2)), x, y, angle)
    rot_point((x+(size/2)), (y+(size/2)*sidelength), x, y, angle)
    rot_point((x+(size/2)), (y-(size/2)*sidelength), x, y, angle)
    rot_point((x+(size/2)*sidelength), (y-(size/2)), x, y, angle)
    rot_point((x-(size/2)*sidelength), (y-(size/2)), x, y, angle)
    rot_point((x-(size/2)), (y-(size/2)*sidelength), x, y, angle)
    rot_point((x-(size/2)), (y+(size/2)*sidelength), x, y, angle)
    print("PU;")

def ngon(n, size, x, y, angle):
    print("PU;")
    for i in range(n+1):
        rot_point(x, y+size, x, y, angle+(math.tau*i/len(range(n))))
        print("PD;")
    print("PU;")


if __name__ == "__main__":
    print("SP1;")
    #shape(1000, 5000, 3000, 0.3*math.tau, 0.5)
    for i in range(3,12,3):
        for r in range(0,10):
            ngon(i, 3000-r*300, 10300/2, 7650/2, 0.1*r*math.tau)
