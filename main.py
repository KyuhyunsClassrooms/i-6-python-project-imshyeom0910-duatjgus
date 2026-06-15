key_piece = 0



quiz_data = [

    [

        "병원에서 가장 기본적으로 사용되며, 독일의 물리학자 뢴트겐이 발견한 방사선의 이름은?",

        "X선",

        "알파벳 대문자 한 글자와 선"

    ],

    [

        "컴퓨터 단층촬영의 영문 약어는?",

        "CT",

        "대문자 2글자"

    ],

    [

        "방사선 피폭을 줄이는 3대 원칙은 시간, 거리 그리고 무엇인가?",

        "차폐",

        "방사선을 가리는 것"

    ],

    [

        "방사선량의 국제단위(SI 단위)는?",

        "2",

        "c but)"

    ]

]



def show_intro():

    print("=" * 60)

    print("눈을 떠보니 나는 낡고 음침한 폐병원 안에 누워 있었다.")

    print("주변은 어둡고 적막했다.")

    print("내가 누구인지, 왜 이곳에 있는지 기억나지 않는다.")

    print("\n'여기서 나가야 해.'")

    print("=" * 60)



    name = input("당신의 이름을 기억해내 보세요: ")

    print(f"\n[시스템] {name}님의 기억을 찾는 탈출을 시작합니다.")

    return name





def quiz(question, answer, hint):

    while True:

        print("\n" + question)

        user = input("정답 입력 : ")



        if user.lower() == answer.lower():

            print("✅ 정답입니다!")

            break

        else:

            print("❌ 오답입니다.")

            print("💡 힌트 :", hint)





def floor1():

    print("\n" + "=" * 60)

    print("1층 : 어두운 X-ray실")

    print("=" * 60)



    while True:

        print("\n1. X-ray 촬영대 조사")

        print("2. 낡은 책상 조사")

        print("3. 문 조사")

        print("4. 퀴즈 풀기")



        choice = input("선택 : ")



        if choice == "1":

            print("\n촬영대 위에 먼지가 쌓인 환자복이 놓여 있다.")

            print("가슴 부분에 숫자 '1024'가 적혀 있다.")

            print("왜인지 모르게 익숙하다.")



        elif choice == "2":

            print("\n환자번호 : 1024")

            print("이름 : 삭제됨")

            print("기록 일부가 훼손되어 있다.")



        elif choice == "3":

            print("\n잠긴 문이다.")

            print("숫자 비밀번호가 필요해 보인다.")



        elif choice == "4":

            quiz(

                quiz_data[0][0],

                quiz_data[0][1],

                quiz_data[0][2]

            )

     

            while True:

                password = input("\n비밀번호를 입력하세요 : ")



                if password == "1024":

                    print("🔓 문이 열렸다!")

                    return

                else:

                    print("비밀번호가 틀렸습니다.")





def floor2():

    global key_piece



    print("\n" + "=" * 60)

    print("2층 : 버려진 CT실")

    print("=" * 60)



    while True:

        print("\n1. CT 장비 조사")

        print("2. 컴퓨터 조사")

        print("3. 보관함 조사")

        print("4. 퀴즈 풀기")



        choice = input("선택 : ")



        if choice == "1":

            print("\n환자번호 : 1024")

            print("상태 : 심각한 피폭")



        elif choice == "2":

            print("\n기록 접근 제한")

            print("환자 정보 일부가 삭제되어 있다.")



        elif choice == "3":

            print("\n잠겨 있는 보관함이다.")



        elif choice == "4":

            quiz(

                quiz_data[1][0],

                quiz_data[1][1],

                quiz_data[1][2]

            )

           

            key_piece += 1

            print(f"\n🗝️ 열쇠 조각 획득! ({key_piece}/3)")

            return





