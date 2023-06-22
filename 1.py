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

