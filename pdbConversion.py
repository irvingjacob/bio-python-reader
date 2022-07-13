from email import header
from Bio.PDB import PDBParser
from Bio.PDB.PDBParser import PDBParser

# import necessary fr3d classes
from fr3d.data import Atom
from fr3d.data import Component
from fr3d.data import Structure

import sys


# reading in PDB file
p = PDBParser(PERMISSIVE=1)
structure = p.get_structure("X", "Top Model_11nt_GAAA.pdb")
                            # What the file will be referred to as, file name (must be in root dir)

print(structure.header)
#
if not structure.header['name']:
    structure.header['name'] = "UNNAMED"
    name = "UNNAMED"
else: 
    name = structure.haeder['name']


# Create dictionaries with structure header info
# for model in structure:
#     for chain in model:
#         for residue in chain:
#             for atom in residue:
#                 print(atom.__dict__)

atoms = []     
for model in structure:
    for chain in model:
        for residue in chain:
            full_id = residue.get_full_id()
            print(full_id)
            ins_code = full_id[3][2]
            if ins_code == " ":
                ins_code = None
            for atom in residue:
                x = atom.coord[0]
                y = atom.coord[1]
                z = atom.coord[2]
                pdb=full_id[0]
                this_model = full_id[1]
                this_chain = full_id[2]
                component_number = full_id[3][1]
                alt_id = atom.get_altloc()
                print(alt_id)
                atoms.append(Atom(x=x, y=y, z=z,
                    pdb=name,
                    model=this_model,
                    chain=this_chain,
                    component_id=residue.get_resname(),
                    component_number=component_number,
                    component_index=None,
                    insertion_code=ins_code,
                    alt_id= alt_id,
                    group=None,
                    type=None,
                    name=atom.get_name(),
                    symmetry=None,
                    polymeric=False))
print(atoms)
"""
full_id = residue.get_full_id()
 print(full_id)
("1abc", 0, "A", ("", 10, "A"))
This corresponds to:

The Structure with id "1abc"
The Model with id 0
The Chain with id "A"
The Residue with id ("", 10, "A")

The Residue id indicates that the residue is not a hetero-residue (nor a water) because it has a blank hetero field, that its sequence identifier is 10 and that its insertion code is "A"."""
                # print(residue.icode)
                #print(z,y,z,name,models,chains)
                # atoms.append(Atom(x=atom.coord[0], y=atom.coords['y'], z=atoms.coord['z'],
                #     pdb=self.pdb,
                #     model=self.model,
                #     chain=self.chain,
                #     component_id=self.component_id,
                #     component_number=self.component_number,
                #     component_index=self.component_index,
                #     insertion_code=self.insertion_code,
                #     alt_id=self.alt_id,
                #     group=self.group,
                #     type=self.type,
                #     name=self.name,
                #     symmetry=self.symmetry,
                #     polymeric=self.polymeric))
