#/scratch/madhu/Harshit/scoring/7.5_Data_NR30/7.5_nr30_clean.npz

import numpy as np
import pickle

#loaded = np.load("/scratch/madhu/kritika/Depth/compressd_nbrs/9_03_5A_rnbrs_clean.npz", allow_pickle=True)

with open('./6.5A_rnbrs_Depths_no_hist_8-4_Dict.pickle', 'rb') as f:
    D = pickle.load(f)
print("This is the number of unique nbrs that are enriched by at least 20 in the radial_nbrDATASET:",len(D))

def decomp_dict(Dict):
    Decomp = {}
    for key, value in Dict.items():
        if np.isnan(value).any():
            print(key,value)
        #print(key,value)
        if len(key) <= 2:
            Decomp[key] = value
        if len(key) > 2:
            first_element = key[0]
            for i in range(len(key) - 2):
                new_key = (first_element,) + key[i+1:i+3]
                if new_key in Decomp:
                    for v in value:
                        Decomp[new_key]=np.append(Decomp[new_key],v)
                else:
                    Decomp[new_key] = value
        if len(key) > 3:
            first_element = key[0]
            for i in range(len(key) - 3):
                new_key = (first_element,) + key[i+1:i+4]
                if new_key in Decomp:
                    for v in value:
                        Decomp[new_key]=np.append(Decomp[new_key],v)
                else:
                    Decomp[new_key] = value        
        if len(key) > 4:
            for i in range(len(key) - 4):
                new_key = (first_element,) + key[i+1:i+5]
                if new_key in Decomp:
                    for v in value:
                        Decomp[new_key]=np.append(Decomp[new_key],v)
                else:
                    Decomp[new_key] = value
        if len(key) > 5:
            for j in range(len(key) - 5):
                new_key = (first_element,) + key[j+1:j+6]
                if new_key in Decomp:
                    for v in value:
                        Decomp[new_key]=np.append(Decomp[new_key],v)
                else:
                    Decomp[new_key] = value
        if len(key) > 6:
            for i in range(len(key) - 6):
                new_key = (first_element,) + key[i+1:i+7]
                if new_key in Decomp:
                    for v in value:
                        Decomp[new_key]=np.append(Decomp[new_key],v)
                else:
                    Decomp[new_key] = value
        if len(key) > 7:
            for i in range(len(key) - 7):
                new_key = (first_element,) + key[i+1:i+8]
                if new_key in Decomp:
                    for v in value:
                        Decomp[new_key]=np.append(Decomp[new_key],v)
                else:
                    Decomp[new_key] = value
        if len(key) > 8:
            for i in range(len(key) - 8):
                new_key = (first_element,) + key[i+1:i+9]
                if new_key in Decomp:
                    for v in value:
                        Decomp[new_key]=np.append(Decomp[new_key],v)
                else:
                    Decomp[new_key] = value
        if len(key) > 9:
            for i in range(len(key) - 9):
                new_key = (first_element,) + key[i+1:i+10]
                if new_key in Decomp:
                    for v in value:
                        Decomp[new_key]=np.append(Decomp[new_key],v)
                else:
                    Decomp[new_key] = value
        if len(key) > 10:
            for i in range(len(key) - 10):
                new_key = (first_element,) + key[i+1:i+11]
                if new_key in Decomp:
                    for v in value:
                        Decomp[new_key]=np.append(Decomp[new_key],v)
                else:
                    Decomp[new_key] = value
        if len(key) > 11:
            for i in range(len(key) - 11):
                new_key = (first_element,) + key[i+1:i+12]
                if new_key in Decomp:
                    for v in value:
                        Decomp[new_key]=np.append(Decomp[new_key],v)
                else:
                    Decomp[new_key] = value
        if len(key) > 12:
            for i in range(len(key) - 12):
                new_key = (first_element,) + key[i+1:i+13]
                if new_key in Decomp:
                    for v in value:
                        Decomp[new_key]=np.append(Decomp[new_key],v)
                else:
                    Decomp[new_key] = value
        if len(key) > 13:
            for i in range(len(key) - 13):
                new_key = (first_element,) + key[i+1:i+14]
                if new_key in Decomp:
                    for v in value:
                        Decomp[new_key]=np.append(Decomp[new_key],v)
                else:
                    Decomp[new_key] = value
    return Decomp

Decomped = decomp_dict(D)
print("Lenght of Decomposition:",len(Decomped))

Neigh = {}
np.seterr(all='raise')
for key, value in Decomped.items():
    if len(value)>20:
        try:
            nvalue, bins = np.histogram(value, np.arange(0,15.5,0.5), density = True)
            Neigh[key] = nvalue
        except Exception as e:
            print("Key: ",key," Depths Not coverted to Hist: ",value)


length_counts = {len(key): 0 for key in Neigh.keys()}
for key in Neigh.keys():
    length_counts[len(key)] += 1

for length, count in length_counts.items():
    print("Number of keys with length", length, ":", count)

with open('./Decomp_Hists_07_04_Dict_6.5A.pickle', 'wb') as handle:
    pickle.dump(Neigh, handle, protocol=pickle.HIGHEST_PROTOCOL)

