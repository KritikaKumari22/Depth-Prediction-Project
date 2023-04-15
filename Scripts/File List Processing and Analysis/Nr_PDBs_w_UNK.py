import os
# import sys
# %matplotlib inline
# import matplotlib
# import numpy as np
# import matplotlib.pyplot as plt

PDB_nrs= 0
path = "C://Users//Kritika Kumari//Desktop//Project Madhu//Sem8//Mys//"
for filename in os.listdir(path):
      if filename.endswith('.pdb'):
        # print(filename)
        infile= ''
        with open(filename) as inf:
            ensemble_lines = inf.readlines()
            # for y in ensemble_lines:
            n=0
            while not infile:
                if ensemble_lines[n][17:20] == 'UNK':
                    PDB_nrs+=1
                    infile=str(filename)
                    print(infile)
                    break
                    # with open('Ptoremove.txt','w') as ouf:
                    #     ouf.writelines(str(infile))
                    # break
                n=+1

            # print(ensemble_lines)
n = 0
# while n in range(0,len(ensemble_lines)):
#     if ensemble_lines[n][17:20] == 'UNK':
#         PDB_nrs+=1
#         break
#     n=+1
# with open('Ptoremove.txt','w') as ouf:
            # ouf.writelines(str(infile))
    
        # for ensemble_lines in inf.readlines():
        #             if ensemble_lines[17:20] == 'UNK':
        #                 PDB_nrs+=1
        #                 print(PDB_nrs)
        #                 with open('Ptoremove.txt','w') as ouf:
        #                         ouf.writelines(str(infile))



# # infile = sys.argv[1]
# with open(infile) as inf:
#     ensemble_lines = inf.readlines()

# res_ids = ''
# n = 0

# if ensemble_lines[n][17:20] == 'UNK':
#        PDB_nrs+=1

# with open('PDBids_toremove.txt','w') as ouf:
#     ouf.writelines(str(infile))
#     ouf.close()






















# SMALL_SIZE = 10
# MEDIUM_SIZE = 16
# BIGGER_SIZE = 18

# csfont = {'fontname':'sans-serif'}
# hfont = {'fontname':'serif'}
# plt.rcParams.update({'font.family':'serif'})
# plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
# plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
# plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
# plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
# plt.rc('legend', fontsize=13)


# xAxis=np.arange(len(PDB_nrs))
# plt.figure(figsize=(15,3))
# plt.plot(xAxis,PDB_nrs, color='black')
# plt.savefig(results_dir +str(runnum)+ 'Intermittent Input.png',dpi=120)
# plt.show()
    


