"""
Objective: Find vowels in a given string, 's'.
's' is given by the grader.
Prints out how many vowels are found in a string, 's'.
"""

vowels = set("aeiou")
x = 0

for letter in s:
    if letter in vowels:
        x += 1

print("Number of vowels: " + str(x))