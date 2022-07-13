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


## Atoms
- fred-python| BioPython
- x,y,z | atom.coord[0], atom.coord[1], atom.coord[2]:
- model | residue.get_full_id()[1]



fr3d-python reader.py makes cif object of all features, which includes atom objects (Atom defined in fr3d/data/atoms.py) and 
[PDB and mmCIF corresponding tags](https://mmcif.wwpdb.org/docs/pdb_to_pdbx_correspondences.html) 
