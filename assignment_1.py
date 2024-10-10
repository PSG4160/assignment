from random import *

def game_start():
    class DataError(Exception):  # 예외처리 옵션을 넣기 위해 예외 클래스화 
        pass

    while(True):
        random_number = randrange(1, 11)  # 1~10 사이의 숫자 생성하기
        # print(random_number) # 코드 완성 전에 편하게 확인하기
        print("숫자를 맞춰보세요.")

        while(True):
            try:
                my_number = int(input("숫자를 입력하세요 : "))
                if my_number <= 0 or my_number >= 11:
                    raise ValueError
                
                if random_number > my_number:
                    print("숫자가 너무 작아요. 다시 입력하세요.")
                elif random_number < my_number:
                    print("숫자가 너무 커요. 다시 입력하세요.")
                else:
                    print("정답입니다. GOOD")
                    break  # 정답을 맞췄으니 스탑!
                
            except ValueError:
                print("1~10 까지의 숫자만 입력 하세요.")

        while(True):
            try:
                regame = str(input("게임을 재시작 하겠습니까? (yes/no) :"))
                if regame.lower() not in ["yes", "no"]:
                    raise DataError
                
                if regame == "no":
                    print("게임을 종료하겠습니다.")
                    return  # 함수 종료 !!!!!!!! (이거 때문에 고생했음)
                elif regame == "yes":
                    break  # 게임 재시작
            except DataError:
                print("yes 또는 no만 입력하세요.")

game_start()