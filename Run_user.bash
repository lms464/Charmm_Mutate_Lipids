#!/bin/bash

MUTDIR="/home/liam/Censere/github/Mutate_Lipids"

WRKDIR=$1
LIP=$2

ref_txt="mut"
inpt="step5_assembly.crd"
# inpt="step4_lipid.crd"

cp ${WRKDIR}/${inpt} ./

# USER- KEEP mutate_user.inp
# This file will can be used again and again
# and upated to deal with more lipids
# @Liam, set it up to fill in the atoms
# from a spread sheet or somethign?

cp mutate_user.inp mutate.inp
sed -i "s/\#NAME/${LIP}/g" mutate.inp

charmm <mutate.inp> mut.out
#python addCrystPdb.py -i ${ref_txt}.pdb -cryst 175 175 85 90 90 90
rm mutate.inp
python top_parser.py ${ref_txt}.pdb ${LIP}

cp ${ref_txt}.pdb topol2.top ${WRKDIR}/gromacs
cp -r MDP ${WRKDIR}/gromacs
cp DVPC.itp PVPC.itp ${WRKDIR}/gromacs/toppar

