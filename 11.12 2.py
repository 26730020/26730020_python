#학생 정보가 담긴 문자열
# 기호 |    김한결(3글자) 김한|(2글자)  김|(1글자)
student = "20261234홍길동|컴퓨터공학과"
student1 = "20261234홍길|컴퓨터공학과"
student2 = "20261234홍|컴퓨터공학과"

pos = student2.find("|") #$
print(pos)

if len(student) ==17:
#문자열 슬라이싱으로 정보 추출
student_id = student[0:8]  #학번
name = student[8:pos]  #이름
major = student[pos+1:]  #학과

#결과 출력
print("학번:", student_id)
print("이름:",name)
print("학과:",major)

string = "Monty Python"
print(string[-1]) #결과 n
print(string[:-1]) #결과 Monty Pytho
