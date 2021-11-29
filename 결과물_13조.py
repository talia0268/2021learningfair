a = {"일반 핫도그": 3900 , "치즈 핫도그" : 4300 , "칠리 핫도그" : 4400 , "치킨 핫도그" : 4300}
b = {"초코 조각 케이크" : 6000,"치즈 조각 케이크" : 5000, "햄 에그 샌드위치" : 4500}
c = {"아메리카노" : 3300, "에스프레소" : 2700, "카페라떼" : 3800, "바닐라 라떼" : 4000}
d = {"레몬에이드" : 5000, "자몽에이드" : 5000, "청포도 에이드" : 5000}
print("[카페 오전 11시의 메뉴판]")
print(a)
print(b)
print(c)
print(d)

ans = "네"
ssum = 0
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sum7 = 0
sum8 = 0
sum9 = 0
sum10 = 0
sum11 = 0
sum12 = 0
sum13 = 0
sum14 = 0

while ans == "네" :

    name = input("원하시는 메뉴를 입력해주세요 : ")
    soo = int(input("수량을 입력해주세요 : "))
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    sum7 = 0
    sum8 = 0
    sum9 = 0
    sum10 = 0
    sum11 = 0
    sum12 = 0
    sum13 = 0
    sum14 = 0

    if name == "일반 핫도그":
        sum1 = soo * 3900

    elif name == "치즈 핫도그":
        sum2 = soo * 4300

    elif name == "칠리 핫도그":
        sum3 = soo * 4400

    elif name == "치킨 핫도그":
        sum4 = soo * 4300

    elif name == "초코 조각 케이크":
        sum5 = soo * 6000

    elif name == "치즈 조각 케이크":
        sum6 = soo * 5000

    elif name == "햄 에그 샌드위치":
        sum7 = soo * 4500

    elif name == "아메리카노":
        sum8 = soo * 3300

    elif name == "에스프레소":
        sum9 = soo * 2700

    elif name == "카페라떼":
        sum10 = soo * 3800

    elif name == "바닐라 라떼":
        sum11 = soo * 4000

    elif name == "레몬에이드":
        sum12 = soo * 5000

    elif name == "자몽에이드":
        sum13 = soo * 5000

    elif name == "청포도 에이드":
        sum14 = soo * 5000

    else:
        print("없는 메뉴입니다.")

    ssum = ssum + sum1 + sum2 + sum3 + sum4 + sum5 + sum6 + sum7 + sum8 + sum9 + sum10 + sum11 +sum12 + sum13 + sum14
    

    ans = input("다시 주문하시겠습니까?(네, 아니오)로 대답해주세요 : ")


an1 = "다시"

while an1 == "다시" :
    an1 = input("결제 수단을 선택해주세요 (카드/현금) : ")

    if an1 == "카드" :
        print(ssum , "원 카드로 결제하겠습니다.")
        print("--------ʅʕ´•ﻌ•`ʔʃ--------")

    elif an1 == "현금" :
        print(ssum , "원 현금으로 결제하겠습니다.")
        print("--------ʅʕ´•ﻌ•`ʔʃ--------")

    else :
        print("카드 혹은 현금으로 다시 대답해주세요 !! ")

        an1 = "다시"





