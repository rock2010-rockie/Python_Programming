# 튜플 심화

# ===========================================================
#  튜플에서 제공하는 메소드
# ===========================================================

t = (1, 1, 2, 2, 2)

print(t.count(1))  # 1이 몇개 있는지?

print(t.index(2))  # 2의 첫번째 인덱스는?


# ===========================================================
#  그 외
# ===========================================================

# tuple -> list 변환
l = list(t)
print(l)

# list -> tuple 변환
t = tuple(l)
print(t)

# 튜플을 이용해서 swap하기
a, b = 10, 20
a, b = b, a
print(a, b)

# 튜플 언패킹
t = (1, 2, 3, 4)

print(*t)

a, b, c, d = t
print(a, b, c, d)

a, *b, c = t
print(a, b, c)

t2 = (5, 6)
print(t + t2)

print((*t, *t2))


# zip 함수 사용
subjects = ("국어", "수학", "영어")
scores = (80, 90, 95)

# (('국어', 80), ('수학', 90), ('영어', 95)) 출력하기
print(tuple(zip(subjects, scores)))


# ===========================================================
#  Tuple Comprehension은 없음
# ===========================================================

# Generator 표현식
gen = (x for x in range(1, 11))
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i, end=" ")
print()  # 순회환 곳을 기억함. 제너레이터는 한번쓰면 날아감(일회성)

# 순회가 끝나면 소진됨/ 초과로 더 쓰면 0이 출력
for i in gen:
    print(i, end=" ")
print()

a = [x for x in range(1, 11)]
b = (x for x in range(1, 11))
print(a, b)

# List comprehension vs generator
print(sum(a), sum(a))  # 55 55 출력
print(sum(b), sum(b))  # 55 0 출력

# 1 ~ 10의 제곱수 튜플 만들기
# ()는 튜플이 아니라 generator를 생성하는 generator 표현식임
result = tuple(
    x**2 for x in range(1, 11)
)  # 소괄호가 생략된 제너레이터 <- 인자가 하나여서
print(result)


# tuple의 생성자에 generator를 넘겨 값을 순회하면서 튜플을 만듦


# 두 점의 x, y, z축 좌표값끼리 더한 튜플을 만들기 (11,22,33)
p1 = (1, 2, 3)
p2 = (10, 20, 30)

result = tuple(a + b for a, b in zip(p1, p2))
print(result)


# =========================================================
#  🔥 실습 문제
# =========================================================

# 일주일 동안의 학습 시간을 저장한 튜플
days = ("일", "월", "화", "수", "목", "금", "토")
hours = (2, 3, 1, 4, 5, 2, 6)

# 1️⃣ 월 ~ 금까지 총 학습시간 출력하기
# ✅ 15시간
print(sum(hours[1:6]))

# 2️⃣ 가장 많이 공부한 시간 출력하기
# ✅ 6시간
print(max(hours))

# 3️⃣ 가장 많이 공부한 요일 출력하기
# ✅ 토요일
print(days[hours.index(max(hours))])

# 4️⃣ 가장 높은 점수와 가장 낮은 점수 출력하기
scores = (90, 85, 78, 92, 88, 76)

max = max(scores)
min = min(scores)

print(f"가장 높은 점수:{max}, 가장 낮은 점수:{min}")
# sortedd() 써서 [0]번째가 최소 [-1]번쨰가 최대로 구해서 코드 짤 수 있음

# ✅ max 점수: 92점, min 점수: 76점


# 5️⃣ 과일가게 총 재고 금액 구하기
stocks = (
    ("사과", 1000, 5),
    ("바나나", 2000, 3),
    ("체리", 5000, 2),
)

# 총 재고 금액 출력
total = sum(price * qty for _, price, qty in stocks) # _자리에 name이 들어가나 안쓰기 때문에 언더바 표시
# total = sum([price * qty for _, price, qty in stocks]) / 똑같다 

print(f"총액: {total:,}원")

#for entry in stocks:
#   total += entry[1] * entry[2]
#print(total)                       / for문으로 하기

# ✅ 총액: 21,000원
