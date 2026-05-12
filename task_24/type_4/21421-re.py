from re import finditer
with open (r'../files/24_21421.txt') as file:
    data = file.readline()

pattern = '[1-9AB][0-9AB]*[02468A]'

matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))