# import os
import sys
# import re

File1= sys.argv[1]
File2=sys.argv[2]
File_1not_in_2= "./In_"+str(File1)+"_but_not_in"+str(File2)+".txt"
File_2not_in_1= "./In_"+str(File2)+"_but_not_in"+str(File1)+".txt"

# Notclean_original_list = "C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/Final Lists/Notclean_original.txt"

# Originally_clean_pdbs= "C:/Users/Kritika Kumari/Desktop/Project Madhu/Sem8/Mys/filtering PDBs/Final Lists/Originally_clean_pdbs_NR30.txt"

File1_list=[]
with open(File1,'r') as inf:
            lines = [x for x in inf.readlines()]

            for k in lines:
                k=str(k)
                # if len(k.split(' ')) >= 2:
                #     line=k.split(' ')
                #     dir= line[1]
                # if k.startswith('/scratch/madhu/kritika/'):
                File1_list.append(k)

File2_list=[]
with open(File2,'r') as inf:
            lines = [x for x in inf.readlines()]

            for k in lines:
                k=str(k)
                # if len(k.split(' ')) >= 2:
                #     line=k.split(' ')
                #     dir= line[1]
                # if k.startswith('/scratch/madhu/kritika/'):
                File2_list.append(k)

for j in File1_list:
    if j not in File2_list:
        with open(File_1not_in_2 ,'a+') as gf:
            gf.write(j)


for k in File2_list:
    if k not in File1_list:
        with open(File_2not_in_1 ,'a+') as f:
            f.write(k)


# for j in got_detailed_pdbs[:-1]:
#     with open(All_broken_PDBS,'a+') as gf:
#         gf.write(j)
# for j in got_detailed_pdbs[-1]:
#     with open(All_broken_PDBS,'a+') as gf:
#         gf.write(j.rstrip())





# got_detailed_pdbs=[]
# with open(All_broken_PDBS,'r') as inf:
#             lines = [x for x in inf.readlines()]

#             for k in lines:
#                 got_detailed_pdbs.append(k)

# pdbs=[]
# with open(UNK_results,'r') as inf:
#             lines = [x for x in inf.readlines() if x[0].isdigit()]

#             for k in lines:
#                 k=str(k)
#                 if len(k.split(' ')) >= 2:
#                     line=k.split(' ')
#                     dir= line[1]
#                     if dir.startswith('/scratch/'):
#                         pdbs.append(dir)


# for i in pdbs:
#     if i in got_detailed_pdbs:
#         with open(Extra_filepath,'a+') as uf:
#                 uf.write(i)

# for j in pdbs:
#     if j not in got_detailed_pdbs:
#         with open(Not_broken_filepath,'a+') as gf:
#                 gf.write(j)



