import os
#string to store the command
OScommand = "echo late to the party"

#run the os command using system function
os.system(OScommand)

import subprocess
subprocess.call(['echo', 'welcome'], shell= True)

(SDout, SDerr) = subprocess.Popen( ['C:/Users/Guest1/AppData/Local/Programs/Python/Python311/python.exe' ,'c:/Users/Guest1/Desktop/pyprograms/print1.py']
                                  ,stdout=subprocess.PIPE
                                  ,stderr=subprocess.PIPE
                                  ,shell=True).communicate()
                                  
#print SDout and SDerr variables

print(SDout.decode())
print(SDerr.decode())