# -*- coding: utf-8 -*-
"""
@author: JacobNordberg
"""

from os import listdir
from os.path import isfile, join

stateChoice = "ME"

computer_name      = {
        'MN20170811A': 'Malika',
        'MN20160330A': 'Erich',
        'MN20190226A': 'Nicholas',
        'LAPTOP-61LLEIFE': 'Jacob'
        }

#gdb = r"D:\Data\State\{}\{}.gdb".format(stateChoice, stateChoice)
gdb = r"C:\USS\United States Solar Corporation\Site Selection - Documents\Data\State\{}\{}.gdb".format(stateChoice, stateChoice)

onlyfiles = [f for f in listdir(gdb) if isfile(join(gdb, f))]

for a in onlyfiles:
    if a.endswith(".sr.lock"):
        name = a.split('.')[1]
        print "{} is in the database".format(computer_name.get(name))
        break
else:
    print "The {} database is clear".format(stateChoice)
