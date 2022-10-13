# Mutate Lipids Pipe Line

## Pipeline designed for taking a charmm structure and prepping it for gromacs.

This is a pipeline and ''hack'' to build mutated lipids for molecular dynamics simulations. This should be used as a last resort. Mutate is modified from [Klauda Lab](https://user.eng.umd.edu/~jbklauda/wiki/doku.php?id=mutating_a_lipid). MDP files are CHARMM-GUI standard. Charmm is Charmm36

- Assumption 1: You have the structure/param.... files for your system and lipid you want to make
  - topol.str and toppar are included in directory
- Assumption 2: You are running python 3+
- Assumption 3: You have gotten the gromacs .top and/or .itp file for mutated lipid
  - If Assumption 3 does not hold 
    - CHARMM-GUI can convert some topologies, issues have arrisen for full system
    -  VMD's topo gmxwriter can give you a starting topology and itp file, please use at your own risk.
- Assumption 4: you have installed CHARMM





1) Open mutate.inp. 
2) The line that read ```open read unit 1 card name <filename> ``` add your coordinate file ```<.crd>``` . It may be easiest to use a system that has been solvated.
3) The line: ```! Change name of residues to be mutated``` fill in ```rename resname <NEW NAME> select resname <OLD NAME> end```. 
4) Under the line ```! Rename atoms ``` define the atoms you are renaming or moving. Ex: ```rename atom <OLD Atom> select resname <NEW NAME>  .and. (type <NEW atom>) end```
5)  At the end of the file, you will see ```open write unit 2 card name <filename> ``` and ```write coor card unit2 / write psf card unit 2 /  write coor unit 2 pdb``` . For each file output input a file name 
6) In terminal: run the command  ``` charmm <mutate.inp> mutate.out```, and let run.
7) With your new pdb file ```python addCrystlPdb.py -i <filename.pdb> -cryst x y z a b c``` where x y z are the periodic bounds and a b c are the angles of the box/rectangle...
8) Finally run, ```python top_parser.py <filename.pdb> ``` This will build a gromacs top file used for your simulations. _Warning_ updates are required, such as a lipid input argument parser and should only be used for lipids currently! Please update itps and lipids as you need. 

