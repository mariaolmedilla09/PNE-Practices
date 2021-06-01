from Seq1 import Seq
import pathlib
import jinja2
import requests
GENE_FOLDER = "./Sequences/"

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print(termcolor.colored(message, color))

def format_command(command): #this is bc if we try to send "PING", we get PING\r\n
    return command.replace("\n", "").replace("\r", "")

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

def ping(cs):
    print_colored("PING command", "green")
    response = "OK"
    cs.send(response.encode())

def get(list_sequences, seq_number):
    sequence = list_sequences[int(seq_number)]
    context = {"number": seq_number, "sequence": sequence}
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents


def info(argument):
    print_colored("INFO", "yellow")
    seq = Seq(argument)
    length = "Total length: " + str(seq.len())
    bases_count = seq.count_bases()[0]
    percentages = seq.count_bases()[1]
    response = [length]
    for i in range(0, len(bases_count)):
        list_bases = ["A: ", "C: ", "G: ", "T: "]
        response.append(list_bases[i] + str(bases_count[i]) + " -->  " + str(percentages[i]) + "%")
    context = {'sequence': argument, 'info_sequence': response}
    contents = read_template_html_file("./html/info.html").render(context=context)
    return contents

def comp(argument):
    print_colored("COMP", "yellow")
    seq = Seq(argument)
    complement = seq.complement()
    context = {"sequence": argument, "comp_sequence": complement}
    contents = read_template_html_file("./html/comp.html").render(context=context)
    return contents


def karyotype_by_specie(argument, return_html):
    species = argument
    species_fmt = species.replace(' ', '_').lower()
    endpoint_by_specie = 'https://rest.ensembl.org/info/assembly/{}?content-type=application/json'.format(species_fmt)
    r = requests.get(endpoint_by_specie).json()
    if 'karyotype' in r:
        response = r['karyotype']
    else:
        response = 'karyotype not available for that species'
    context = {'karyotype': response, 'species': species}

    if return_html:
        return read_template_html_file("./html/karyotype.html").render(context=context)
    else:
        print("The requested json is the following: ", context)
        return context

def chromosome_length(species, length_name, return_html):

    species_fmt = species.replace(' ', '_').lower()
    endpoint_by_specie = 'https://rest.ensembl.org/info/assembly/{}?content-type=application/json'.format(species_fmt)
    r = requests.get(endpoint_by_specie).json()
    if 'top_level_region' in r:
        for e in r['top_level_region']:
            if e['name'] == length_name:
                response = e['length']
                break
        context = {'length_chromosome': response, 'species': species}
        if return_html:
            return read_template_html_file("./html/chromosome_length.html").render(context=context)
        else:
            print("The requested json is the following: ", context)
            return context

    else:
        if return_html:
            return read_template_html_file("./html/error.html").render()
        else:
            print("{'Error' : ''}")
            return {'Error' : ''}


def get_gene_id_by_name(gene_name):
    genes_dict = {
        "FRAT1": "ENSG00000165879",
        "ADA": "ENSG00000196839",
        "FXN": "ENSG00000165060",
        "RNU6_269P": "ENSG00000212379",
        "MIR633": "ENSG00000207552",
        "TTTY4C": "ENSG00000228296",
        "RBMY2YP": "ENSG00000227633",
        "FGFR3": "ENSG00000068078",
        "KDR": "ENSMUSG00000062960",
        "ANK2": "ENSG00000145362"
    }
    if gene_name in genes_dict:
        return genes_dict[gene_name]
    elif not gene_name in genes_dict:
        return "NONE"


def gene_sequence(gene_name, return_html):
    context = {}
    try:
        url_gene_seq = 'https://rest.ensembl.org/sequence/id/{0}?content-type=text/plain'.\
            format(get_gene_id_by_name(gene_name))
        r = requests.get(url_gene_seq).text
    except:
        if return_html:
            return read_template_html_file("./html/error.html").render()
        else:
            print("{'Error' : ''}")
            return {'Error': ''}

    context['gene_name'] = gene_name
    context['sequence'] = r
    if return_html:
        return read_template_html_file("./html/gene_sequence.html").render(context=context)
    else:
        print("The requested json is the following: ", context)
        return context

