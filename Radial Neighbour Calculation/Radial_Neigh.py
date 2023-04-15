import os
import sys
import glob
import numpy as np
from sklearn.neighbors import NearestNeighbors

def read_pdb(filename):
    with open(filename) as inf:
        return [x for x in inf.readlines() if x.startswith('ATOM')]


def gen_res_dict(pdblines):
    res_dict = {}
    for x in pdblines:
        # if x.split()[4][0] == 'A': #Just Using A chain, so only 1 model is being Used?
        resid = (x[22:26].strip())
        if resid in res_dict:
            res_dict[resid].append(x) #Appending or putting the whole PDB line related to the residue "resid"
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
    distances = [dist[np.argsort(dist)] for dist in distances]
    return indices, distances


def yeet(indices, distances):

    newstars = []
    new_dists = []
    for star, far in zip(indices, distances):
        indices_to_remove = []
        for i in range(1, len(star)):
            if abs(star[0] - star[i]) < 2:
                indices_to_remove.append(i)
        star = np.delete(star, indices_to_remove)
        far = np.delete(far, indices_to_remove)
        newstars.append(star)
        new_dists.append(far)
    return np.array(newstars, dtype=object), np.array(new_dists, dtype=object)
            

def add_depth(values,newstars): #yeet is newstars

    f = []
    for i in range(len(newstars)):
        r = values[newstars[i].astype(int),0]
        d = values[i,4].strip()
        f1 = np.append(r,d)
        f.append(f1)
    return np.array(f,dtype=object)

name = sys.argv[1]
pdblines = read_pdb(name)
res_dict = gen_res_dict(pdblines)
values = get_data(res_dict)
values = np.array(values)
indices, distances = neighbors(values,7.5)
newstars,new_dists = yeet(indices, distances)
data = add_depth(values,newstars)

outfile = name.split('/')[-1]
np.savez_compressed('/scratch/madhu/kritika/Depth/radial_nbrDATASET/%s'%outfile,x = (data,new_dists))
