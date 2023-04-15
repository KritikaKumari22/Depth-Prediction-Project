import os
import sys

pdbs=[]
with open("C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/PDBs_w_UNK.txt") as inf:
            lines = [x for x in inf.readlines()]

            for k in lines:
                k=k.split(' ')
                filename = str(k[1])
                extracted_string = filename.rsplit("/", 1)[-1].split("-")[0]
                result = extracted_string[3:] + '.pdb'
                pdbs.append(result)

print(pdbs)
print(len(pdbs))
# folder= "./Downloads/"
# for filename in os.listdir(folder):


for filename in pdbs:
    try:
        os.rename("./Downloads/"+filename, "./d/UNK_"+filename)
    except Exception as e:
        print(e)
        print(filename)

