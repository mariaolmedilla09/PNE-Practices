
# We are creating a class called "Dog" with an specific constructor, with just 2 parameters, that are called "instance attributes"---> name and age of the dog. Then I assign the parameters to the internal variables created inside the program.
class Dog:
    def __init__(self, name, age):  # init will create one instance of the class. This function is called a "constructor of the class" and it is executed every time we create an object of the create class.
        self.name = name   # self is something we have to write by default in a mandatory way when we define the class in any function where we specify inside the class.
        self.age = age
    #pass   # A way to tell python not to do anything (There's nothing inside this class).

    def sit(self):
        print('This is {}, and Im sitting down here'.format(self.name))

"""def set_name(self, name):
        if self.name = name
        print("This is {}, and I'm sitting down here".format(self.name))"""  # This function allows us change the internal parameters by "setters and getters".

"""def set_name(self, name):
        if self.name = name
        print("This is {}, and I'm sitting down here".format(self.name))"""

def rollover(self):
    pass

def sitdown(self):
    print("Yes, I will sit down")   #This method and the previous one should be one indent inner, but it launches an error.

ares = Dog('ares',10) # Passing parameters to the class to create an instance of the "Dog class".

ares.name ='trueno'
ares.age = 1
ares.set_name('toby')
print(ares.name)



ares.name = "trueno"  # Now I can access the information that is inside the object.
ares.age = 1  # I have this capability to change everything that is inside the class.

pass  # To debugg until the end of the program.