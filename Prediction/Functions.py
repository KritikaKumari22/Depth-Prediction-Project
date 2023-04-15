
def Generate_List():
    from pathlib import Path
    path = Path('Data_Pilot/pdbs_folds/content/Results/')
    i=0
    List = []
    for entry in path.iterdir():
        if entry.name.endswith('-residue.depth'):
            #print(entry.name)
            o = open(entry,'r')
            data = o.readlines()
            l = []
            i=0
            for line in data:
                i=i+1
                s = line.split()
                m = s[0]
                if s[6] == 'nan':
                    s[6] = 0.00
                if m[0] == 'A':
                    l.append(s[2:7:2])
            List.append(l)
    return List

def Fasta_to_AA(seq):
    seq = seq.lower()
    seq = seq.replace('a', "ALA ") 
    seq = seq.replace('b', "ASX ") 
    seq = seq.replace('c', "CYS ") 
    seq = seq.replace('d', "ASP ") 
    seq = seq.replace('e', "GLU ") 
    seq = seq.replace('f', "PHE ") 
    seq = seq.replace('g', "GLY ") 
    seq = seq.replace('h', "HIS ") 
    seq = seq.replace('i', "ILE ") 
    seq = seq.replace('k', "LYS ") 
    seq = seq.replace('l', "LEU ") 
    seq = seq.replace('m', "MET ") 
    seq = seq.replace('n', "ASN ") 
    seq = seq.replace('p', "PRO ") 
    seq = seq.replace('q', "GLN ") 
    seq = seq.replace('r', "ARG ") 
    seq = seq.replace('s', "SER ") 
    seq = seq.replace('t', "THR ") 
    seq = seq.replace('v', "VAL ") 
    seq = seq.replace('w', "TRP ") 
    seq = seq.replace('x', "XAA ") 
    seq = seq.replace('y', "TYR ") 
    seq = seq.replace('z', "GLX ") 
    return seq.split()


def Inherit(seq, fold, shift):
    if len(seq) <= len(fold):
        i = 0 + shift
        A = []
        for x in seq:
            a = []
            a.append(x)
            a.extend(fold[i])
            A.append(a)
            i = i + 1
            if i == len(fold):
                break
        return A
    else:
        raise ValueError("Invalid input: sequence is longer than fold")
