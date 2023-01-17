"""class parentclass():
    parentvar1 = "parentvariable value"
    def parentfunction(self):
        print("This is a parentclass")

#Childclass

class childclass(parentclass):
    childvar1 = "parentvariable value"
    def childfunction(self):
        print("This is child class")

#create an object of the child class
cobj = childclass()
 
#class childclass and parent class from the object
cobj.childfunction()
cobj.parentfunction()
"""

""" #multiple Inheritance
class parent_1():
    "this is parent1 class"
    def parent1function(self):
        print("this is a message from the parent_1.parent1function")

class parent_2():
    "this is parent2 class"
    def parent2function(self):
        print("this is a message from ther parent_2.parent2function")

#inherit from both parents

class child(parent_1, parent_2):
    "this is child class inheriting from parent_1 and parent_2"
    def childfunction(self):
        print("this is from child.childfunction")

#create child object
cobj = child()

cobj.parent1function()
cobj.parent2function()
"""

#multile:vel inheritance

class grandparent():
    "this is multilevel"
    def grandparentfunction(self):
        print("this is from grandparent.grandparentfunction")

#inherit from grandparent class

class parent(grandparent):
    "this is parent class"
    def parentfunction(self):
        print("this is from parent.parentfunction")

#inherit from parent class

class child(parent):
    "this is child class"
    def childfunction(self):
        print("this is from child.childfunction")

#create child object

gcobj = child()
gcobj.grandparentfunction()
gcobj.parentfunction()
gcobj.childfunction()