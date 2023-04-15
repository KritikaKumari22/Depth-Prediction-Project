import os
# import sys
import shutil
import urllib.request

file="Org_list.txt"
path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/Radial Neighbours/REdownload the Originally CLean PDBs/"
filepath=os.path.join(path, file)

pdb_filenames=[]
with open(filepath) as inf:
            lines = [x for x in inf.readlines()]
            

            for k in lines:
                filename = str(k.strip())
                # print(filename)
                extracted_string = filename.rsplit("/", 1)[-1].split("-")[0]
                result = extracted_string[3:8] + '.pdb'
                pdb_filenames.append(result)
print(pdb_filenames)

# Base URL for downloading PDB files from RCSB PDB
base_url = "https://files.rcsb.org/download/"

# loop through the list of PDB filenames and download each file
for pdb_filename in pdb_filenames[1902:]:
    # remove newline character at the end of the filename
    pdb_filename = pdb_filename.strip()
    url = base_url + pdb_filename
    try:
        with urllib.request.urlopen(url, timeout=3600) as response, open(pdb_filename, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print(f'Downloaded {pdb_filename} from {url}')
    except Exception as e:
        print(f'Error downloading {pdb_filename} from {url}: {e}')