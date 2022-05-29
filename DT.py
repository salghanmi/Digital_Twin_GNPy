#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 
from subprocess import run,PIPE
import re


#cmd_str= "gnpy-transmission-example -v -e eqpt_config.json Inf_Topology_V018.xls trx Node_2 trx Node_3 --show-channels -po=4.5 >> Simulation_Data.txt"


def run_simulation(Power): # Declear 
    
    filename="Simulation_Data.txt"  # Database 
    #command= ["cat",filename]
    #command = cmd_str.split()
    command=["gnpy-transmission-example", "-v", "-e", "eqpt_config.json",  "Inf_Topology_V018.xls" 
    ,"trx DC_Site_A", "trx DC_Site_B", "--show-channels" ,"-po="+str(Power)]

    myoutput = open(filename, 'w')
    output = run(command,stdout=myoutput)
    command= ["cat",filename]
    output = run(command,stdout=PIPE)
    encoding = 'utf-8'
    results=str(output.stdout)

    items=re.findall("Final GSNR.*$",results,re.MULTILINE)
    for x in items:
        line=x
 
    line=line.split()[4]

    GSNR_value=line.partition("\\x1b[1;36;40m")[-1]

    return float(GSNR_value)

Power=0.5 
GSNR= run_simulation(Power)
print("New GSNR: ", GSNR)
print("New launch power: ", Power)

while GSNR < 11:   # 
    Power=Power+1
    GSNR= run_simulation(Power)
    print("New GSNR: ", GSNR)
    print("New launch power: ", Power)
    pass



