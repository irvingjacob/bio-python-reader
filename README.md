# bio-python-reader
Testing of using [BioPython](https://biopython.org/) to read .pdb formatted files

Must have copy of fr3d dirctory from [fr3d-python](https://github.com/BGSU-RNA/fr3d-python) in PYTHON-PATH or have fr3d-python in this directory and run setup.py (Maybe not tested)


## Goal:
read in .pdb files using biopython, convert to a format that can be used by fr3d-python to help fr3d python have functionality for .pdb files and .cif files. 

## pdbConversion.py
pdbConversion.py right now just uses a parser to extract info from a pdb file 
Parsing comes from Bio.PDB import PDBParser 
Use ``` PDBParser().get_structure("x", "XXX.pdb") ```
Unlike fr3d-python, the "x" will set the identifier for the name instead of using the PDB ID. This can be filled easily with the pdb id though. "XXX.pdb" is the name of the .pdb file that will be parsed. PDB file must be located in the same directory as pdbConversion.py (bio-python-reader) directory as of right now to be read in. 

## Notes: 
fr3d-python reader.py reads the following attributes (biopython pdb equivalents in parenthesis): 
- name ()
- operators () => CIF: pdbx_struct_oper_list PDB: 
- assemblies ()
- entities ()
- chemp comp () 

("1abc", 0, "A", ("", 10, "A"))
This corresponds to:

The Structure with id "1abc"
The Model with id 0
The Chain with id "A"
The Residue with id ("", 10, "A")

## Residues
- Full ids can be gathered at the Residue level using ``` residue.get_full_id(). These attributes include Structure, Model, Chain, Residue("Hetero, Water, Other" ,"sequence id","insertion code").

## Atoms
The following attributes for atom objects in fr3d-python correspond to the following in BioPython
- fred-python| BioPython
- x,y,z | atom.coord[0], atom.coord[1], atom.coord[2]
- model | ```residue.get_full_id()[1]```
- chain | ```residue.get_full_id()[2]```
- component_id | ```residue.get_resname()```
- component_number | ```residue.get_full_id()[3][1]```
- component_index | 
- insertion_code | ```residue.get_full_id()```
- alt_id | ```atom.get_altloc()```
- group | 
- type | 
- name | ```atom.get_name()```
- symmetry | 
- polymeric | 

fr3d-python reader.py makes cif object of all features, which includes atom objects (Atom defined in fr3d/data/atoms.py) and 
[PDB and mmCIF corresponding tags](https://mmcif.wwpdb.org/docs/pdb_to_pdbx_correspondences.html) 