def floor3():

    global key_piece



    print("\n" + "=" * 60)

    print("3층 : 방사선 치료실")

    print("=" * 60)



    while True:

        print("\n1. 치료기 조사")

        print("2. 환자 차트 조사")

        print("3. CCTV 조사")

        print("4. 퀴즈 풀기")



        choice = input("선택 : ")



        if choice == "1":

            print("\n치료기가 꺼져 있지만 경고등이 깜빡인다.")



        elif choice == "2":

            print("\n환자번호 : 1024")

            print("사고 조사 진행 중")

            print("원장 승인 문서 존재")



        elif choice == "3":

            print("\n흐릿한 CCTV 영상이 재생된다.")

            print("한 환자가 치료실 안으로 들어온다.")

            print("영상은 심하게 깨져 얼굴을 알아볼 수 없다.")

            print("잠시 후 경고음이 울리고 화면이 끊긴다.")

            print("\n[환자번호 1024]")

            print("[기록 종료]")



        elif choice == "4":

            quiz(

                quiz_data[2][0],

                quiz_data[2][1],

                quiz_data[2][2]

            )

         



            key_piece += 1

            print(f"\n🗝️ 열쇠 조각 획득! ({key_piece}/3)")

            return





def floor4(player_name):

    global key_piece



    print("\n" + "=" * 60)

    print("4층 : 원장실")

    print("=" * 60)



    while True:

        print("\n1. 책장 조사")

        print("2. 서랍 조사")

        print("3. 금고 조사")



        choice = input("선택 : ")



        if choice == "1":

            print("\n사고 은폐 보고서")

            print("--------------------")

            print("방사선 과다 피폭")

            print("사망 확인")

            print("환자 기록 삭제")

            print("사고 보고서 폐기")

            print("관계자 진술 통제")

            print("사건 은폐 완료")



        elif choice == "2":

            if key_piece < 3:

                key_piece += 1



            print(f"\n🗝️ 열쇠 조각 획득! ({key_piece}/3)")



            if key_piece == 3:

                print("🔑 열쇠가 완성되었다!")



        elif choice == "3":



            if key_piece < 3:

                print("\n열쇠가 부족하다.")

                continue



            print("\n금고가 열렸다...")

            print("\n====================")

            print("환자 신원 확인서")

            print("====================")

            print("환자번호 : 1024")

            print(f"이름 : {player_name}")

            print("\n사망 원인 : 방사선 과다 피폭")

            print("최종 상태 : 사망")



            print("\n순간 머릿속으로 모든 기억이 밀려온다.")

            print("차가운 치료실.")

            print("울리는 경고음.")

            print("당황한 의료진.")

            print("\n그리고...")

            print("\n침대 위에 누워 있던 사람은")

            print("\n바로 당신이었다.")



            final_quiz()

            return





def final_quiz():



    while True:



        print("\n" + quiz_data[3][0])



        print("1. 렘(rem)")

        print("2. 시버트(Sv)")

        print("3. 큐리(Ci)")

        print("4. 베크렐(Bq)")



        answer = input("선택 : ")



        if answer == quiz_data[3][1]:

            print("\n출구가 열렸다...")

            break



        else:

            print("❌ 오답입니다.")

            print("💡 힌트 :", quiz_data[3][2])



def show_ending():

    print("\n" + "=" * 60)

    print("1. 진실 수용 엔딩")

    print("2. 진실 폭로 엔딩")

    print("=" * 60)



    choice = input("선택 : ")



    if choice == "1":

        print("\n'그래... 나는 이미 죽었구나.'")

        print("\n당신은 모든 기억을 받아들인다.")

        print("병원 복도 끝에서 따뜻한 빛이 새어 나온다.")

        print("당신은 천천히 그 빛을 향해 걸어간다.")

        print("\n더 이상 두렵지 않다.")

        print("\n[진실 수용 엔딩]")



    elif choice == "2":

        print("\n'나는 죽었지만... 이 일은 묻혀서는 안 돼.'")

        print("\n당신은 사고 기록과 은폐 문서를 챙긴다.")

        print("다음 날 병원의 의료사고가 세상에 알려진다.")

        print("병원은 폐쇄되고 진실은 밝혀진다.")

        print("\n[진실 폭로 엔딩]")



    else:

        print("\n운명을 선택하지 못했다.")

        print("[배드 엔딩]")









player_name = show_intro()



floor1()

floor2()

floor3()

floor4(player_name)



show_ending()



print("\n게임 종료") 




