from operator import concat
import re

filePath = r'Tester.csv'
# Note the prefix 'r' indicates "raw string" to ensure '\' is escaped
charToSplitOn = r'\d'

with open(filePath, 'r') as f:
    file_contents = f.read()

words = file_contents.split(charToSplitOn)
print(concat('Count of strings after the split: ', str(len(words))))

# Compile the regular expression pattern
searchPattern = re.compile(charToSplitOn)
matches = searchPattern.finditer(file_contents)
for match in matches:
    print(match)
