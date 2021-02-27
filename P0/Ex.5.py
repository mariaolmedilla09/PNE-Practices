# Write a python program for calculating the number of each bases located on each of the five genes.
# It is similar to exercise 4, but what is printed on the console is the dictionary returned by the seq_count() function.
import Seq0

GENE_FOLDER = "./Sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    print("Gene ", gene, ":" , Seq0.seq_count(sequence))
