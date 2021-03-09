

class Dog:
    def __init__(self, name, age):  # init will create one instance of the class. This function is called a "constructor of the class" and it is executed every time we create an object of the create class.
    self.name = name   # self is something we have to write by default in a mandatory way when we define the class in any function where we specify inside the class.
    self.age = age
    #pass   # A way to tell python not to do anything (There's nothing inside this class).

ares = Dog('ares',18) # Passing parameters to the class to create an instance of the "Dog class".

toby = Dog('toby',21)