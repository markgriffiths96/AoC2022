# Advent of Code 2022 - Day 3

import string

file1 = open('day3.txt', 'r')
backpacks = file1.readlines()

# Part 1

backpacks_split = []
dupes = []
score = 0

for i in range(len(backpacks)):
    backpacks[i] = backpacks[i].rstrip()
    size = int((len(backpacks[i])/2))
    backpacks_split.append([backpacks[i][j:j+size] for j in range(0, len(backpacks[i]), size)])
    
    dupes.append(''.join(set(backpacks_split[i][0]).intersection(backpacks_split[i][1])))
    
    if dupes[i].isupper():
        score += string.ascii_uppercase.index(dupes[i]) + 27
    
    else: score += string.ascii_lowercase.index(dupes[i]) + 1
    
print("The sum of the priorities of duplicated items is",score)


# Part 2

group_size = 3
badges = []
badges_score = 0
i = 0

while i < len(backpacks):
    badges_temp = (''.join(set(backpacks[i]).intersection(backpacks[i+1])))
    for j in range(group_size-2): badges_temp = (''.join(set(badges_temp).intersection(backpacks[i+j+2])))
    i += group_size
    badges.append(badges_temp)
    
for i in range(len(badges)):
    if badges[i].isupper():
        badges_score += string.ascii_uppercase.index(badges[i]) + 27
    
    else: badges_score += string.ascii_lowercase.index(badges[i]) + 1
    
print("The sum of the priorities of badges is",badges_score)
