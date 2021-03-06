# Which is the most frequent base in each gene?
# Output: number of times that the bases appear + the most common one.

import Seq0

GENE_FOLDER = "./Sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "T", "G" ]

print("-----| Exercise 8|-----")

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    count = 0
    print("Gene", gene)
    for base in base_list:
        print(base + ":", Seq0.seq_count_base(sequence, base))
        appearance = Seq0.seq_count_base(sequence, base)
        if appearance > count:
            count = appearance
            higher_base = base
    print("Gene", gene, ": Most Frequent Base:", higher_base)