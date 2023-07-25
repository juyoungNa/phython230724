# ifelse.py
#선택한 블럭 추석처리 : ctrl + /
# score = int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

value = 5
while value > 0:
    print(value)
    value -= 1

lst = [100, "문자열", 3.14]
for i in lst:
    print(i, type(i))

print("---break---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---continue---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

print("---range함수---")
print(list(range(1,11)))
print(list(range(2000,2024)))
print(list(range(1,32)))

for i in range(10):
    print(i)