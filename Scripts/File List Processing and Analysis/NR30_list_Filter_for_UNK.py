import os
# import sys

NR30_widout_UNKs="NR30_widout_UNKs.txt"
UNK_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/"
new_nr30__filepath= os.path.join(UNK_path, NR30_widout_UNKs)

NR30_original_list="nr30_list.txt"
NR30_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/"
NR30_filepath= os.path.join(NR30_path, NR30_original_list)

PDBs_w_UNK="PDBs_w_UNK.txt"
w_UNK_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/"
PDBs_w_UNK_filepath=os.path.join(w_UNK_path, PDBs_w_UNK)

new_lines=[]
with open(NR30_filepath) as inf:
            lines = [x for x in inf.readlines() if len(x)>0]
            with open(PDBs_w_UNK_filepath,'r') as uf:
                # uf.seek(0)
                lines_rm = uf.readlines()
                rmv=[]
                for k in lines_rm:
                    rmv.append(k.split(' ')[1].strip())
                    # print(k.split(' ')[1])
                    
                # print(len(rmv))
                i=0
                for line in lines:
                    if line.strip() not in rmv:
                        # print(rmv_line[1])
                        new_lines.append(line)
                    else:
                        # print(line)
                        i+=1
                # print(i)
# print(new_lines)

with open(new_nr30__filepath,'a+') as new:
    for l in new_lines[:-1]:
        new.write(l.rstrip()+'\n')
    new.write((new_lines[-1]).rstrip())

                                  