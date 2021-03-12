import termcolor

class Seq:

    def __init__(self, strbases):
        if Seq.is_valid_sequence_2(strbases):
            print('New sequence created')
            self.strbases = strbases
        else:
            self.strbases = 'Error'
            print('INCORRECT sequence detected')

    def __str__(self):
    	return self.strbases

    def len(self):
        return len(self.strbases)
    @staticmethod
    def is_valid_sequence_2(bases):
        for i in bases:
            if i != 'A' and i != 'T' and i != 'C' and i != 'G':
                return False
            return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = 'Sequence' + str(i) + ': ( Lenght :' + str(list_sequences[i].len()) + ')' + str(list_sequences[i])
            termcolor.cprint(text, 'yellow')


def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
        return list_seq




