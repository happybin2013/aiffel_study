# 아이펠 7기 python 기초교육
# https://wikidocs.net/

# 121~150
#121 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
# input_data = input("알파벳을 입력해 주세요: ")
# if input_data.islower() is True:
#     print(input_data.upper())
# else:
#     print(input_data.lower())

#122 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
# score = int(input("score: "))
#
# if 81 <= score <= 100:
#     print("grade is A")
# elif 61 <= score <= 80:
#     print("grade is B")
# elif 41 <= score <= 60:
#     print("grade is C")
# elif 21 <= score <= 40:
#     print("grade is D")
# else:
#     print("grade is E")

#123 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라.
# 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
# exchange_rate = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
# user = input("입력: ")
# key, value = user.split()
# print(float(key) * exchange_rate[value], "원")

#124 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
# input_list = []
# input_list.append(int(input("number1: ")))
# input_list.append(int(input("number2: ")))
# input_list.append(int(input("number3: ")))
#
# print(max(input_list))

#125 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
# phone_number = input("휴대전화 번호 입력: ")
# num = phone_number.split("-")[0]
# if num == "011":
#     com = "SKT"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# else:
#     com = "알수없음"
# print(f"당신은 {com} 사용자입니다.")

#126 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라
# input_data = input("우편번호: ")[:3]
# if input_data in ["010", "011", "012"]:
#     print("강북구")
# elif input_data in ["014", "015", "016"]:
#     print("도봉구")
# else:
#     print("노원구")

#127 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다.
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
# input_data = int(input("주민등록번호: ")[7])
# if input_data in [1,3]:
#     print("남자")
# elif input_data in [2,4]:
#     print("여자")

#128 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
# 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
# input_data = input("주민등록번호: ").split("-")[1]
# if 0 <= int(input_data[1:3]) <= 8:
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")

#129 다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.
# num = input("주민등록번호: ")
# 계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
#         int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
#         int(num[11])* 4 + int(num[12]) * 5
# 계산2 = 11 - (계산1 % 11)
# 계산3 = str(계산2)
#
# if num[-1] == 계산3[-1]:
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")

#130 btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다.
# 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#
# fluctuation_range = float(btc['max_price']) - float(btc['min_price'])
# opening_price = float(btc['opening_price'])
# max_price = float(btc['max_price'])
#
# if (opening_price+fluctuation_range) > max_price:
#     print("상승장")
# else:
#     print("하락장")

#141 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.
list = [100, 200, 300]
for data in list:
    print(data+10)

#142 for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.
list = ["김밥", "라면", "튀김"]
for data in list:
    print(f"오늘의 메뉴: {data}")

#143 저장된 문자열의 길이를 다음과 같이 출력하라.
list = ["SK하이닉스", "삼성전자", "LG전자"]
for data in list:
    print(len(data))

#144 동물 이름과 글자수를 다음과 같이 출력하라.
list = ['dog', 'cat', 'parrot']
for data in list:
    print(f"{data}", len(data))

#145 for문을 사용해서 동물 이름의 첫 글자만 출력하라.
list = ['dog', 'cat', 'parrot']
for data in list:
    print(data[0])

#146 for문을 사용해서 다음과 같이 출력하라.
list = [1, 2, 3]
for data in list:
    print(f"3 x {data}")

#147 for문을 사용해서 다음과 같이 출력하라.
list = [1, 2, 3]
for data in list:
    print(f"3 x {data} =",3*data)

#148 for문을 사용해서 다음과 같이 출력하라.
list = ["가", "나", "다", "라"]
for data in list[1:]:
    print(data)

#149 for문을 사용해서 다음과 같이 출력하라.
list = ["가", "나", "다", "라"]
for data in list[::2]:
    print(data)

#150 for문을 사용해서 다음과 같이 출력하라.
list = ["가", "나", "다", "라"]
for data in list[::-1]:
    print(data)
