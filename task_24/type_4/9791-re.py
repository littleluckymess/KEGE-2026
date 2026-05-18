from re import finditer
with open (r'../files/24_9791.txt') as file:
    data = file.readline()

pattern = '[1-9A-F][0-9A-F]*'

matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))


