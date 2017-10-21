data = "00000000000000000000100000000000000000000"

str2idx = {
        "111": 0,
        "110": 1,
        "101": 2,
        "100": 3,
        "011": 4,
        "010": 5,
        "001": 6,
        "000": 7
}

def step(data, rule):
    newdata = ""
    newdata += rule[str2idx["0" + data[:2]]]
    for i in range(1,len(data)-1):
        newdata += rule[str2idx[data[i-1:i+2]]]
    newdata += rule[str2idx[data[-2:] + "0"]]
    return newdata

if __name__ == "__main__":
    for _ in range(17):
        print(data)
        data = step(data, "01011010")
