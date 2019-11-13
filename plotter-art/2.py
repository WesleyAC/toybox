import random
from math import sin, cos, tau

def point(x, y):
    print(f"PA {int(y)},{int(x)};")

if __name__ == "__main__":
    random.seed(69)
    max_x = 7650
    max_y = 10600
    print("VS8;PA0,0;SP1;")
    for x in range(150, max_x-150, 150):
        print("PU;")
        for i, y in enumerate(range(0, max_y - random.randint(x/2,1000+x), 17)):
            point(
                x +
                sin(
                    (x+cos(y/max_y*tau*(y/max_y*2))*5000) / max_y * tau * 5
                )*100 +
                sin(y/max_y*tau*300)*(sin((x+y)/(max_x+max_y)*tau)*7),
                y + sin(x/max_x*tau*0.3)*25
            )
            if i == 0:
                print("PD;")
    print("SP0;")
