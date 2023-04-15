import pickle

# load the .pickle file
with open('/scratch/madhu/kritika/Depth/scoring_nbrs/DecompDict_06_04_6A_Dict.pickle', 'rb') as f:
    data_dict = pickle.load(f)

# access the data from the file
#print(type(data_dict))
#sorted_dict = {}
#sort the dictionary by the highest array value labels first
#data_dict = sorted(data_dict.items(), key=lambda x: max(x[1]))


def sortD(temp):
    temp_list = sorted(list(temp.items()), key = lambda key : len(key[0]),reverse=True)
    reordered = {ele[0] : ele[1]  for ele in temp_list}
    return reordered

sort_data_dict = sortD(data_dict)


# print the sorted dictionary
for label, array in sort_data_dict.items():
    #if len(label)>3:
        #print(label)
    with open('/scratch/madhu/kritika/Depth/scoring_nbrs/6_All_nbrs_06_04.txt', 'a+') as fi:
        fi.write(str(label)+'\n')
    if len(label)==4:
        #print(label)
        with open('/scratch/madhu/kritika/Depth/scoring_nbrs/6_len_3.txt', 'a+') as fi:
            fi.write(str(label)+'\n')
            #fi.write(str(label)+':'+str(array)+'\n')
        #continue
    if len(label)==5:
        with open('/scratch/madhu/kritika/Depth/scoring_nbrs/6_len_4.txt','a+') as fu:
            fu.write(str(label)+'\n') 
    elif len(label)==6:
        with open('/scratch/madhu/kritika/Depth/scoring_nbrs/6_len_5.txt','a+') as fu:
            fu.write(str(label)+'\n') 
    elif len(label)==7:
        with open('/scratch/madhu/kritika/Depth/scoring_nbrs/6_len_6.txt','a+') as fu:
            fu.write(str(label)+'\n') 
    elif len(label)==8:
        with open('/scratch/madhu/kritika/Depth/scoring_nbrs/6_len_7.txt','a+') as fu:
            fu.write(str(label)+'\n') 		
