#Dish_Change

n = int(input())
a = list(map(int, input().split()))

best = 0
ans = float('inf')

for dish in set(a):
    last_picked = -2
    count = 0
    
    for i in range(n):
        if a[i] == dish and i != last_picked + 1:
            count += 1
            last_picked = i
    
    if count > best or (count == best and dish < ans):
        best = count
        ans = dish

print(ans)