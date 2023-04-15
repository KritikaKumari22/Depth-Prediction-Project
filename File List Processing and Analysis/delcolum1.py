# import os
import sys

# PDBs_Broken="Broken_PDBs.txt"
# Broken_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/"
# PDBs_Broken_filepath=os.path.join(Broken_path, PDBs_Broken)
Initial= sys.argv[1]

# new_PDBs_Broken="new_Broken_PDBs.txt"
# new_Broken_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/"
# new_PDBs_Broken_filepath=os.path.join(new_Broken_path, new_PDBs_Broken)
Final =sys.argv[2]

new_lines=[]
with open(Initial) as inf:
            lines = [x for x in inf.readlines() if len(x)>0]

            for k in lines:
                new_lines.append(k.split(' ')[1].strip())

with open(Final,'a+') as uf:
    for l in new_lines[:-1]:
        uf.write(l.rstrip()+'\n')
    uf.write((new_lines[-1]).rstrip())