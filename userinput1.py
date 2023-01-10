import sys;
"""
l_UserInput = input("enter text and press enter:")
print("text entered " + l_UserInput)

cust_name = input("enter customer name:")
cust_cs = input("customer credit score:")
cust_loan_amt = input("customer loan amount:")

#multi line input

l_userinput = ""
terminate_str = ":END"

print("enter multiline user input, please enter the string ':END'")
print("to terminate reading input")

#while true:
while 1==1:
    data = input()
    if data.strip() == terminate_str:
        break
    l_userinput= l_userinput + "\n" + data
    print(l_userinput)
"""

commandline_args_list = sys.argv
print(commandline_args_list)
#cust_name = commandline_args_list(1)
#cust_cs = commandline_args_list(2)
#cust_loan_amt = commandline_args_list(3)
