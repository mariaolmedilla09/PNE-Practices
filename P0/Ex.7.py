# Implement the seq_complement(seq) function, that calculates a new sequence composed of the complement base of each of the original bases.
# A and T are complement, as well as C and G.
import Seq0
FOLDER = "./Sequences/"
ID = "U5.txt"
U5_seq = Seq0.seq_read_fasta(FOLDER + ID)

print("-----| Exercise 7|-----")

print("Frag: ", U5_seq[0:20])
print("Comp: ", Seq0.seq_complement(U5_seq[0:20]))