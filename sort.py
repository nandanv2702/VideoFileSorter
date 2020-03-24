import os
import sys
import shutil

os.chdir('/')

if len(sys.argv) > 1:
    projectName = sys.argv[1]
    canon = 'Canon'
    iphone = 'iPhone'

    if os.path.exists('/Volumes/Nandan V'):
        os.chdir('Volumes/Nandan V/Project Self')
        parent_dir = os.getcwd()

        # need to change directory to Nandan V, make a new folder with the projectName and make two folders called 'iPhone' and 'Canon' in it

        print('\n')

        path = os.path.join(parent_dir, projectName)

        os.mkdir(path)

        os.mkdir(path + '/' + canon)

        os.mkdir(path + '/' + iphone)

        # change the working directory to the new folder created

        os.chdir(projectName)

        # waits for user to import all files and then sorts them

        moved = False
        while(not moved):
            value = input("Did you import your files? Y/N: ")
            if(value == "Y"):
                print(os.getcwd())

                files = os.listdir()

                for i in range(0, len(files)):
                    if files[i][:3] == "IMG":
                        shutil.move(files[i], 'Canon')
                    elif files[i][:3] == "MOV":
                        shutil.move(files[i], 'iPhone')
                    else:
                        continue
                moved = True
            else:
                print('\n')
                print("Move your files now!")
                moved = False
        print('\n')
        print("All files have been moved and sorted!")

else:
    print("projectName not specified." + '\n' + "Cannot carry out task")

print(os.getcwd())
