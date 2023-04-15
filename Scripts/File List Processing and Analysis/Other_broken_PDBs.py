import os
import sys
import re

Extrapdb="UNKs_broken_pdbs.txt"
Extra_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/Alphafold/"
Extra_filepath=os.path.join(Extra_path, Extrapdb)

Not_chain_broken="Not_broken_pdbs.txt"
Not_broken_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/Got Chain break info/"
Not_broken_filepath=os.path.join(Not_broken_path, Not_chain_broken)

UNK_results= "C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/PDBs_w_UNK.txt"
# Used_in_downloading= "C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/Alphafold/new_Broken_PDBs.txt"
All_broken_PDBS= "C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/Got Chain break info/All_broken_PDBs.txt"

# got_detailed_pdbs=[]
# with open(Detailed_results,'r') as inf:
            # lines = [x for x in inf.readlines() if x[0].isdigit()]

            # for k in lines:
            #     k=str(k)
            #     if len(k.split(' ')) >= 2:
            #         line=k.split(' ')
            #         dir= line[1]
            #         if dir.startswith('/scratch/'):
            #             got_detailed_pdbs.append(dir)

# for j in got_detailed_pdbs:
#     with open(All_broken_PDBS,'a+') as gf:
#         gf.write(j)



#                         got_detailed_pdbs.append(dir)
#                         # print(dir)



got_detailed_pdbs=[]
with open(All_broken_PDBS,'r') as inf:
            lines = [x for x in inf.readlines()]

            for k in lines:
                got_detailed_pdbs.append(k)

pdbs=[]
with open(UNK_results,'r') as inf:
            lines = [x for x in inf.readlines() if x[0].isdigit()]

            for k in lines:
                k=str(k)
                if len(k.split(' ')) >= 2:
                    line=k.split(' ')
                    dir= line[1]
                    if dir.startswith('/scratch/'):
                        pdbs.append(dir)


for i in pdbs:
    if i in got_detailed_pdbs:
        with open(Extra_filepath,'a+') as uf:
                uf.write(i)

# for j in pdbs:
#     if j not in got_detailed_pdbs:
#         with open(Not_broken_filepath,'a+') as gf:
#                 gf.write(j)



