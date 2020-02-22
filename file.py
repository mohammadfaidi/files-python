'''
The open() function takes two parameters; filename, and mode.

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")
To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("demofile.txt", "rt")

By default the read() method returns the whole text, but you can also specify how many characters you want to return:

f = open("demofile.txt", "r")
print(f.read(5))
You can return one line by using the readline() method:




'''




#f = open("demofile.txt", "r")

#print(f.read())


'''
By looping through the lines of the file, you can read the whole file, line by line:

f = open("demofile.txt", "r")
for x in f:
  print(x)

'''

'''

f = open("demofile.txt", "r")
print(f.readline())
f.close(
'''


f=open("file.txt","w")
f.write("hello  world")
f.close()


f=open("file.txt","r")
for x in f:
    print(x)

f.close()



'''
Delete a File
To delete a file, you must import the OS module, and run its os.remove() function:

Remove the file "demofile.txt":

import os
os.remove("demofile.txt")
Check if File exist:
To avoid getting an error, you might want to check if the file exists before you try to delete it:

Example
Check if file exists, then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
'''


import os

if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("the file is not exist")


