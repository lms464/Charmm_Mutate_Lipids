import sys
def write_itp(fl):
    
    # TODO build lipid input argument
    # This is a list of itp files for simulation
    itps = ['#include "toppar/forcefield.itp"', '#include "toppar/DPOP.itp"', 
                '#include "toppar/DVPC.itp"',
                '#include "toppar/TIP3.itp"','#include "toppar/CLA.itp"',
                '#include "toppar/SOD.itp"','[ system ]','; Name','Title',
                "[ molecules ]",'; Compound      #mols']
    
    
    fl = open(fl,'r')
    lines = fl.readlines()
    
    # Used tk count and check number of mecules
    res = []
    res_name = 0
    res_name_old = 0
    
    # varriables leftover from different script
    ################
    aa_bool = True
    proa_bool = True
    prob_bool = True
    zma_bool = True
    gpd_bool = True
    nec_bool = True
    ################
    lipids = ["DPOP","DVPC"]
    
    f = open('topol2.top','w')
    
    for i in itps:
        # writes out header
        f.write("%s\n"%i)
    res_out = []
    for li, line in enumerate(lines[1:]):
        res_name = line[17:21]
        # parsed for lipid names
        
        # Used tk sort and check for spcific lipids
        # and solvents/ions
        if li != 0:
            if res_name != res_name_old:
                if len(res) > 0:
                    print("%s \t %i"%(res_name_old,len(res)))
                    f.write("%s \t %i\n"%(res_name_old,len(res)))
                    res = []
                
        if res_name in lipids and line[13:16] == 'P  ':        
            res.append(res_name)
            res_out.append(res_name)

        
        if res_name == 'DPOP' and line[13:15] == 'O3':
                res.append(res_name)
                res_out.append(res_name)
                
        
        if res_name == 'TIP3' and line[13:16] == 'OH2':
                res.append(res_name)
                
        if res_name == 'CLA ' and line[13:16] == "CLA":
                res.append(res_name) 
        
        if res_name == 'SOD ' and line[13:16] == "SOD":
                res.append(res_name) 
        res_name_old = line[17:21]
        
    f.close()   

    print("DPOP: %i"%res_out.count("DPOP"))
    print("DVPC: %i"%res_out.count("DVPC"))



if len(sys.argv) < 2:
    print("wrong inputs number")
write_itp(sys.argv[1])