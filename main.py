
# 1
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)


# 2
sum = 0
for i in range(1, 50):
    sum += i
    if i % 5 != 0:
        print(i)
        continue

# 3
for i in range(-10, 11):
    if i < 0:
        continue
    print(i * i, end=' ')

# 4
sum = 0
for i in range(1, 100):
    if i % 3 == 0:
        continue
    sum += i
    
print(sum)
