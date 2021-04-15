from Seq1 import Seq
def print_colored(message, color):pass
    #import termcolor
    #import colorama
    #colorama.init(string="False")
    #print(termcolor.colored(message, color))

def format_command(command): #used not to get PING\r\n
    return command.replace("\n","").replace("\n","")

def ping(cs):
    #print_colored("PING command!", "green")
    response = "OK!\n"
    cs.send(response.encode())

def get(cs, list_sequences, argument):
    #print_colored("GET", "yellow")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(response.encode())

def info(cs, argument):
    #print_colored("INFO", "yellow)
    print("INFO")
    sequence = Seq(argument)
    total_length = str(sequence.len())
    response_2 = total_length
    count_diff_bases = sequence.count_bases()
    sum = count_diff_bases[0] + count_diff_bases[1] + count_diff_bases[2] + count_diff_bases[3]
    percen_a = "(" + str(round((count_diff_bases[0] / sum) * 100,2)) + "%" + ")"
    percen_c = "(" + str(round((count_diff_bases[1] / sum) * 100,2)) + "%" + ")"
    percen_g = "(" + str(round((count_diff_bases[3] / sum) * 100,2)) + "%" + ")"
    percen_t = "(" + str(round((count_diff_bases[2] / sum) * 100,2)) + "%" + ")"
    response_3 = "A: " + str(count_diff_bases[0]) + percen_a + "\n" + "C: " + str(count_diff_bases[1]) + percen_c + "\n" + "G: " + str(count_diff_bases[3]) + percen_g + "\n" + "T: " + str(count_diff_bases[2]) + percen_t + "\n"
    cs.send(("Sequence: " + argument + "\n" + "Total length: " + response_2 + "\n" + response_3).encode())
    print("Sequence: " + argument + "\n" + "Total length: " + response_2 + "\n" + response_3)

def comp(cs, argument):
    #print_colored("COMP", "yellow")
    print("COMP")
    sequence = Seq(argument)
    response = sequence.complement()
    cs.send(response.encode())
    print(response)

def rev(cs, argument):
    #print_colored("REV", "yellow")
    print("REV")
    sequence = Seq(argument)
    response = sequence.reverse()
    cs.send(response.encode())
    print(response)

def gene(cs, argument):
    GENE_FOLDER = "./Sequences/"
    argument = GENE_FOLDER + argument + ".txt"
    gene = Seq()
    gene.read_fasta(argument)
    cs.send(str(gene).encode())
    print(gene)
