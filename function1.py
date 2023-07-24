# function1.py
#함수 정의
def setValue(newValue):
    x = newValue
    print("지역변수:", x)

#함수 호출
result = setValue(5)
print(result)

#함수 정의
def swap(x,y):
    return y,x

#호출
print( swap(3,4) )

#교집합 문자를 리턴하는 함수
def intersect(prelist, postlist):
    #지역변수
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #x라는 글자가 postlist에 있고 x가 result에 없으면
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print(intersect("HAM", "SPAM"))
