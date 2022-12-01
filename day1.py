# Advent of Code 2022 - Day 1

file1 = open('day1.txt', 'r')
lines = file1.readlines()

calories_temp = 0 
calories = []

for i in lines:
    if len(i.strip()) != 0: calories_temp += float(i)
    elif len(i.strip()) == 0:
        calories.append(calories_temp)
        calories_temp = 0
        
print("The elf with the most calories has",max(calories),"calories in total.")
        
print("The total calories of the three elves with the most calories is",sum(sorted(calories, reverse=True)[:3]), "calories.")