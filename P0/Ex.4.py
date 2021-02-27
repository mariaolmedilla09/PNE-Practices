# Implement the seq_count_base(seq, base) function, that calculates the number of times the given base appears in the sequence.
# It should be written in the Seq0.py file.

import Seq0

GENE_FOLDER = "./Sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "T", "G" ]

print("-----| Exercise 4|-----")

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    print("Gene", gene)
    for base in base_list:
        print(base + ":", Seq0.seq_count_base(sequence, base))
