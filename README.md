# Mutate Lipids Pipe Line

## Pipeline designed for taking a charmm lipid structure and moddifying it.

This is a pipeline and ''hack'' to build mutated lipids for molecular dynamics simulations. Mutate is modified from [Klauda Lab](https://user.eng.umd.edu/~jbklauda/wiki/doku.php?id=mutating_a_lipid). MDP files are CHARMM-GUI standard. Charmm is Charmm36

- Assumption 1: You have the structure/param.... files for your system and lipid you want to make
  - TODO add charmm36m toppar file
  - If you are missing the desired parameter, this script will not work!
  - Please consider reading through the exhisting charmm36 lipid options as a starting structure
- Assumption 2: You are running python 3+
  - Pything scripts here are using python 3. Scripts may be modified to run pythong 2 butnit is not advised
- Assumption 3: Before you simulate: you have gotten the gromacs .top and/or .itp file for mutated lipid
  - If Assumption 3 does not hold 
    - CHARMM-GUI can convert topologies (https://www.charmm-gui.org/?doc=input/converter.ffconverter)
      - You will need a psf, charmm crd, and str/rtf files associates with the mutated structure
      - AutoPSF from vmd to genterate a psf file (note the header will need to be replased with and XPLORE header)
      - Please use the script found here to build a charmm crd file: https://www.ks.uiuc.edu/Research/vmd/script_library/scripts/write_charmm_crd/
    -  VMD's topo gmxwriter can give you a starting topology and itp file, but it is not considered safe for simulation .
- Assumption 4: you have installed CHARMM





1) Open mutate.inp. 
2) The line that read ```open read unit 1 card name <filename> ``` add your coordinate file ```<.crd>``` . Please use a system that has been solvated.
3) Under the  line: ```! Change name of residues to be mutated``` fill in ```rename resname <NEW NAME> select resname <OLD NAME> end```. 
4) Under the line ```! Rename atoms ``` define the atoms you are renaming or moving. Ex: ```rename atom <OLD Atom> select resname <NEW NAME>  .and. (type <NEW atom>) end```
  - These NEW atom names should come from your parameter file.
  - It may be the case you need to mosify multiple atoms, this command can be used for each atom your are changing
5)  At the end of the file, you will see ```open write unit 2 card name <filename> ``` and ```write coor card unit2 / write psf card unit 2 /  write coor unit 2 pdb``` . For each file output input a file name 
6) In terminal: run the command  ``` charmm <mutate.inp> mutate.out```, and let run.
7) With your new pdb file ```python addCrystlPdb.py -i <filename.pdb> -cryst x y z a b c``` where x y z are the periodic bounds and a b c are the angles of the box/rectangle... and can be found from your original structure file
  - TODO implent parser 
8) Finally run, ```python top_parser.py <filename.pdb> ``` This will build a gromacs top file used for your simulations. 
  - I have found this process disorders the pdb file, this script builds a nee topology file from thr re-ordered pdb
  - TODO  update itps and lipids as you need. 

