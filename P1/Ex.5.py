from Seq1 import Seq

def print_result(i, sequence):
    print("Sequence" + str(i) + ": (Length: " + str(sequence.len()) + " ) " + str(sequence))
    a, c, g, t = sequence.count_bases()
    print("A: " + str(a) + ", C: " + str(c) + ", T: " + str(t) + ", G: " + str(g) + ",")

print("-----| Practice 1, Exercise 5 |-----")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid Sequence")

"""list_seq = [s1, s2, s3]

for i in range(1, 4):
    print_result(i, list_seq[i-1])"""  # Possible solution for this case, but if we have more sequences, we have to add them manually.

list_seq = [s1, s2, s3]

for i in range(1, len(list_seq) +1):  # This solution is the same than the above one but improved.
    print_result(i, list_seq[i-1])




"""print_result(1, s1)
print_result(2, s2)
print_result(3, s3)"""