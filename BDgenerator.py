import random

bd_stu = random.randrange(2002, 2005)*10000 + \
    random.randrange(1, 13)*100 + random.randrange(1, 28)

bd_uni = random.randrange(1980, 1990)*10000 + \
    random.randrange(1, 13)*100 + random.randrange(1, 28)

bd_str = random.randrange(1970, 2002)*10000 + \
    random.randrange(1, 13)*100 + random.randrange(1, 28)

inp = input("(1) : 학생의 생년월일 \n(2) : 성인의 생년월일 \n(3) : 완전 랜덤\n")
if inp == "1":
    print(bd_stu)
elif inp == "2":
    print(bd_uni)
elif inp == "3":
    print(bd_str)