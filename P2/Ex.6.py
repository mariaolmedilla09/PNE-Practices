from Client0 import Client
from pathlib import Path
from Seq1 import Seq

print("-----| Practice 2, Exercise 5 |-----")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)

s = Seq()
s.seq_read_fasta('../Session-04/FRAT1.txt')
count = 0
"""for i in range(0, len(s.strbases), 10):   # We go from 10 to 10: from i to 10.
    fragment = s.strbases[i:i+10]
    print(fragment)
    count = count +1
    if count == 5:
        break"""   # This is a possible solution to this issue, but the following one is better.

i = 0
while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i: i + 10]
    count += 1
    i += 10
    print("Fragment: ", count, ":", fragment)
    print(c.talk(fragment))
    # Now, once we have split the fragments in a correct way, we need to send them to the Server. As we want to send each of the fragments, we must write it inside the loop

