# DemoFile.py
for i in range(0,10):
    url = "http://www.credu.com/?page=" + str(i)
    print(url)


for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---오른쪽 정렬---")    
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(5))

print("---서식 지정---")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))


#파일경로
filepath = r"c:\work\demo.txt" 

#파일 쓰기
f = open(filepath, "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일 읽기
f = open(filepath, "rt", encoding="utf-8")
result = f.read()

print("---라인단위---")
f.seek(0)
print( f.readline(), end="" )
print( f.readline(), end="" )

print("---리스트로 받기---")
f.seek(0)
result = f.readlines()
print(result)

f.close()
print(result)
