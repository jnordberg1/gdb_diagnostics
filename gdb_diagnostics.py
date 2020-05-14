# -*- coding: utf-8 -*-
"""
Created on Thu May 07 10:35:56 2020

@author: JacobNordberg
"""

from os import listdir
from os.path import isfile, join

computer_name      = {
        'MN20170811A': 'Malika',
        'MN20160330A': 'Erich',
        'MN20190226A': 'Nicholas',
        'MN20170810A': 'Jacob'
        }

def diagnose_gdb(stateChoice):
    #gdb = r"D:\Data\State\{}\{}.gdb".format(stateChoice, stateChoice)
    gdb = r"C:\USS\United States Solar Corporation\Site Selection - Documents\Data\State\{}\{}.gdb".format(stateChoice, stateChoice)
    
    onlyfiles = [f for f in listdir(gdb) if isfile(join(gdb, f))]
    
    for a in onlyfiles:
        if "-" in a:
            name = a.split('-')[1]
            print "{} is a duplicated file from {}'s computer".format(a, computer_name.get(name))
            break
    else:
        print "The {} database is clean".format(stateChoice)
        
diagnose_gdb("PA")