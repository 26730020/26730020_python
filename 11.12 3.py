#input() 표준입력함수 ( 키보드 -> 변수 저장)

response = input(' 게임을 계속하시겠어요?)
if response,lower() == 'yes' or 'y':
              print('게임을 계속합니다.')
else:
              print('다음에 또 봐요.')

#대문자
print('Hello'.isupper())

#알파벳
print("abc123".isalpha())

#알파벳 + 숫자
print("abc123".isalnum())

#10진수
print('123'.isdecimal())

#줄바꿈 
