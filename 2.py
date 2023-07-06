a = int(input())
if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0):
    print('YES')
else:
    print('NO')

a = [1,2,-6,100,99,101,-80,0]
b = a[0]
i = 0
while i <= len(a):
    if a[i] >= b:
        b = a[i]

    i += 1
    if i == len(a):
        break

print(b)

with open("nums.txt", "r") as f:
    result = sum(map(int, f))
    print(result)

f.close()

a = [1,2,-6,100,99,101,-80,0]
b = a[0]
i = 0
while i <= len(a):
    if a[i] >= b:
        b = a[i]

    i += 1
    if i == len(a):
        break

print(b)
