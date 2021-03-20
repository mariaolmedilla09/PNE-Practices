from Client0 import Client
from pathlib import Path
from Seq1 import Seq

print("-----| Practice 2, Exercise 5 |-----")

IP = "127.0.0.1"
PORT_1 = 12000
PORT_2 = 12300
c_1 = Client(IP, PORT_1)
c_2 = Client(IP, PORT_2)

s = Seq()
s.seq_read_fasta('../Session-04/FRAT1.txt')
count = 0
i = 0
while i < len(s.strbases) and count < 10:
    fragment = s.strbases[i: i + 10]
    count += 1
    i += 10
    print("Fragment: ", count, ":", fragment)
    if count % 2 == 0:
        print(c_2.talk("Fragment " + str(count) + ": " + fragment))
    else:
        print(c_1.talk("Fragment " + str(count) + ": " + fragment))


