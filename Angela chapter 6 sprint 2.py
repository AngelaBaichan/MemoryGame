data = [[4,6,3,6], [5,9,2,67,4], [39,9],[33,6,8],[44,2,7,9,3,7,1]]
for lists in data:
    try:
        print(lists[3])
    except IndexError:
        print("no 3rd index in data lines")
        
        
