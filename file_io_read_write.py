"""import os
input_file = open("C:\\Users\\Guest1\\Documents/Data.txt", "r")

#assign the object "input_file" read function to a variable

var_text = input_file.read()

#print the data in one go

print(var_text)

#close thye file stream handler
input_file.close()
"""
"""import os
#reopen the file
input_file1 = open("C:\\Users\\Guest1\\Documents/Data.txt", "r")

#while trye enter into an infinite loop (we handle it by a break)
while True:
    curr_line = input_file1.readline() #read line by line,to variable current line
    if not curr_line:
        break  #break if there is no line to read
    print(curr_line)  #print the current line

#close the file stream holer
input_file1.close() """
"""
def even_or_odd(n1):
    if n1%2 == 0:
        print(str(n1) + "is even")
    else:
        print(str(n1) + "is odd")

import os

#reopen the file
input_file1 = open("C:\\Users\\Guest1\\Documents/Data.txt", "r")
#while trye enter into an infinite loop (we handle it by a break)
while True:
    curr_line = input_file1.readline() #read line by line,to variable current line
    if not curr_line:
        break  #break if there is no line to read
    try:
        even_or_odd(int(curr_line))  #print(curr_line)  #print the current line
    except:
        print("error: "+curr_line+" is not a number")

#close the file stream holer
input_file1.close()

import os
readlines_file = open("C:\\Users\\Guest1\\Documents/Data.txt", "r")

#prints the file xontents as a LIST
print(readlines_file.readlines())
readlines_file.close()
"""

import os

#create a file handler to create a new file in WRITE mode

#create folder if doesnt exist and ignore if exist
#try:
#    os.mkdir("C:\\Users\\Guest1\\Documents/Data.txt", "r")
#except:
#    pass

#create a file in WRITE mode
new_file = open("C:\\Users\\Guest1\\Documents/output.txt", "w")

#write to file using write method
new_file.write("welcome to python\n")
new_file.write("vinni\n")
new_file.write("153EST\n")
new_file.close()