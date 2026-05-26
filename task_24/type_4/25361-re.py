from re import finditer
with open (r'../files/24_25361.txt') as file:
    data = file.readline()

pattern = r'[02468]([^F02468]*F){76}[^F02468]*'

matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))