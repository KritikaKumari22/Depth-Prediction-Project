import numpy as np
import pickle

loaded = np.load("/scratch/madhu/kritika/Depth/compressd_nbrs/6.5A_16-17_03/6.5A_rnbrs_17_03_clean.npz", allow_pickle=True)

D = loaded['x']

temp = {}

for i in D:
    v=i[-1]
    if v== 'nan':
            print("NAN!")
    else:
        try:
            temp[tuple(i)[:-1]].append(v.astype(float))
        except:
            temp[tuple(i)[:-1]] = [v.astype(float)]
# for i in temp:
#     print(i)
print("Length of Temp or Number of Unique Nbrs of any length, unenriched",len(temp))



def sortD(temp):    
    temp_list = sorted(list(temp.items()), key = lambda key : len(key[0]),reverse=True)
    reordered = {ele[0] : ele[1]  for ele in temp_list}
    return reordered

reordered = sortD(temp)


def r_keys(tempR,d):
    for key in tempR:
        if key in d:
            del d[key]


'''def decomp_dict(Dict):
    Decomp = {}
    for key,value in Dict.items():
        if len(key)>4:
            N = key[:5]
            if N in Decomp:
                for v in value:
                    Decomp[N].append(v)
            else:
                Decomp[N] = value
                
    return Decomp

Decomp = decomp_dict(reordered)
print("Length of Decomposition:",len(Decomp))'''

Neigh = {}
tempR = []
tempN = reordered
print("Length of Temp",len(tempN))
while len(tempN) != 0:    
    r_keys(tempR,reordered)
    reordered.update(tempN)
    sortD(reordered)
    tempR = []
    tempN = {}
    np.seterr(all='raise')
    for key, value in reordered.items():
        if len(value)>20:
            try:
                #nvalue, bins = np.histogram(value, np.arange(0,15.5,0.5), density = True)
                Neigh[key] = value
            except Exception as e:
                print("Key: ",key," Depths Not coverted to Hist: ",value)
        elif len(key)>4: #Now consider decomposition till 3 residue neighbourhood whcih can be exhausted easily.
            if key[:-1] in reordered:
                tempR.append(key)
                for v in value:
                    reordered[key[:-1]].append(v)
            else:
                tempR.append(key)
                try:
                    for v in value:
                        tempN[key[:-1]].append(v.astype(float))
                except:
                    tempN[key[:-1]] = value



length_counts = {len(key): 0 for key in Neigh.keys()}
for key in Neigh.keys():
    length_counts[len(key)] += 1

for length, count in length_counts.items():
    print("Number of keys with length", length, ":", count)

with open('./6.5A_rnbrs_Depths_no_hist_8-4_Dict.pickle', 'wb') as handle:
    pickle.dump(Neigh, handle, protocol=pickle.HIGHEST_PROTOCOL)
