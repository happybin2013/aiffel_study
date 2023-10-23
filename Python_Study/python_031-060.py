# 아이펠 7기 python 기초교육
# https://wikidocs.net/

# 031~060
#031 아래 코드의 실행 결과를 예상해보세요.
a = "3"
b = "4"
print("#031: ",a + b) #34

#032 아래 코드의 실행 결과를 예상해보세요.
print("#032: ","Hi" * 3) #HiHiHi

#033 화면에 '-'를 80개 출력하세요.
print("#033: ","-" * 80)

#034 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
t1 = 'python'
t2 = 'java'
t3 = t1 + " " + t2 + " "
print("#034: ",t3 * 4)

#35 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("#035: ","이름: %s 나이: %d" %(name1,age1))
print("#035: ","이름: %s 나이: %d" %(name2,age2))

#036 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
print("#036: ","이름: {} 나이: {}".format(name1,age1))
print("#036: ","이름: {} 나이: {}".format(name2,age2))

#037 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
print("#037: ",f"이름: {name1} 나이: {age1}")
print("#037: ",f"이름: {name2} 나이: {age2}")

#038 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
상장주식수 = "5,969,782,550"
print("#038: ",int(상장주식수.replace(",","")))

#039 다음과 같은 문자열에서 '2020/03'만 출력하세요.
분기 = "2020/03(E) (IFRS연결)"
print("#039: ",분기[:7])

#040 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "   삼성전자    "
print("#040: ",data.strip())

#041 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"
print("#041: ",ticker.upper())

#042 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker = "BTC_KRW"
print("#042: ",ticker.lower())

#043 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
print("#043: ","hello".capitalize())

#044 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
if file_name.endswith("xlsx"):
    print("#044: ","xlsx으로 끝남")
else: print("#044: ","xlsx으로 끝남X")

#045 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx","xls")))
if file_name.endswith(("xlsx","xls")):
    print("#045: ","xlsx 또는 xls으로 끝남")
else: print("#045: ","xlsx으로 끝남X")

#046 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))
if file_name.startswith("2020"):
    print("#046: ","2020시작")
else: print("#046: ","2020시작X")

#047 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
print("#047: ",a.split(" "))

#048 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
print("#048: ",ticker.split("_"))

#049 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-05-01"
date_split = date.split("-")
print("#049: ","연도: " + date_split[0],"월: " +date_split[1],"일: "+ date_split[2])

#050 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
data = "039490     "
print("#050: ",data.rstrip())

#051 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print("#051: ",movie_rank)

#052 051의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append("배트맨")
print("#052: ",movie_rank)

#053 movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank.insert(1,"슈퍼맨")
print("#053: ",movie_rank)

#054 movie_rank 리스트에서 '럭키'를 삭제하라.
del movie_rank[3]
print("#054: ",movie_rank)

#055 movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
del movie_rank[2]
del movie_rank[2]
print("#055: ",movie_rank)

#056 lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

print("#056: ",lang1 + lang2)

#057 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
nums = [1, 2, 3, 4, 5, 6, 7]
print("#057: ","max: ", max(nums))
print("#057: ","min: ", min(nums))

#058 다음 리스트의 합을 출력하라.
nums = [1, 2, 3, 4, 5]
print("#058: ",sum(nums))

#059 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print("#059: ","개수: ",len(cook))

#060 다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5]
print("#060: ",sum(nums) / len(nums))