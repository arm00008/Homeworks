n = 0
for i in range(10):
    x = int(input())
    if x % 2 == 0:
        n += 1
if n == 10:
    print("YES")
else:
    print("NO")
