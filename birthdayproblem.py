# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 18:23:48 2022

@author: olivi
"""

import random

matches = 0

for i in range(1000000):
    bdays = []
    for j in range(36):
        bday = random.randint(1, 365)
        if bday in bdays:
            matches += 1
            break
        bdays.append(bday)
print(matches / 1000000)