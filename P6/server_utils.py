from Seq1 import Seq
import jinja2
import pathlib
from urllib.parse import urlparse, parse_qs
GENE_FOLDER = "./Sequences/"

def print_colored(message, color):pass
    #import termcolor
    #import colorama
    #colorama.init(string="False")
    #print(termcolor.colored(message, color))

def format_command(command): #used not to get PING\r\n
    return command.replace("\n","").replace("\n","")

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

def ping(cs):
    #print_colored("PING command!", "green")
    response = "OK!\n"
    cs.send(response.encode())

def get(cs, list_sequences, argument):
    cs.send(get(list_sequences, argument).encode())

def get(list_sequences, argument):
    sequence = list_sequences[int(argument)]
    context = {
        "number": argument,
        "sequence": sequence
    }
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents



def info(argument):
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
    context = {"Sequence: " + argument + "\n" + "Total length: " + response_2 + "\n" + response_3}
    contents = read_template_html_file("./html/info.html").render(context=context)
    return contents

def comp(argument):
    #print_colored("COMP", "yellow")
    print("COMP")
    sequence = Seq(argument)
    response = sequence.complement()
    context = {"sequence": argument, "comp_sequence": response}
    contents = read_template_html_file("./html/comp.html").render(context=context)
    return contents

def rev(argument):
    #print_colored("REV", "yellow")
    print("REV")
    sequence = Seq(argument)
    response = sequence.reverse()
    context = {"sequence": argument, "rev_sequence": response}
    contents = read_template_html_file("./html/rev.html").render(context=context)
    return contents

def gene(seq_name):
    GENE_FOLDER = "./Sequences/"
    argument = GENE_FOLDER + seq_name + ".txt"
    gene = Seq()
    gene.read_fasta(argument)
    context ={
        "gene_name": seq_name,
        "gene_contents": gene.str_bases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents
