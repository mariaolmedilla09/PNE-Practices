# Write a python program for creating a new fragment composed of the first 20 bases of the U5 gene.
# Then calculate the reverse of this fragment by calling the seq_reverse() function. Finally print it on the console
import Seq0
FOLDER = "./Sequences/"
ID = "U5.txt"
U5_seq = Seq0.seq_read_fasta(FOLDER + ID)
print("-----| Exercise 6|-----")
print("Gene U5")
print("Frag: ", U5_seq[0:20])
print("Rev: ", Seq0.seq_reverse(U5_seq[0:20]))
