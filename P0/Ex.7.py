import Seq0
FOLDER = "./Sequences/"
ID = "U5.txt"
U5_seq = Seq0.seq_read_fasta(FOLDER + ID)
print("Frag: ", U5_seq[0:20])
print("Comp: ", Seq0.seq_complement(U5_seq[0:20]))