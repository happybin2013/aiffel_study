# 아이펠 7기 python 기초교육
# https://wikidocs.net/

# 091~120
#091 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.
inventory = {"메로나":[300,20],"비비빅":[400,3],"죠스바":[250,100]}
print(inventory)

#092 inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory["메로나"][0],"원")

#093 inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory["메로나"][1],"개")

#094 inventory 딕셔너리에 아래 데이터를 추가하라.
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
inventory["월드콘"] = [500,7]
print(inventory)

#095 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream_key_list = icecream.keys()
print(icecream_key_list)

#096 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream_value_list = icecream.values()
print(icecream_value_list)

#097 icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(sum(icecream.values()))

#098 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#099 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
fruit = dict(zip(keys,vals))
print(fruit)

#100 date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_dict = dict(zip(date,close_price))
print(close_dict)

#111 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
# input_hellow = input("입력(안녕하세요): ")
# print(input_hellow * 2)

#112 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
# input_num = input("입력(정수): ")
# print(type(input_num))
# try:
#     print(int(input_num) + 10)
# except:
#     print("정수를 입력해주세요..")

#113 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
# input_num = int(input("정수를 입력해주세요: "))
# if input_num % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

#114 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
# input_num = int(input("정수를 입력해주세요: ")) + 20
# if input_num <= 255:
#     print(input_num)
# else:
#     print(255)

#115 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 출력 값의 범위는 0~255이다.
# 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
# input_num = int(input("정수를 입력해주세요: ")) - 20
# if input_num > 255:
#     print(255)
# elif input_num < 0:
#     print(0)
# else:
#     print(input_num)

#116 사용자로부터 입력 받은 시간이 정각인지 판별하라.
'''
현재시간:02:00
정각 입니다.
'''
# input_time = input("시간을 입력해 주세요: ")
# if input_time[-2:] == "00":
#     print("정각입니다.")
# else:
#     print("정각이 아닙니다.")

#117 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = ["사과", "포도", "홍시"]
# input_word = input("좋아하는 과일은? ")
# if input_word in fruit:
#     print("정답입니다.")
# else:
#     print("X")

#118 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이
# 투자 경고 종목이라면 '투자 경고 종목입니다'를
# 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
#
# investment_data = input("투자하려는 종목을 알려주세요: ")
# if investment_data in warn_investment_list:
#     print("투자 경고 종목입니다")
# else:
#     print("투자 경고 종목이 아닙니다.")

#119 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
#
# input_data = input("제가 좋아하는 계절은? ")
#
# if input_data in fruit.keys():
#     print("정답입니다.")
# else:
#     print("오답입니다.")

#120 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

input_data = input("좋아하는 과일은? ")

if input_data in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")