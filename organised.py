import os
import shutil

# Please type in your username
from_dir="C:/Users/USERNAME/Downloads/"
to_dir="C:/Users/USERNAME/Downloads/Documents"
listOfFiles=os.listdir(from_dir)

for filename in listOfFiles:
    name, extension = os.path.splitext(filename)
    #print(name)
    #print(extension)
    if extension == "":
        continue
    if extension in [".txt", ".doc", ".docx", ".pdf"’]:
        path1 = from_dir + "/" + filename
        path2 = to_dir + "/" + "Image files!"
        path3 = to_dir + "/" + "Image files!" + "/" + filename
        if os.path.exists(path2):
            print("Moving " + filename + "...")
            print("Please bear with us!")
            print()
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving  " + filename + "...")
            print("Please bear with us!")
            print()
            shutil.move(path1,path3)
