# Implement the seq_len(seq) function, that calculates the total number of bases in the sequence. It should be written in the Seq0.py file.

import Seq0

GENE_FOLDER = "./Sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    print("Gene " + gene + " ---> Length:" + str(Seq0.seq_len(sequence)))


