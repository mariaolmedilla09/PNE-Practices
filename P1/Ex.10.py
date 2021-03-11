from Seq1 import Seq

GENE_FOLDER = "../P0/Sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
base_list = ["A", "C", "T", "G" ]

print("-----| Practice 1, Exercise 10 |-----")

for gene in gene_list:
    sequence = Seq()
    sequence.read_fasta(GENE_FOLDER + gene + ".txt")
    appearance = Seq.count_bases(sequence)
    count = 0
    for e in range(0, len(appearance)):
         if appearance[e] > count:
            count = appearance[e]
            higher_base = base_list[e]
    print("Gene", gene, ": Most Frequent Base:", higher_base)



