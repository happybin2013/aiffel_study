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
print("시가총액", 시가총액)
print("현재가", 현재가)
print("PER", PER)