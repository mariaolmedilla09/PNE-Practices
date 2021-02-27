import Seq0

GENE_FOLDER = "./Sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "T", "G" ]

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    count = 0
    print("Gene", gene)
    for base in base_list:
        print(base + ":", Seq0.seq_count_base(sequence, base))
        appearance = Seq0.seq_count_base(sequence, base)
        if appearance > count:
            count = appearance
    print("Gene", gene, ": Most frequent base:", base)