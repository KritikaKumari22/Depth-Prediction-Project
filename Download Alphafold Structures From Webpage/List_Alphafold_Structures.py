import os
import sys

pdbs=[]
path = sys.argv[1]
list = sys.argv[2]
i=0
j=0
for filename in os.listdir(path):
          if filename.endswith('.pdb'):
            with open(list,'a+') as f:
                f.write(str(filename)+'\n')                    
                

