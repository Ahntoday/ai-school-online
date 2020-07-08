import json
import getpass

#json에 student 내용 저장
file_path = "./student.json"

students = [
    {
        'id': 'ser',
        'password': 1234,
        'name': '잔나비',
        'age': 18,
        'job': '대학생'
    },
    {
        'id': 'yeon',
        'password': 1234,
        'name': '검정치마',
        'age': 19,
        'job': '대학생'
    },
    {
        'id': 'jin',
        'password': 1234,
        'name': '스텔라장',
        'age': 22,
        'job': '대학생'
    }
]

data = {'students_list': students}
print(data)

with open(file_path, 'w') as outfile:
    json.dump(data, outfile, indent='\t')

#json 파일 읽기
with open(file_path, 'r') as json_file:
    json_data = json.load(json_file)
    print(json_data['students_list'])

def print_name():
    # json 파일 읽고, 학생들 이름 출력하기.
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)
        for i in range(3):
            print(json_data['students_list'][i]['name'])

def write_younger():
    # 20살 미만 학생 open의 쓰기 모드를 활용하여 넣어보기.
    younger_students = []
    younger_data = {'younger_list': younger_students}
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)
        for i in range(3):
            if (json_data['students_list'][i]['age'] < 20):
                younger_data['younger_list'].append({
                    'id': json_data['students_list'][i]['id'],
                    'password': json_data['students_list'][i]['password'],
                    'name': json_data['students_list'][i]['password'],
                    'age': json_data['students_list'][i]['age'],
                    'job': json_data['students_list'][i]['job']
                })
            with open(file_path, 'w') as outfile:
                json.dump(younger_data, outfile, indent='\t')

def print_younger():
    # 20살 미만 younger_students.json 읽어서 학생 출력
    with open(file_path, 'r') as json_file:
        younger_data = json.load(json_file)
        print(younger_data['younger_list'])

def check_id_isNULL():
    # 조건문으로 아이디를 안 넣으면, 쓰기 안 되게 막아보기
    id_input = input("아이디 입력 :")
    try:
        if id_input != "":
            write_data(id_input)
        else:
            raise NotImplementedError
    except NotImplementedError:
        print("아이디를 입력하지 않았습니다.")


def write_data(id_input):
    student=[]
    password_input = getpass.getpass("패스워드 입력 : ")
    print(password_input)
    name_input = input("이름 입력: ")
    age_input = int(input("나이 입력: "))
    job_input = input("직업 입력: ")
    student['id'] = id_input
    student['password'] = password_input
    student['name'] = name_input
    student['age'] = age_input
    student['job'] = job_input
    students.append(student)
    print("회원가입 완료")

if __name__ == "__main__":
    print_name()
    write_younger()
    print_younger()
    check_id_isNULL()

