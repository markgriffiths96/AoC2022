# Advent of Code 2022 - Day 2

file1 = open('day2.txt', 'r')
rounds = file1.readlines()

for i in range(len(rounds)): rounds[i] = rounds[i].split(" ")

# Part One

score = 0

for i in rounds:
    if i[1].rstrip() == "X":
        score += 1
        if i[0]  == "A": score += 3
        elif i[0]  == "B": score += 0
        elif i[0]  == "C": score += 6
    elif i[1].rstrip() == "Y":
        score += 2
        if i[0]  == "A": score += 6
        elif i[0]  == "B": score += 3
        elif i[0]  == "C": score += 0    
    elif i[1].rstrip() == "Z":
        score += 3
        if i[0] == "A": score += 0
        elif i[0] == "B": score += 6
        elif i[0] == "C": score += 3
        
print("Total score according to the strategy guide is:",score)

score = 0

# Part Two
for i in rounds:
    if i[1].rstrip() == "X":
        if i[0]  == "A": score += 3
        elif i[0]  == "B": score += 1
        elif i[0]  == "C": score += 2
    elif i[1].rstrip() == "Y":
        score += 3
        if i[0]  == "A": score += 1
        elif i[0]  == "B": score += 2
        elif i[0]  == "C": score += 3   
    elif i[1].rstrip() == "Z":
        score += 6
        if i[0] == "A": score += 2
        elif i[0] == "B": score += 3
        elif i[0] == "C": score += 1

print("Total score according to the updated strategy guide is:",score)

    
