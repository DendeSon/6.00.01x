"""
Objective: Find how many times 'bob' appears in a string, 's'.
's' is given by the grader.
Prints out how many times 'bob' was found in a string, 's'.
"""

b = "bob"
count = 0

for word in range(len(s)):
    if s[word:word + 3] == b:
        count += 1

print("Number of times bob occurs is: " + str(count))