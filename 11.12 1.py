# 문자열 슬라이싱
# [start:end:step]
# [:9:-1] 양수 음수 [인덱스 번호]

# string = "Monty Pyhon" #공백도 포함
# print(string[5])

#뒤에서 4자리
string = "Monty 7724"  #-4,-3,-2,-1(7724) monty 뒤에 문자가 바뀌어도 뒤에 4자리가 나옴
print(string[-4:]) #또는 string[-4::]

#[::] -> 전체 출력
#print(string[::]) 
