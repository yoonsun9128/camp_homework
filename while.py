def main():
        count = 0
        max_count = 5
        while True:
                a = input("숫자를 입력해 주세요(종료 - exit) : ")
                if count > max_count:
                        print("5회이상 진행 했습니다!")
                        break
                elif a == "exit":
                        print("게임을 종료하셨습니다.")
                        break
                
                try : 
                        a = int(a)
                        count += 1
                        print(int(a) * 2)  
                except ValueError:
                        count -= 1
                        print(f"입력한 문자는 {a} 입니다!!")   
               

main()
