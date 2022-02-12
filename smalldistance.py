# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 20:23:06 2022

@author: olivi
"""

import random

result = 0

for i in range(1000000):
    X = random.uniform(0.0, 1.0)
    Y = random.uniform(0.0, 1.0)
    if abs(X - Y) <= 0.2:
        result += 1

print(result / 1000000)
    