def gene_info(gene_name, return_html):
    context = {}
    try:
        url_gene_info = 'http://rest.ensembl.org/sequence/id/{}?content-type=application/json'.\
            format(get_gene_id_by_name(gene_name))
        r = requests.get(url_gene_info).json()
    except:
        if return_html:
            return read_template_html_file("./html/error.html").render()
        else:
            print("{'Error' : ''}")
            return {'Error':''}
    context['gene_name'] = gene_name
    context['id'] = r['id']
    sequence = r['seq']
    len_sequence = len(sequence)
    context['length'] = len_sequence
    information = r['desc']
    information_splitted = information.split(':')
    context['name'] = information_splitted[1]
    context['start'] = information_splitted[3]
    context['end'] = information_splitted[4]
    if return_html:
        return read_template_html_file("./html/gene_info.html").render(context=context)
    else:
        print("The requested json is the following: ", context)
        return context

def gene_calc(gene_name, return_html):
    context = {}
    try:
        url_gene_calc = 'https://rest.ensembl.org/sequence/id/{0}?content-type=text/plain'. \
            format(get_gene_id_by_name(gene_name))
        r = requests.get(url_gene_calc).text
    except:
        if return_html:
            return read_template_html_file("./html/error.html").render()
        else:
            print("{'Error' : ''}")
            return {'Error': ''}

    context['gene_name'] = gene_name
    sequence_gene = Seq(r)
    len_sequence_gene = sequence_gene.len()
    len_sequence_percentage = sequence_gene.percentage_base(sequence_gene.count_bases(),len_sequence_gene)
    context['len_sequence_gene'] = len_sequence_gene
    context['sequence_percentage_gene'] = len_sequence_percentage
    if return_html:
        return read_template_html_file("./html/gene_calc.html").render(context=context)
    else:
        print("The requested json is the following: ", context)
        return context


def list_species(argument, return_html):

    context = {}
    if len(argument) > 0:
        context["limit"] = argument
    else:
        if return_html:
            return read_template_html_file("./html/error.html").render()
        else:
            print("{'Error' : ''}")
            return {'error' : ''}

    limit_int = int(argument)

    url_emsembl_species = 'http://rest.ensembl.org/info/species?content-type=application/json'

    r = requests.get(url_emsembl_species).json()

    list_of_species = []
    if 'species' in r:
        len_list_of_species_tot = len(r['species'])
        #print(len_list_of_species_tot)
        if limit_int > len_list_of_species_tot:
            if return_html:
                return read_template_html_file("./html/error.html").render()
            else:
                return {'error': ''}

        for specie_data in r['species']:
            list_of_species.append(specie_data['common_name'])
            if len(list_of_species) == limit_int:
                break

    context['len_species'] = len_list_of_species_tot

    if return_html:
        if len_list_of_species_tot > 1:
            pretty_str_list_of_species = '-' + list_of_species[0] + '<br /> -'
            pretty_str_list_of_species += '<br /> -'.join(list_of_species[1:])
        elif len_list_of_species_tot == 1:
            pretty_str_list_of_species = '-' + list_of_species[0]
        else: pretty_str_list_of_species = ''
        context["list_species"] = pretty_str_list_of_species
        return read_template_html_file("./html/list_species.html").render(context=context)

    else:
        context["list_species"] = list_of_species
        print("The requested json is the following: ", context)
        return context


def rev(argument):
    print_colored("REV", "yellow")
    seq = Seq(argument)
    reverse = seq.reverse()
    context = {"sequence": argument, "rev_sequence":reverse}
    contents = read_template_html_file("./html/rev.html").render(context=context)
    return contents

def gene(seq_name):
    print_colored("GENE", "yellow")
    PATH = GENE_FOLDER + seq_name + ".txt"
    s1 = Seq()
    s1.read_fasta(PATH)
    context = {"gene_name": seq_name, "gene_contents": s1.strbases}
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents