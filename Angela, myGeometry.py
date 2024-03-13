import math
def calcAreaofCircle(radius):
    result = 0.0
    pi = math.pi
    result = pi * radius * radius
    return result
    

def calcPerimeterofCircle(radius):
    result = 0.0
    pi = math.pi
    result = 2 * pi * radius 
    return result

def main():
    area = calcAreaofCircle(12)
    perimeter = calcPerimeterofCircle(12)
    print(area)
    print(perimeter)
    
main()
