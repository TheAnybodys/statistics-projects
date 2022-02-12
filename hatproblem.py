# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 18:47:34 2022

@author: olivi
"""

import random

omega = int(input("Number of total people: "))

none_correct = 0

for i in range(1000000):
    chosen_hats = []
    chosen_people = []
    wrong_hat = 0
    for j in range(omega):
        hat = random.randint(1, omega)
        while hat in chosen_hats:
            hat = random.randint(1, omega)
            continue
        person = random.randint(1, omega)
        while person in chosen_people:
            person = random.randint(1, omega)
            continue
        if hat != person:
            wrong_hat += 1
        chosen_hats.append(hat)
        chosen_people.append(person)
    if wrong_hat == omega:
        none_correct += 1

print(none_correct / 1000000)