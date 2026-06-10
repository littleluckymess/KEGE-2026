from re import finditer
with open (r'../files/24_18186.txt') as file:
    data = file.readline()

SSG = r'[^AE]{2}[AE]'
pattern = rf'(?<={SSG}).*?(?={SSG})'

matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len))+6)
