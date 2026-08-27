# 문자열
# "", '' <- "" 권장

a = "python"
print(a, type(a))
b = "pthton"  # 이거도 됨

# I'll be back
print("I'll be back")
print("I'll be back")

multiline = """
Life is short
You need Python
"""
print(multiline)


# docstring
def func():
    """이 함수는 테스트용입니다."""
    pass


print(func.__doc__)

# 문자열 연결
print("Hello" + "Python")
print("Hello" * 10)
print("-" * 100)

#print("10" + 10)
print(int("10") + int("2"))

#문자열 포멧팅(f-stfing)
name = "pororo"
age = 23

print(f"이름: {name}, 나이: {age}살")
print(f"내년 나이: {age + 1}살")
print(f"{name.upper()}")

pi = 3.141592

print(f"{pi:.3f}")

num=123456789

print(f"{num:,}")
print(f"{num:15,d}") #15칸 확보, 오른쪽 정렬 /  ,는 숫자와 d사이에 쓰고 천단위 콤마를 찍는다
print(f"{num:<15,d}") # 왼쪽 정렬
print(f"{num:015,d}") #15칸 확보, 오른쪽 정렬 /  ,는 숫자와 d사이에 쓰고 천단위 콤마를 찍는다 + 앞을 0으로 채움
