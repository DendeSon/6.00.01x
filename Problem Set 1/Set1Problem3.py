"""
Objective: Find the longest substring in alphabetical order in string, 's'.
's' is given by the grader.
Letters are added into the 'longest' string and appended to 'hold' once an 
earlier letter is found. 
Prints out the longest substring in alphabetical order, 'hold'.
"""

hold =[]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= s[i - 1]:
        longest += s[i]
    if s[i] < s[i - 1]:
        hold.append(longest)
        longest = s[i]
hold.append(longest)
    
print("Longest substring in alphabetical order is: " + max(hold, key=len))