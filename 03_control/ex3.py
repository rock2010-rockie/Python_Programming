# for 문

# for (int i = 0; i < 10; i++)
# for i in iterable객체:

for i in range(5):
    print(i, end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1, 6):
    print(i, end=" ")
print()

# 1 ~ 10, 2씩 띄어서
for i in range(1, 10, 2):
    print(i, end=" ")
print()

# 5, 4, 3, 2, 1
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 1 ~ 10까지의 합
tot = 0
for i in range(1, 11):
    tot += i
print(f"tot = {tot}")

print(sum(range(1, 11)))

s = "MAY 이예빈 (李睿彬) 🐘"

for c in s:
    print(c, end=" ")
print()

print(len(s))

# 구구단 출력
# 2 * 1 = 2  2 * 2 = 4  2 * 3 = 6  2 * 4 = 8  .. 2 * 9 = 18
# ..
# 9 * 1 = 9  9 * 2 = 18 .. 9 * 9 = 81
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}", end="\t")
    print()
else:
    print("End") #사실 굳이 안써도 된다
