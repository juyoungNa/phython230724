# DemoStr.py
# print( dir(str) )

strA = "파이썬은 강력해"
strB = "python is very powerful"

print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.count("p"))
print(strB.count("p",7))
print(strB.startswith("python"))
print(strB.endswith("ful"))
result = strB.upper()
print(result)
result2 = result.lower()
print(result2)

data = "<<<  spam and ham  >>>"
result = data.strip("<> ")
print(data)
print(result)
result2 = result.replace("spam", "spam egg")
print(result2)
lst = result2.split()
print(lst)
print("---하나의 문자열로 합치기---")
print("|".join(lst))
data2 = "spam::ham::egg"
result3 = data2.split("::")
print(result3)
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("MBC2580".isdecimal())
print("2580".isdecimal())

