# VideoFileSorter

This project saves the need to manually sort your file and create/rename new folders for each 

Open the sort.py file from your terminal along with one argument - this will be the name of the folder you make; this only works if your hard drive is connected - I've hard coded it for my hard drive, but this can be modified to work for any hard drive by using os.listdir() and looking for the last element in the 'Volumes' directory. 

Inside the newly created folder in the hard drive, the script will create two folders - one for 'Canon' and one for 'iPhone'; this is so that videos shot with your iPhone are moved to one folder, and ones shot with the camera are moved to another. 

-- can also modify script to sort drone footage 

A prompt shows up on the terminal asking you to confirm that you've moved all your raw footage into the new folder. Once done, it'll sort your files into respective folders for you.
