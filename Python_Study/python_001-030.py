# 아이펠 7기 python 기초교육
# https://wikidocs.net/ 001~030

#001 출력: Hello World
print("#001: ","Hello World")

#002 출력: Mary's cosmetics
print("#002: ","Mary's cosmetics")

#003 출력: 신씨가 소리질렀다. "도둑이야".
print("#003: ",'신씨가 소리질렀다. "도둑이야".')

#004 출력: C:\Windows
print("#004: ","C:\Windows")

#005 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
print("#005: ","안녕하세요.\n만나서\t\t반갑습니다.") # /n은 줄바꿈 /t는 탭의 역할을 한다.

#006 출력 예상
print("#006: ","오늘은", "일요일") #오늘은 일요일

#007 출력: naver;kakao;sk;samsung
print("#007: ","naver","kakao","sk","samsung",sep=";")

#008 출력: naver/kakao/sk/samsung
print("#008: ","naver","kakao","sk","samsung",sep="/")

#009 다음 코드를 수정하여 줄바꿈이 없이 출력하세요.
print("#009: ","first",end='');print("second")

#010 5/3의 결과를 화면에 출력하세요.
print("#010: ",5/3)

#011 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자 = 50000
print("#011: ","삼성전자 10주의 총 평가금액: ", 삼성전자 * 10)

#012 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
'''
항목	값
시가총액	298조
현재가	50,000원
PER	15.79
'''
시가총액 = "289조"
현재가 = "50,000원"
PER = 15.79
print("#012")
print("시가총액", 시가총액)
print("현재가", 현재가)
print("PER", PER)

#013 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
s = "hello"
t = "python"

print("#013: ",s+"!",t)

#014 아래 코드의 실행 결과를 예상해보세요.
print("#014: ",2 + 2 * 3) # 8

#015 type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
a = "132"
print("#015: ",type(a))

#016 문자열 '720'를 정수형으로 변환해보세요.
num_str = "720"
print("#016: ",int(num_str))

#017 정수 100을 문자열 '100'으로 변환해보세요.
num = 100
print("#017: ",str(num))

#018 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
float_str = "15.79"
print("#018: ",float(float_str))

#019 year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = "2020"
year_int = int(year)
print("#019: ",year_int-2, year_int-1, year_int,sep='\n')

#020 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
month_price = 48584
total_price = month_price * 36
print("#020: ",total_price)

#021 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
print("#021: ",letters[0], letters[2])

#022 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
print("#022: ",license_plate[-4:])

#023 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
print("#023: ",string[::2]) #짝만 출력[1::2]

#024 문자열을 거꾸로 뒤집어 출력하세요.
string_python = "PYTHON"
print("#024: ",string_python[::-1])

#025 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
print("#025: ",phone_number.replace("-"," "))

#026 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
phone_number = "010-1111-2222"
print("#026: ",phone_number.replace("-",""))

#027 url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "http://sharebook.kr"
print("#027: ",url.split(".")[-1])

#028 아래 코드의 실행 결과를 예상해보세요.
#lang = 'python'
#lang[0] = 'P'
#print("#028: ",lang) #에러 출력 문자열 수정 불가

#029 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string_aA = 'abcdfe2a354a32a'
print("#029: ",string_aA.replace("a","A"))

#030 아래 코드의 실행 결과를 예상해보세요.
string = 'abcd'
string.replace('b', 'B')
print("#030: ",string) #abcd 문자열은 수정 불가

