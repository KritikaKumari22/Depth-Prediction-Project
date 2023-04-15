import pickle

# load the .pickle file
with open('./Decomp_Hists_31bin_07_04_Dict_7.5A.pickle', 'rb') as f:
    data_dict = pickle.load(f)

# access the data from the file
#print(data)
#sorted_dict={}
# sort the dictionary by the highest array value labels first
#data_dict = sorted(data_dict.items(), key=lambda x: max(x[1]))

def sortD(temp):
    temp_list = sorted(list(temp.items()), key=lambda item: sum([int(el==0) for el in item[1]]), reverse=False)
    reordered = {ele[0]: ele[1] for ele in temp_list}
    return reordered

sorted_dict=sortD(data_dict)


# print the sorted dictionary
for label,array in sorted_dict.items():
    if len(label)>2:
        print(array)
        with open('./plot_hists_31bins.txt', 'a+') as fi:
             fi.write(str(label)+':'+str(array)+'\n')
             #fi.write(str(i)+'\n')
		
