# Depth-Prediction-Project

## Preface:
The depth of a protein residue measures the degree of burial of a residue from bulk solvent in the folded state of the protein1. The Depth of a protein residue is governed by the folded state of the protein and, therefore, its spatial neighbourhood. The conservation of folds across solved protein structures makes it possible for us to learn this correlation of depth with the protein structure and thereby predict it for any given structure of the protein.

## Aim:
Our aim is to predict the Residue Depth of an unsolved protein sequence, for each of its residues using Threading.

## Methodology:
We aim to do this by correlating the enrichment of depth values of the residue for a given spatial neighbourhood in the NR30 PDB dataset. Based on the enrichment of Depth values of residue in a specific neighbourhood the target sequence protein given a random fold will be assigned a score for the residue in the same specific neighbourhood. Similarly, scores will be assigned to each residue in the sequence and a cumulative score will be generated for the fold it has been given. This will be done across folds got from a fold-set database. The fold with the maximum cumulative depth will be give the prediction of Depth for each of it's residues.

The Dataset used for training the model and generating Depth-of-the-residue-with-specific-neighbourhood Scores is NR30.

The Depth values for the NR30 were calculated using the Depth Server2.

HOMSTRAD database was used to get protein folds.

Previous Results by Harshit

### Refernces
* Tan, K. P., Nguyen, T. B., Patel, S., Varadarajan, R., & Madhusudhan, M. S. (2013). Depth: a web server to compute depth, cavity sizes, detect potential small-molecule ligand-binding cavities and predict the pKa of ionizable residues in proteins.

* Depth Webserver
