from Seq1 import Seq

GENE_FOLDER = "../P0/Sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
base_list = ["A", "C", "G", "T"]

for gene in gene_list:
    sequence = Seq()
    sequence.read_fasta(GENE_FOLDER + gene + ".txt")
    count_tuple = Seq.count_bases(sequence)
    c = 0
    for i in range(0, len(count_tuple)):
        if count_tuple[i] > c:
            c = count_tuple[i]
            base = base_list[i]
    print("Gene", gene, ": Most frequent base:", base)