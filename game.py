print("갤러그 게임 시작")
print("적 비행기 출현")
print("1. 발사 2. 오른쪽이동 3. 왼쪽이동")
number = input("숫자를 입력하세요: ")
print("입력값: ", number)
#만약 1번을 입력하면 총알 발사
if int(number) == 1:
  print("총알 발사!")
#만약 2번을 입력하면 오른쪽이동
elif int(number) == 2:
  print("오른쪽이동")
#만약 3번을 입력하면 왼쪽이동
elif int(number) == 3:
  print("왼쪽이동")