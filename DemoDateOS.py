# DemoDateOS.py
from datetime import *

print( dir() )
d1 = date(2023,7,20)
print(d1)
d2 = date.today()
print(d2)
d3 = timedelta(days=100)
print(f"100일을 더하면:{d2+d3}")
d4 = datetime.now()
print(d4)

import random
print(random.random())
print(random.random())
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20),10))
print(random.sample(range(20),10))


from os.path import *
print(abspath("python.exe"))
print(basename("c:\\python310\\python.exe"))
print(getsize("c:\\python310\\python.exe"))

if isfile("c:\\python310\\python.exe"):
    print("파일 있음")
else:
    print("파일 없음")


lotto = list(range(1,46))
random.shuffle(lotto)
print(lotto)
j = 0
for i in lotto:
    print(i)
    j = j + 1
    if j > 5:
        break


from os import *

# print( dir() )
print("운영체제이름:", name)
print("환경변수:", environ)
# print(system("notepad.exe"))

print("현재폴더:", getcwd())
chdir("..")
print("현재폴더:", getcwd())
chdir("c:\\work")
print("현재폴더:", getcwd())

import glob
result = glob.glob("*.py")

print(result)
for item in glob.iglob("*.*"):
    print(item)