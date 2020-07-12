# 파이썬 문자열, 리스트, 딕셔너리 다루기 마스터해보자

import json

with open('./swit_chat.json', 'r') as jsonfile:
    swit_chat_data = json.load(jsonfile)
    # print(swit_chat_data)

# swit_chat_data 에 담긴 데이터는 실제 광주인공지능사관학교 스윗의 데이터이다.
# 문제 :
# 가장 많이 글을 쓴 채팅을 작성한 사람은 누구일까..?
# 힌트 ) 유저 별 content 수를 세서 누가 가장 많이썼을지 알아보기

def get_frequent_user(user_data):
    table = fill_frequency_table(user_data)
    frequent_user = user_data[0]
    for user in user_data:
        if table[user] > table[frequent_user]:
            frequent_user = user
    return frequent_user, table[frequent_user]


def fill_frequency_table(user_data):
    table = {}
    for user in user_data:
        table[user] = 0
    print("채팅을 작성한 user들의 채팅 횟수를 0으로 초기화하겠습니다.")
    print(table)
    print("=====================================")
    for user in user_data: # 딕셔너리로 user를 key로하는 value를 증가한다. (value가 count역할)
        table[user] += 1
    print("user별 채팅 횟수를 보여드리겠습니다. ")
    print(table)

    return table


def main():
    user_data = []
    for data in swit_chat_data['data']:
        if data['content_type'] == 'chat':
            # print(data['user_name'])
            user_data.append(data['user_name'])
    answer, answer_count = get_frequent_user(user_data)
    print("=====================================")
    print("채팅을 가장 많이 작성한 사람은 <",answer,"> 이고, 채팅횟수는",answer_count,"번 입니다옹")

main()