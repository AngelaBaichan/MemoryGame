num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))


try:
    ans = num1/num2
    print("Answer =",ans)
except ZeroDivisionError:
    print("Error: Divided by 0")
    
