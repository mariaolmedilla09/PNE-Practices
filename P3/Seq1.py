#import termcolor
from pathlib import Path

class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = "NULL" # CONSTANT (UPPER CASE): its value is never going to change. They can be used directly in the function definition, but inside the function we have to make reference to the class form which we obtain this constant. They help us save time if they change.
    INVALID_SEQUENCE = "ERROR"
    def __init__(self, strbases=NULL_SEQUENCE):
        if strbases == Seq.NULL_SEQUENCE:
            print("NULL seq created")
            self.strbases = strbases
        else:
            self.strbases = strbases
            if self.is_valid_sequence():
                print("New sequence created!")
            else:
                self.strbases = Seq.INVALID_SEQUENCE   # The sequence is not valid.
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
            #termcolor.cprint(text, 'yellow')
            print(text)

    def __str__(self):  # Whatever is witten here, will be executed when I press "print".
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):   # If the sequence is null or not valid, it is not going to count it. If this gets executed in these cases, we will return 0,0,0,0
        a, c, g, t = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, g, t
        else:
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                elif ch == "T":
                    t += 1
            return a, c, g, t


    def count_bases(self):  # Cleaner way to do it, instead of using a pass in the case of the null and invalid sequences (DOUBT)
        a, c, g, t = 0, 0, 0, 0
        if not self.strbases == Seq.NULL_SEQUENCE and not self.strbases == Seq.INVALID_SEQUENCE:
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                elif ch == "T":
                    t += 1
        return a, c, g, t  # It must be here, because if it is more to the right, it will only return something in case the sequence is valid.

    def count(self):
        a, c, g, t = self.count_bases()
        return {"A": a, "C": c, "T": t, "G": g}

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            complement = ""
            for ch in self.strbases:
                if ch == "A":
                    complement += "T"
                elif ch == "C":
                    complement += "G"
                elif ch == "G":
                    complement += "C"
                elif ch == "T":
                    complement += "A"
            return complement

    @staticmethod    # In order not to pass the "self" in the parenthesis of the function.
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())

def test_sequences():  # In order not to write the sequences in all the exercises. It can be written at the top of the program also.
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid Sequence")
    return s1, s2, s3