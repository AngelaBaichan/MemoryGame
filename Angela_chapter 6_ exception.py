try:
    file_object = open('angela_info.txt','r')
    for lines in file_object:
        print(lines)

except FileNotFoundError:
    print("use the correct path of your files")
