Stack = ["-1"] * 20
TopOfStack = -1

def Push(Data):
    global TopOfStack
    if TopOfStack == 19:
        return -1
    TopOfStack += 1
    Stack[TopOfStack] = Data
    return 1

def Pop():
    global TopOfStack
    if TopOfStack == -1:
        return "-1"
    Data = Stack[TopOfStack]
    Stack[TopOfStack] = "-1"
    TopOfStack -= 1
    return Data

def ReadData(Filename):
    try:
        with open(Filename, "r") as File:
            for Line in File:
                if Push(Line.strip()) == -1:
                    print("Stack full")
    except OSError:
        print("Error reading file")

def Calculate():
    Total = float(Pop())
    while TopOfStack != -1:
        Operator = Pop()
        Number = float(Pop())
        if Operator == "+":
            Total += Number
        elif Operator == "-":
            Total -= Number
        elif Operator == "*":
            Total *= Number
        elif Operator == "/":
            Total /= Number
        elif Operator == "^":
            Total **= Number
    return Total

if __name__ == "__main__":
    Filename = input("Enter filename: ")
    ReadData(Filename)
    Total = Calculate()
    print("Final total:", Total)
