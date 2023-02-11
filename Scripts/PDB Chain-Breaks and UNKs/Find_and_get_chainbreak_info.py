def get_ATOM_lines_from_PDB_lines(all_PDB_lines):    
    # Long version of the code easy to understand
    ATOM_lines = []
    for line in all_PDB_lines:
        if line.startswith('ATOM'):
            ATOM_lines.append(line)
    
    # Shorter version can be writen in one line
    #ATOM_lines = [line for line in all_PDB_lines if line.startswith('ATOM')]    
    return ATOM_lines
    
def find_chain_breaks(ATOM_lines):
    chain_res_dict = find_chain_wise_residue_list(ATOM_lines)    
    break_dict = find_breaks_from_chain_res_dict(chain_res_dict)
    return break_dict


def find_chain_wise_residue_list(ATOM_lines): 
    # finds a list of residue numbers for each chain    
    # Initiating a dictionary where chain id forms the key and the value is an empty dictioary
    chain_res_dict = dict([(line[21:22],[]) for line in ATOM_lines]) # this is short hand version of a for loop
    
    # Filling the empty dictionary with residue numbers for each chain
    for line in ATOM_lines:        
        chain_res_dict[line[21:22]].append(int(line[22:26].strip()))
    return chain_res_dict

def find_breaks_from_chain_res_dict(chain_res_dict):
    break_dict = {} # dictionary to store breaks
    for chain in chain_res_dict.keys():
        # Finding missing ints from residue number ilst
        k = find_missing_ints_starting_from_1(chain_res_dict[chain])
        if len(k)!=0:
            break_dict[chain] = find_missing_ints_starting_from_1(chain_res_dict[chain])
    return break_dict

def find_missing_ints_starting_from_1(list_of_ints):
    # loop thorugh interger from 1 to largest int in the list
    # if the input has a missing number, store it in a list    
    missing_ints = [] 
    for x in range(1,max(list_of_ints)+1):
        if x not in list_of_ints:
            missing_ints.append(x)
    return missing_ints


import os
import sys

UNK_file="10-02-PDBs_w_UNK.txt"
UNK_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/Alphafold"
UNK__filepath= os.path.join(UNK_path, UNK_file)

Broken_file="10-02-Broken_PDBs.txt"
Broken_path="C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/Alphafold"
Broken_filepath=os.path.join(Broken_path, Broken_file)

# var=sys.argv[2]
path = sys.argv[1]
i=0
j=0
for filename in os.listdir(path):
          if filename.endswith('.pdb'):
            # print(filename,i)
            with open(path+"/"+filename) as inf:
                # ensemble_lines = [y for y in inf.readlines()]
                atom_lines = [x for x in inf.readlines() if x.startswith('ATOM')]
                for y in atom_lines:
                    if y[17:20] == 'UNK':
                                i+=1
                                print(i,str(filename))
                                with open(UNK__filepath,'a') as ouf:
                                    ouf.write('\n'.join([str(i)+' '+str(filename)+'\n']))                    
                                break
                    elif ' UNK ' in y:
                                i+=1
                                print(i,str(filename))
                                with open(UNK__filepath,'a') as f:
                                    f.write('\n'.join([str(i)+' '+str(filename)+' Chain Breaked'+'\n']))                    
                                break


                break_dict = find_chain_breaks(atom_lines)
                if len(break_dict) > 0: 
                              
                                with open(Broken_filepath,'a+') as uf:
                                    uf.seek(0)
                                    lines = [x for x in uf.readlines() if x[0].isdigit()]
                                    j = len(lines)+1
                                    uf.write('\n'.join([str(j)+' '+str(filename)+'\n']))
                                    missing_Res=[]
                                    for chain in break_dict.keys():
                                        # Finding missing ints from residue number ilst
                                        values_str = ''.join(str(break_dict[chain]))
                                        missing_Res.append(str(chain+':'+values_str))
                                    # missing_Res.append('\n'.join([str(j)+' '+str(filename)+missing_Res+'\n']) 
                                    for  item in missing_Res:
                                        uf.write(item+'\n')
                                    uf.close()    
                                print(j,str(filename),"Chain Break")            
                                # break                 


