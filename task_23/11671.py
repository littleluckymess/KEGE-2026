def f(start, cnt):
  if cnt == 15:
      return [start]
  return f(start + 10, cnt + 1) + f(start - 5, cnt + 1)

print(len(set(f(1,0))))

#########################

def f(start, cnt):
  if cnt == 15:
      return {start}
  return f(start + 10, cnt + 1) | f(start - 5, cnt + 1)

print(len(set(f(1,0))))

##########################

def f(start, cnt):
  if cnt == 15:
      ans.add(start)
      return
  f(start + 10, cnt + 1)
  f(start - 5, cnt + 1)

ans = set()
f(1,0)
print(len(ans))

############################

nums = {1}
for i in range(15):
    nums = {x + 10 for x in nums} | {x - 5 for x in nums}
print(len(nums))
