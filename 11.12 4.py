print(' '.isspace())
print('\n'.isspace())
print('   '.isspace())
#startswith(s) s로 시작하는지 검사
#endswith(s) s로 끝나는지 검사 (주로 확장명 검사)

#split(공백) -> 리스트
string = "welcome to python"
string = (string.split(' '))
print(string)

string1 = "welcome/to/python"
string1 = string1. split('/')
print(string1)

#문자열을 하나의 문자 요소들로 변환 list()
string = "welcome to python"
string = list(string)

#문자열을 하나의 문자 요소들로 변환 list() 공백은 빼고
#replace() , join()
string1 = "welcome to python"
string1 = list(string1.replace(" ",""))
