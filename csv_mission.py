# TODO_0 : csv 모듈 불러오기
import csv

def user_input():
    try:
        id, pw = map(str, input("아이디와 비밀번호를 차례로 입력해주세요 : ").split())
        return id, pw
    except:
        print("올바르지 않은 입력입니다!")
        id, pw = user_input()
        return id, pw

# TODO_1 : signin 함수를 구현해서 로그인 시키기
# 1. csv 파일에서 존재하는 아이디인지 확인하기
# 2. 존재하면 비밀번호 맞는지 체크
# 3. 비밀번호도 맞으면 로그인성공 출력하기
def signin(id, pw):
    f = open('data.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr: # 다시 구현해야할 듯
        if id == line[0]:
            if pw == line[0][1]:
                print("로그인 성공")
    f.close()


# TODO_2 : csvfile 에 유저가 존재하는지 확인하는 함수 구현해서 호출하기
# 1. 아이디를 기준으로 존재하는 유저인지 확인
# 2. 존재한다면 다시 아이디를 입력받고,
# 3. 존재하지 않는다면 다음 단계로 넘겨주기
def check_user(id):
    f = open('data.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        if id == line[0]:
            #존재하는 경우 : 다시 아이디 입력받는다.
            id2 = input("아이디를 입력하세요")
            return id2
        else:
            #존재하지 않는 경우-> 다음단계
            return id
    f.close()


# TODO_3 : csvfile 에 등록되어있는 형태로 유저 등록하는 함수 구현하기
# 1. 아이디와 비밀번호를 그냥 데이터로 받아서 추가해보기
# 2. 아이디와 비밀번호를 '딕셔너리' 형태로 받아서 추가해보기 (프로그래밍 실력의 기본은 구글링! 최대한 구글링 해보세요!!)
def signup(checked_id, checked_pw):
    f = open('data.csv', 'a', newline='')
    wr = csv.writer(f)
    wr.writerow([checked_id, checked_pw])
    f.close()
    print("회원가입이 완료되었습니다.")

# def signup(dict_user):
#     print(dict_user)
#     f = open('data.csv', 'a', newline='')
#     wr = csv.writer(f)
#     wr.writerow(dict_user)
#     f.close()

def userlist():
    print("현재 존재하는 유저 :")
    # TODO_4 : csvfile 에서 현재 가입되어 있는 유저 전부 출력하기
    f = open('data.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        print(line)
    f.close()

def exitcheck():
    stop = int(input("\n계속하시려면 0, 종료하시려면 1을 눌러주세요. : "))
    if stop == 0:
        start()
    elif stop == 1:
        exit()


def start():
    print('csv 로 데이터 다루기 로그인 예제')

    signup_or_login = input('1 - 로그인 / 2 - 회원가입 : \n')

    if signup_or_login == '1':
        id, pw = user_input()
        # TODO_5 : 위의 TODO1 참고 후 signin 함수 실행하기
        signin(id, pw)

    elif signup_or_login == '2':
        # TODO_6 : 회원가입을 아이디와 비밀번호만 받아서 진행할 것
        # 1. 존재하는지 확인 (위의 TODO_2의 함수 활용)
        # 2. 문제 없으면 회원가입 완료 후 userlist() 함수 구현

        input_id = input("아이디를 입력하세요: ")
        checked_id = check_user(input_id)
        checked_pw = input("비밀번호를 입력하세요: ")

        dict_user = {
            "id": checked_id,
            "pw": checked_pw
        }

        # signup(id, pw) 데이터 그대로 전달해서 회원 등록
        signup(checked_id, checked_pw)

        # 딕셔너리로 전달해서 회원등록
        # signup(dict_user)

        userlist()
    else:
        print("올바른 숫자를 입력하세요!")

    exitcheck()


start()
