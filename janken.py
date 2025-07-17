import random

hands = ['G', 'C', 'P'] #手の出し方
win_map = {
    'G': 'C', #グーはチョキに勝つ
    'C': 'P', #チョキはパーに勝つ
    'P': 'G', #パーはグーに勝つ
}

def judge(my, oppo): #勝敗の判定
    if my == oppo:
        return 'draw'
    elif win_map[my] == oppo:
        return 'win'
    else:
        return 'lose'

print('じゃんけんをします。3本勝負。2本先取。')
my_points = 0 #自分の得点
oppo_points = 0 #相手の得点

while my_points < 2 and oppo_points < 2: #どちらかの得点が2点になるまで繰り返す
    try:
        my = input('(G=グー,C=チョキ,P=パー ):').strip().upper()
        if my not in hands:
            raise ValueError('無効な手です')

        oppo = random.choice(hands)
        print(f"じゃんけん・・・ポン！あなた:{my},相手:{oppo}")

        result = judge(my, oppo)
        if result == 'draw':
            print('あいこです。もう一度\n')
            continue #あいこのとき繰り返す。
        elif result == 'win':
            print('あなたの勝ち！\n')
            my_points += 1 #勝った時自分のポイントに1点加算
        else:
            print('あなたの負けです。\n')
            oppo_points += 1 #負けた時相手のポイントに1点加算

        print(f"【現在のスコア】わたし:{my_points},相手:{oppo_points}")

    except ValueError as e:
        print(e)
        print("もう一度入力してください。\n")

#ループを抜けたとき、どちらかのスコアは必ず2点
if my_points == 2: #抜けた時点で自スコアが2点
    print('あなたの勝ちです！おめでとう！')
else: #抜けた時点で自スコアが2点未満
    print('あなたの負けです。')
