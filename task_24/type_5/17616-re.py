from re import finditer

with open (r'../files/24_17616.txt') as file:
    data = file.readline()

number = r'([1-9][0-9]*|0)'
zero = rf'({number}\*)*0(\*{number})*'
pattern = rf'{zero}(\+{zero})+'

matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))



ans = 0

for match in matches:
    len_match = len(match)
    if eval(match) == 0:
        ans = max(ans, len(match))
    elif len_match > ans:
        for l in range(0, len_match):
            if match[l] in '+*': continue
            if match[l] == '0' and match[l] not in '+*': continue
            for r in range(len_match - 1, l, -1):
                if match[r] in '+*': continue
                new_match = match[l:r + 1]
                if eval(new_match) == 0:
                    ans = max(ans, len(new_match))
                    break
print(ans)



