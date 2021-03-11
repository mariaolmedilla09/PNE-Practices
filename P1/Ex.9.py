from Seq1 import Seq

def print_result(sequence):
    print("Sequence" + ": (Length: " + str(sequence.len()) + " ) " + str(sequence))
    print("Bases: ", sequence.count())
    print("Rev: ", sequence.reverse())
    print("Comp: ", sequence.complement())

print("-----| Practice 1, Exercise 9 |-----")
s1 = Seq()
s1.read_fasta("ADA.txt")
print_result (s1)
