Aim:To write a Python program to implement the re (Regular Expression) module.

Algorithm:
  
Code:
import re

text = "Python is easy. Python is powerful."

# Search
print("Search:", re.search("Python", text).group())

# Find all
print("Find All:", re.findall("Python", text))

# Replace
print("Replace:", re.sub("Python", "Java", text))

# Split
print("Split:", re.split(" ", text))

# Match
print("Match:", re.match("Python", text).group())


Output:
Search: Python
Find All: ['Python', 'Python']
Replace: Java programming is easy. Java is powerful.
Split: ['Python', 'programming', 'is', 'easy.', 'Python', 'is', 'powerful.']
Match: Python

Result: Result: Thus, the re module functions such as search(), findall(), sub(), split() and match() were implemented successfully in Python.
