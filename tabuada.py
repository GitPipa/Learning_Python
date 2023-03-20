def tabuada():
    for i in range(1000):
        x = int(input("Eu digo-te a tabuada. Queres de que número? "))
        y=-1
        print()
        for i in range(11):
            y=y+1
            print(y,"x", x, "=", y * x)

tabuada()

