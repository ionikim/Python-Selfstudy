# 혼자공부하는파이썬 chapter 03-02 간단한 대화프로그램

from datetime import datetime

greeting = str(input('입력: '))

if '안녕' in greeting:
    print("안녕하세요")
elif '몇 시' in greeting:
    now = datetime.now()
    print("{}시 {}분 입니다.".format(now.hour, now.minute))
else:
    print(greeting)