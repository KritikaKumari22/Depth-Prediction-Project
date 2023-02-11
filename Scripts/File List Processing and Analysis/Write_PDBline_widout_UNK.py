import os

PDB_nrs= 0
import sys

infile = sys.argv[1]
# with open(infile) as inf:
#     ensemble_lines = inf.readlines()
x=[]
with open(infile) as inf:
    for ensemble_lines in inf.readlines():
        if ensemble_lines.startswith('ATOM'):
            if ensemble_lines[17:20] != 'UNK':
                x.append(ensemble_lines)

# print(x)

# res_ids = ''
# n = 0

# if ensemble_lines[n][17:20] == 'UNK':
    #    PDB_nrs+=1

with open('PDBids_toremove.txt','w') as ouf:
    for strings in x:
                ouf.write(strings)
    ouf.write(str(infile))
    ouf.close()
    


