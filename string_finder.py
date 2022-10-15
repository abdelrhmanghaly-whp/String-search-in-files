import os
text = input("Enter Your Text :")
path = input("required path :")
# os.chdir(path)
def readf(path):
    f = 0 # intial f 0
    os.chdir(path) # director of the txt
    files = os.listdir()
    # print(files) - msh m7tagnha "u can use it 3ady"
    for file_name in files:
        # txt
        required_path = os.path.abspath(file_name)
        if os.path.isdir(required_path):
            readf(required_path)
        if os.path.isfile(required_path):
            f = open(file_name, "r")
            if text in f.read():
                #intial flag
                f = 1
                print(text + " was found in")
                final_path = os.path.abspath(file_name)
                print(final_path) # last return
                return True
    # flag approach to 1, not found 
    if f == 1:
        print(text + " is not found")
        return False
readf(path) # shows strings in files "sp folder"
