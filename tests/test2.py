'''
Compares the output of print_query on query #34 of CISI
'''

import sys
import subprocess

query34 = "Methods of coding used in computerized index systems." 

program = "./code/print_query.py"
collection = "CISI"
query = "34"

output = subprocess.check_output(["python3", program, collection, query])
answer = output.decode('utf-8').strip()

# compare outputs, word by word
words_answer = answer.split()
words_query34 = query34.strip().split()

if len(words_query34) == len(words_answer):
    for i in range(len(words_answer)):
        if words_query34[i] != words_answer[i]:
            print("ERROR .I= 34")
            exit(1) # signal error to OS

    # if we reach this point, the answer is correct
    print("NO ERROR")
    exit(0) # signal success to OS

# if we reach this point, the returned answer is not as expected
print("ERROR .I= 34")
exit(1) # signal error to OS