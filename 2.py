size = int(input("введи: "))
for i in range(8):
    for k in range(8):
        if (i + k) % 2 == 0:
            print("_" * size, end="")
        else:
            print("#" * size, end="")
    print()