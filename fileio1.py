"""import os
print(os.getcwd())
"""

import os
my_dir = "C:\\pyprograms"
#change directory to the specified name in my_dir
os.chdir(my_dir)

#check if thge current directory is the one specified in variablke "my_dir"
print(os.getcwd())

print(os.listdir(my_dir))

#check if folder exists
print(os.path.exists(my_dir))