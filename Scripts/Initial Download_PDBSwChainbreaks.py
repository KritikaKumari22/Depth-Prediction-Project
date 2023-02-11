import os
# import sys
import urllib.request

PDBs_Broken="new_Broken_PDBs.txt"
new_Broken_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/Alphafold/"
PDBs_Broken_filepath=os.path.join(new_Broken_path, PDBs_Broken)

NoUniprot_Id_inpdb="NoUniprot_Id_inpdb_filepath.txt"
new_Broken_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/Alphafold/"
NoUniprot_Id_inpdb_filepath=os.path.join(new_Broken_path, NoUniprot_Id_inpdb)


NoAlphafoldstrs="No_Aplhafold_strs.txt"
new_Broken_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/Alphafold/"
NoAlphafoldstrs_filepath=os.path.join(new_Broken_path, NoAlphafoldstrs)

pdbs=[]
with open(PDBs_Broken_filepath) as inf:
            lines = [x for x in inf.readlines()]

            for k in lines:
                filename = str(k)
                extracted_string = filename.rsplit("/", 1)[-1].split("-")[0]
                result = extracted_string[3:]
                pdbs.append(result)
base_url = 'https://www.rcsb.org/structure/'
base_alphafold='https://alphafold.ebi.ac.uk/files/AF-'
pdb_url='-F1-model_v4.pdb'
# s=urllib.request.urlopen('https://www.rcsb.org/structure/1C0W')
for pdb in pdbs:
    url = base_url + pdb
    wp=urllib.request.urlopen(url)
    wp=(wp.read()).decode('utf-8')
    try:
        index=wp.find("https://www.uniprot.org/uniprot/")+32
        Id=wp[index:index+6]
        aplha_url=base_alphafold + Id + pdb_url
        try:
            urllib.request.urlretrieve(aplha_url)
        except Exception as e:
            print(e)
            with open(NoAlphafoldstrs_filepath,'a+') as ids:
                ids.write(pdb+' '+Id+'\n')
    except:
        with open(NoUniprot_Id_inpdb_filepath,'a+') as no:
            no.write(pdb+'\n')
