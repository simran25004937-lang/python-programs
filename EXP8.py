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
