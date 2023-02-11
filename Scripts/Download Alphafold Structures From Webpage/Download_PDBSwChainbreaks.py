import os
# import sys
import shutil
import urllib.request

PDBs_Broken="Extra_PDBs_to_download.txt"
new_Broken_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/Alphafold/"
PDBs_Broken_filepath=os.path.join(new_Broken_path, PDBs_Broken)

NoUniprot_Id_inpdb="NoUniprot_Id_inpdb_filepath.txt"
new_Broken_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/Alphafold/"
NoUniprot_Id_inpdb_filepath=os.path.join(new_Broken_path, NoUniprot_Id_inpdb)

Rerun_inpdb="Rerun_pdbs.txt"
Rerun_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/Alphafold/"
Rerun_filepath=os.path.join(Rerun_path, Rerun_inpdb)


NoAlphafoldstrs="No_Alphafold_strs.txt"
new_Broken_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/Alphafold/"
NoAlphafoldstrs_filepath=os.path.join(new_Broken_path, NoAlphafoldstrs)

pdbs=[]
with open(PDBs_Broken_filepath) as inf:
            lines = [x for x in inf.readlines()]
            

            for k in lines:
                filename = str(k.strip())
                print(filename)
                extracted_string = filename.rsplit("/", 1)[-1].split("-")[0]
                result = extracted_string[3:]
                pdbs.append(result)
base_url = 'https://www.rcsb.org/structure/'
base_alphafold='https://alphafold.ebi.ac.uk/files/AF-'
pdb_url='-F1-model_v4.pdb'
# s=urllib.request.urlopen('https://www.rcsb.org/structure/1C0W')
for pdb in pdbs[:]:
    url = base_url + pdb
    try:
        wp=urllib.request.urlopen(url,timeout=3600)
        wp=(wp.read()).decode('utf-8')
        try:
            index=wp.find("https://www.uniprot.org/uniprot/")
            index=index+32
            Id=wp[index:index+6]
            alpha_url=base_alphafold + Id + pdb_url
            if Id != '<head>':
                try:
                    with urllib.request.urlopen(alpha_url,timeout=3600) as response, open(pdb+".pdb", 'wb') as out_file:
                        shutil.copyfileobj(response, out_file)
                    print('Downloading!')
                except Exception as e:
                    print(e)
                    with open(NoAlphafoldstrs_filepath,'a+') as ids:
                        ids.write(pdb+' '+Id+'\n')
            else: 
                with open(NoUniprot_Id_inpdb_filepath,'a+') as no:
                    no.write(pdb+'\n')
        except Exception as e:
            with open(NoUniprot_Id_inpdb_filepath,'a+') as no:
                    no.write(pdb+'\n')
    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print(e)
            with open(Rerun_filepath,'a+') as re:
                re.write(pdb+'\n')
