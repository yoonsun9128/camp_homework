import random
from pprint import pprint
from unittest import result
from datetime import datetime
import time

def play():
    a_num = int(input("글자수를 선택하세요 : "))
    if a_num >=3 and a_num <=10 :
        # 3 -> 입력하면 3자리 숫자가 나옴
        ball = "0123456789"
        game = []
        for i in range(a_num):
            
            while len(game) < a_num:
                game.append(random.randrange(0,len(ball)))
    else:
        print("3부터 10까지로 입력해주세요.")
    print(game)
    print(type(game))
    start_time = time.time()

    count = 0
    last_count = 9
    while True:
        player = input("값을 입력해주세요(종료 - exit) : ")
        count += 1
        if count > last_count:
            print("실패했습니다!")
            break
        elif player == "exit":
            print("게임을 종료하셨습니다.")
            break
        out_count = 0
        st_count = 0
        ball_count = 0
        for i, v in enumerate(player):
            v = int(v)
            if v not in game:
                out_count += 1
            else:
                if game[i] == v:
                    st_count += 1
                else:
                    ball_count += 1
                    
        if st_count == a_num:
            print(f"승리, 도전횟수: {count}번")
            print(f"소요시간 : {time.time()-start_time:.2f}")
            print(f"클리어 일자 : {datetime.now()}")
            break

        print(f"{st_count}스트라이크 {ball_count}볼 {out_count}아웃")
play()
