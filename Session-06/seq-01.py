class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        print("New sequence created!")

    def __str__(self):  # Whatever is witten here, will be executed when I press "print".
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

class Gene(Seq):   # Child class, because the parent is declared between the parenthesis.
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    pass

# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")   # Another mechanism to pass the values and printing one object.
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")