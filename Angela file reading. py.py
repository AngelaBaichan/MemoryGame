file_object = open('test.txt','r')

for lines in file_object:
    each_line = lines.split('.')
    print(each_line[0])

    try:
        print(each_line[7])
    except:
        print("Specified index is invalid")



