from Bio.PDB import PDBParser
import xpdb  # this is the module described below

# read
p = PDBParser()
structure = p.get_structure("X", "Top Model_11nt_GAAA.pdb")
for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:
                print(atom)