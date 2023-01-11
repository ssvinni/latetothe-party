import os
input_file = open("C:\\Users\\Guest1\\Documents/LMSdata.txt", "r")

#assign the object "input_file" read function to a variable
cust_data = input_file.readlines()
print(cust_data)

#print the data in multiple line
input_file.close()
index = 1
for line in cust_data:
    fileName = "C:\\Users\\Guest1\\Documents\\customer" + str(index) + ".txt";
    index = index + 1
    print (fileName + "; " + line)
    new_file = open(fileName, "w")
    new_file.write(line)
    new_file.close()

