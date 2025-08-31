import time 
import sys
import json
from pathlib import Path

user_finish_list = ["終了", "終わり", "バイバイ", "さようなら"]

user_name = ""
mode = ""

def start():
    global user_name
    user_name = input("あなたの名前を教えてください: ")
    print(f"わかりました。これからは{user_name}さんとお呼びいたしますね！")
    print(f"こんにちは、{user_name}さん!このAIは性能が低いのでモードを選択してもらうことにしているのです...")
    print("なのでモードを以下のところから選択してください!")
    mode_choose()

def mode_choose():
    global mode
    print("モード準拠、了解しました！では以下のモードから選択してください。")
    print("1.ノーマルモード\n2.フレンズモード\n3.プログラミングモード")
    mode_input = input("")
    if mode_input == "1":
        mode = "normal"
        print("ノーマルモードでお話ししましょう！何を話しましょう？")
        return
    if mode_input == "2":
        mode = "friends"
        print("フレンズモードだね！じゃあ何を話そうか？")
        return
    if mode_input == "3":
        mode = "programming"
        print("プログラミングモードでお話ししましょう。プログラミング関連なら何でもお答えしますよ！")
        return

base_path = Path(__file__).parent

with open(base_path / 'ai_studies.json', 'r', encoding='utf-8') as f:
    studiesinput = json.load(f)

def get_studies_data(mode, user_chat):
    chat_dict = studiesinput.get(mode, {}).get("user_chat", {})
    return chat_dict.get(user_chat, studiesinput[mode]["default"])

start()
while True:
    if mode == "normal":
        user_chat = input("")
        if user_chat in user_finish_list:
            print(f"わかりました！では{user_name}さん、またお会いしましょう！")
            time.sleep(2)
            sys.exit()
        elif user_chat in studiesinput["normal"]["user_chat"]:
            print(studiesinput["normal"]["user_chat"][user_chat])
        else:
            print(studiesinput["normal"]["default"])

    if mode == "friends":
        f_user_chat = input("")
        if f_user_chat in user_finish_list:
            print(f"わかりました！では{user_name}さん、またお会いしましょう！")
            time.sleep(2)
            sys.exit()
        elif f_user_chat in studiesinput["friends"]["f_user_chat"]:
            print(studiesinput["friends"]["user_chat"][f_user_chat])
        else:
            print(studiesinput["friends"]["default"])

    if mode == "programming":
        p_user_chat = input("")
        if p_user_chat in user_finish_list:
            print(f"わかりました！では{user_name}さん、またお会いしましょう！")
            time.sleep(2)
            sys.exit()
        elif p_user_chat in studiesinput["programming"]["p_user_chat"]:
            print(studiesinput["programming"]["user_chat"][f_user_chat])
        else:
            print(studiesinput["programming"]["default"])