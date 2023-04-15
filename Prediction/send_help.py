import os
import sys
import glob
import numpy as np
from sklearn.neighbors import NearestNeighbors


def read_pdb_files(pdb_file): # reads ATOM lines from pdb file
    with open(pdb_file) as inf:
        return [x for x in inf.readlines() if x.startswith('ATOM')]

def find_sequence(ATOM_lines): # find sequence of a given PDB ATOM lines
    # Make red_dict        
    # Supported aa dict (add entry to support non standard aa)
    single_res = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
         'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
         'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
         'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

    chain_dict = {}
    # Emtpy dictionanries
    for line in ATOM_lines:
        if line[21:22].strip() not in chain_dict.keys():
            chain_dict[line[21:22].strip()] = {}

        if line[22:26].strip() not in chain_dict[line[21:22].strip()].keys():
            chain_dict[line[21:22].strip()][line[22:26].strip()] = []
        if line[17:20] in single_res.keys():
            chain_dict[line[21:22].strip()][line[22:26].strip()]=single_res[line[17:20]]

    # parsing in to dictionaries
    chain_dict = dict([(chain,dict(sorted([(int(res),chain_dict[chain][res]) for res in chain_dict[chain]]))) for chain in chain_dict])
    #chain_seq_dict = dict([(chain,''.join([res[1] for res in chain_dict[chain]])) for chain in chain_dict])        
    return chain_dict

def chain_dict_to_chain_sequence_dict(chain_dict):
    chain_seq_dict = dict([(chain,''.join(chain_dict[chain].values())) for chain in chain_dict]) 
#         chain_seq_dict = dict([(chain,''.join([res[1] for res in chain_dict[chain]])) for chain in chain_dict])        
    return chain_seq_dict

def write_file(file_name,lines): #Documentation: Duh
    with open(file_name,'w') as ouf:
        ouf.writelines(lines)
        
def read_file(file_name): #Documentation: Duh
    with open(file_name) as inf:
        return inf.readlines()
        
def get_ali_lines(chain_dict,seq = '',name = 'SEQ',mutation=False,line_len = 75):
    #USAGE
    #default                   : get_ali_lines(chain_dict)
    #To use a sequence as input: get_ali_lines(None,sequence)
    # Optional Parameters:
    # seq         : Takes in a string. If True ignores input of chain_dict and uses this sequence as sequence.
    # mutation    : format [chain,residue number,ending mutation] eg for a seq = ABC in chain a mutation = ['a',1,X] gives XBC. Ignored if seq is True.
    # line_len    : Specify length of sequnece in each line_len. Takes in interger.
    # name        : specify name of sequence. Takes in string.    
    
    # chain dict analysis only if seq not provided
    if not seq:
        # Mutating chain        
        new_chain_dict = {}
        for chain in chain_dict:
            new_chain_dict[chain] = chain_dict[chain]

        if mutation: # Make false for wild type
            new_chain_dict[mutation[0]][mutation[1]] = mutation[2]

        # sequence of new chain
        seq = ''
        chain_seq_dict = chain_dict_to_chain_sequence_dict(new_chain_dict)
        # adding seq with / at break
        new_chain = False
        for chain in chain_seq_dict:
            if new_chain:
                seq+='/'
            seq+=chain_seq_dict[chain]
            new_chain = True

    outlines = []
    outlines.append('>P1;{}\n'.format(name))
    outlines.append('sequence:{}:::::::0.00: 0.00\n'.format(name))

    n = 0
    line = ''
    for i in seq:
        n += 1
        line += i
        if n == line_len:                        
            outlines.append(line+'\n')
            line = ''
            n=0
    outlines.append(line+'*'+'\n')

    return outlines

def ali_to_seq(ali_lines):
    seq = ''.join([x.strip() for x in ali_lines[2:]])
    return seq

def save_obj(obj,file_name):
    import json
    with open(file_name,'w') as ouf:
        json.dump(obj,ouf)   

def load_obj(file_name):
    import json
    with open(file_name,'r') as inf:
        return json.load(inf)
        
def filter_pdb_based_on_atom_name(atom,pdb_lines):
    return [x for x in pdb_lines if x[12:16].strip() == atom.strip()]
    
def read_pdb_files_with_hetatm(pdb_file): # reads ATOM lines from pdb file
    with open(pdb_file) as inf:
        return [x for x in inf.readlines() if x.startswith('ATOM') or x.startswith('HETATM')]
        
def atom_lines_to_cords(pdb): # parse atom lines in to list of cordinate tuples
    return [(float(line[30:38]),float(line[38:46]),float(line[46:54])) for line in pdb]
    
def get_res_pdb_dict(pdb_lines):
        # returns dict in the form {resid:{ATOM_name:pdb_lines}}
    res_pdb_dict = {}
    for line in pdb_lines:
        res = line[21:26]
        atom = line[12:16].strip()
        if res in res_pdb_dict.keys():
            res_pdb_dict[res][atom] = line
        else:
            res_pdb_dict[res] = {}
            res_pdb_dict[res][atom] = line
    return res_pdb_dict

three_letter_code_dict = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K', 
                          'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
                          'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
                          'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}


def read_pdb(filename):
    with open(filename) as inf:
        return [x for x in inf.readlines() if x.startswith('ATOM')]


def gen_res_dict(pdblines):
    res_dict = {}
    for x in pdblines:
        if x.split()[4][0] == 'A':
            resid = (x[23:26])
            if resid in res_dict:
                res_dict[resid].append(x)
            else:
                res_dict[resid] = [x]

    return res_dict


def get_data(Dict): #Gets the 'CB' atom coordinates for each residue unless no 'CB' for Gly -> 'CA' is taken instead
    L = []
    for key,value in Dict.items():
        flag = True
        # print(key)
        for i in value:
            if i.split()[2] == 'CA':
                flag = False                                                 # Flag remains False until no 'CB' is not found
                split = i
            elif i.split()[2] == 'CB':
                flag = True                                                  # Flag switched to True as soon as 'CB' for the res is encountered
                L.append([i[17:20],i[30:38],i[38:46],i[46:54],i[60:66]])
                break
        if flag == False:                                                   #Write 'CA' coordinates only if Flag was not switched to 'CB'
            L.append([split[17:20],split[30:38],split[38:46],split[46:54],split[60:66]])   
    return L



def neighbors(values, r):
    # Find nearest neighbors of each residue
    coords = np.array(values)[:,1:4].astype(float)
    
    nbrs = NearestNeighbors(radius=r, algorithm='kd_tree').fit(coords)
    
    # Get indices and distances of neighbors within radius r
    distances, indices = nbrs.radius_neighbors(coords)
   
    indices = [ind[np.argsort(dist)] for ind, dist in zip(indices, distances)]
    # distances = [dist[np.argsort(dist)] for dist in distances]
    # return indices, distances
    return indices

def yeet(indices):
#Remove n-i and n+i from the neighbourhood

    newstars=[]
    for star in indices:
        cres=star[0]
        for other in star[1:]:     #everything but the centre
            if abs(cres-other)<2:
                star = np.delete(star,np.where(star == other))
            else:
                pass
        newstars.append(star)
    return np.array(newstars,dtype = object)


def add_depth(values,newstars): #yeet is newstars

    f = []
    for i in range(len(newstars)):
        r = values[newstars[i],0]
        d = values[i,4]
        f1 = np.append(r,d)
        f.append(f1)
    return np.array(f,dtype=object)