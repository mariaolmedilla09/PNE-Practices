# Implement the seq_read_fasta(filename) function. It should open a file, in FASTA format, and return a String with the DNA sequence. The head is removed, as well as the '\n' characters.
# This function should be written in the Seq0.py file

import Seq0
FOLDER = "./Sequences/" # We write "./Sequences/" to go to the parent folder of Ex2 (P0)
                        # We write "../Sequences/" to find the parent folder of the parent folder (PNE-Practices)
ID = "ADA.txt"
U5_seq = Seq0.seq_read_fasta(FOLDER + ID)

print("The frist 20 bases are: ", U5_seq[0:20])



