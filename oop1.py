class python:
    'This is python training class'

    #class variables/attributes
    #a class variable
    ti_var = 100
    #a class list
    ti_list = ["a", "b", "c"]
    #a class tuple
    ti_tuple = ("x","y","z")
    # a class dictionary
    ti_dictionary = {"1":"a", "2":"b", "3":"c"}

    #class function
    def ti_function(self):
        "This is a class function"
        print("This is a message from Python class ti_function")

a= python()
print(a.__doc__)
print(a.ti_list)
a.ti_list.append(-999)
print(a.ti_list)
a.ti_function()

b= python()
b.ti_list.append(-999)
print(b.ti_list)
b.ti_function()
