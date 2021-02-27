from pathlib import Path

#For Ex1
def seq_ping():
    print("OK")

def take_out_first_line(seq):
    return seq[seq.find("\n") + 1:].replace("\n", "")

#For Ex2
def seq_read_fasta(filename):
   sequence = Path(filename).read_text()
   sequence = sequence[sequence.find("\n") + 1:].replace("\n", "")
   return sequence

#For Ex3
def seq_len(seq):
    return len(seq)

#For Ex4
def seq_count_base(seq, base):
    return seq.count(base)

#For Ex5

def seq_count(seq):
    gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for d in seq:
        gene_dict[d] += 1
    return gene_dict


"""def seq_count(seq):  (Another way to do it)
    a, c, g, t = 0, 0, 0, 0
    for c in seq:
        if c == "A":
            a +=1
        elif c == "C":
            c +=1
        elif d == "G":
            g +=1
        else:
            t += 1
    return {"A": a, "C": c, "G": g, "T": t}
    gene_dict = {}
    gene_dict["A"] = a"""

#For Ex6

def seq_reverse(seq):
    reverse = seq[::-1]
    return reverse

#For Ex7

def seq_complement(seq):
    complement_seq = " "
    for gene in seq:
        if gene == "A":
            complement_seq += "T"
        elif gene == "T":
            complement_seq += "A"
        elif gene == "C":
            complement_seq += "G"
        elif gene == "G":
            complement_seq += "C"
    return complement_seq

