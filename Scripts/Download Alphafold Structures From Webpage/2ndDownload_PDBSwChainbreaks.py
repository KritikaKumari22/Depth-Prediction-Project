import os
import sys
import urllib.request

PDBs_Broken="new_Broken_PDBs.txt"
new_Broken_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/"
PDBs_Broken_filepath=os.path.join(new_Broken_path, PDBs_Broken)

pdbs=[]
with open(PDBs_Broken_filepath) as inf:
            lines = [x for x in inf.readlines()]

            for k in lines:
                filename = str(k)
                extracted_string = filename.rsplit("/", 1)[-1].split("-")[0] + ".pdb"
                result = extracted_string[3:]
                pdbs.append(result)
base_url = 'https://files.rcsb.org/download/'
for pdb in pdbs:
    pdb_file = pdb
    url = base_url + pdb_file
    urllib.request.urlretrieve(url, pdb_file)