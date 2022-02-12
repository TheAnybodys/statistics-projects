# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:10:12 2022

@author: olivi
"""

import random

three_colors_replacement = 0
red_and_white_replacement = 0
three_colors_noreplacement = 0
red_and_white_noreplacement = 0


# all three colors with replacement
for i in range(1000000):
    red = 0
    green = 0
    white = 0
    for j in range(3):
        ball_1 = random.randint(1, 9)
        if 1 <= ball_1 <= 3:
            red += 1
        if 4 <= ball_1 <= 6:
            green += 1
        if 7 <= ball_1 <= 9:
            white += 1
    if red == 1 and green == 1 and white == 1:
        three_colors_replacement += 1
    
# two white and one red with replacement
for i in range(1000000):
    red = 0
    green = 0
    white = 0
    for j in range(3):
        ball_2 = random.randint(1, 9)
        if 1 <= ball_2 <= 3:
            red += 1
        if 4 <= ball_2 <= 6:
            green += 1
        if 7 <= ball_2 <= 9:
            white += 1
    if red == 1 and white == 2:
        red_and_white_replacement += 1

# all three colors without replacement
for i in range(1000000):
    red = 0
    green = 0
    white = 0
    chosen_balls = []
    for j in range(3):
        ball_3 = random.randint(1, 9)
        while ball_3 in chosen_balls:
            ball_3 = random.randint(1,9)
            continue
        if 1 <= ball_3 <= 3:
            red += 1
        if 4 <= ball_3 <= 6:
            green += 1
        if 7 <= ball_3 <= 9:
            white += 1
        chosen_balls.append(ball_3)
    if red == 1 and green == 1 and white == 1:
        three_colors_noreplacement += 1

# two white and one red without replacement
for i in range(1000000):
    red = 0
    green = 0
    white = 0
    chosen_balls = []
    for j in range(3):
        ball_4 = random.randint(1, 9)
        while ball_4 in chosen_balls:
            ball_4 = random.randint(1,9)
            continue
        if 1 <= ball_4 <= 3:
            red += 1
        if 4 <= ball_4 <= 6:
            green += 1
        if 7 <= ball_4 <= 9:
            white += 1
        chosen_balls.append(ball_4)
    if red == 1 and white == 2:
        red_and_white_noreplacement += 1

print('Prob. we see all 3 colors, sampling w/replacement: ', \
      three_colors_replacement / 1000000)
print('Prob. we see 2 white and 1 red, sampling w/replacement: ', \
      red_and_white_replacement / 1000000)
print('Prob. we see all 3 colors, sampling w/o replacement: ', \
      three_colors_noreplacement / 1000000)
print('Prob. we see 2 white and 1 red, sampling w/o replacement: ', \
      red_and_white_noreplacement / 1000000)