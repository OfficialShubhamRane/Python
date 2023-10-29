import os

file_path = "E:\\Python\\Python\\Basics\\test.txt"

try: 
    if(os.path.exists(file_path)):
        print("path exists")
        if(os.path.isfile(file_path)):
            print("is file")
            with open(file_path) as file:
                print(file.read())
        elif(os.path.isdir(file_path)):
            print("is directory")
    else:
        print("path does not exists")
except FileNotFoundError as e:
    print(e)
    print("file not found")