class Seq:

    def __init__(self, strbases):
        self.strbases = strbases
        if self.is_valid_sequence():
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("Incorrect sequence detected")

    def is_valid_sequence(self):
        for b in self.strbases:
            if b != "A" and b != "C" and b != "G" and b != "T":
                return False
            return True


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

# Main program

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1:  {s1}")
print(f"Sequence 2:  {s2}")



