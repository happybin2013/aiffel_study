# 아이펠 7기 python 기초교육
# https://wikidocs.net/

# 061~090
#061 price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#062 슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#063 슬라이싱을 사용해서 짝수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#064 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#065 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])

#066 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

#067 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

#068 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

#069 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

#070 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))

#071 my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()
print(my_variable)

#072 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
movie_rank = ("닥터 스트레인지","스플릿","럭키")
print(movie_rank)

#073 숫자 1 이 저장된 튜플을 생성하라.
one = (1,)
print(one)

#074 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# t = (1, 2, 3)
# t[0] = 'a' # 튜플은 원소값 수정이 불가능

#075 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
t = 1, 2, 3, 4
print(type(t))

#076 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t = ('a', 'b', 'c')
print(t)
t = ('A','b','c')
print(t)

#077 다음 튜플을 리스트로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(type(interest))

#78 다음 리스트를 튜플로 변경하라.
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(type(interest))

#079 다음 코드의 실행 결과를 예상하라.
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c) # apple banana cake

#080 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
data = tuple(range(2,100,2))
print(data)

'''
기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. 
하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. 
튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.
'''
#081 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b =  scores
print(*valid_score)

#082 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score =  scores
print(*valid_score)

#083 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b =  scores
print(*valid_score)

#084 temp 이름의 비어있는 딕셔너리를 만들라.
temp = {}
print(temp)

#085 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
price = {"메로나":1000,"폴라포":1200,"빵빠레":1800}
print(price)

#086 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
price["죠스바"] = 1200
price["월드콘"] = 1500
print(price)

#087 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

print("메로나 가격: ", ice["메로나"])

#088 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice["메로나"] = 1300
print(ice["메로나"])

#089 다음 딕셔너리에서 메로나를 삭제하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

del ice["메로나"]
print(ice)

#090 다음 코드에서 에러가 발생한 원인을 설명하라.
'''
>> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
>> icecream['누가바']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'
'''
# key값이 없기 때문에 발생
