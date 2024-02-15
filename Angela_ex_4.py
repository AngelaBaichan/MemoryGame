# Class Ex 4
# result us greater
# f1 = 2**2 x - (3 * x) + 1
# f2 = 2 * x + 3 * x + 3
# where
# x = 1, 2, 3

for num in range(3):
    x = int(input("Enter the value of x"))
    f1 = 2**2 * x - (3 * x) + 1
    f2 = 2 * x + 3 * x + 3
    print(" f1 = ", f1)
    print(" f2 = ", f2)

    if f1 > f2:
        print("f1 is greater")
    else:
        print("f2 is greater than f1")
