from pathlib import Path
import termcolor

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        if strbases == "NULL":
            print("NULL seq created")
            self.strbases = strbases
        else:
            self.strbases = strbases
            if self.is_valid_sequence():
                print("New sequence created!")
            else:
                self.strbases = "ERROR"
                print("Incorrect sequence detected")

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = "Sequence" + str(i) + ": (Length 3)" + str(list_sequences[i])
            termcolor.cprint(text, 'yellow')

    def __str__(self):  # Whatever is witten here, will be executed when I press "print".
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

def generate_seqs(pattern, number):   # Created inside the module, but outside the class
    # A,3
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern))
    return list_seq



