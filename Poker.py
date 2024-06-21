from collections import Counter

### スート、ランク、役を変換する配列
suit = ["S", "C", "D", "H"]
rank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
hand = ["ロイヤルフラッシュ",
        "ストレートフラッシュ",
        "フォーカード",
        "フルハウス",
        "フラッシュ",
        "ストレート",
        "スリーカード",
        "ツーペア",
        "ワンペア",
        "ハイカード"]

### 手札出力
def print_cards(cards):
    for i in range(5):
        # print(cards[i][0], cards[i][1])
        print(suit[cards[i][0]] + rank[cards[i][1] - 1], end=" ")
    print()

### 役判定
def judge_hand(cards):
    # 手役管理用フラグ
    my_hand = [0] * 10

    sort_cards = sorted(cards)
    suits = []
    ranks = []
    for i in range(5):
        suits.append(sort_cards[i][0])
        ranks.append(sort_cards[i][1])
    s_suits = set(suits)
    s_ranks = set(ranks)

    # ロイヤルフラッシュ判定
    if sort_cards == [[0, 1], [0, 10], [0, 11], [0, 12], [0, 13]]:
        my_hand[0] = 1

    # ストレートフラッシュ、フラッシュ、ストレートの判定
    if len(s_suits) == 1:
        if len(s_ranks) == 5 and max(s_ranks) - min(s_ranks) == 4:
            my_hand[1] = 1
        elif s_ranks == {1, 10, 11, 12, 13}:
            my_hand[1] = 1
        else:
            my_hand[4] = 1
    else:
        if len(s_ranks) == 5 and max(s_ranks) - min(s_ranks) == 4:
            my_hand[5] = 1
        elif s_ranks == {1, 10, 11, 12, 13}:
            my_hand[5] = 1

    # フォーカード、フルハウス、スリーカード、ツーペア、ワンペアの判定
    if Counter(ranks).most_common()[0][1] == 4:
        my_hand[2] = 1
    elif Counter(ranks).most_common()[0][1] == 3 and Counter(ranks).most_common()[1][1] == 2:
        my_hand[3] = 1
    elif Counter(ranks).most_common()[0][1] == 3:
        my_hand[6] = 1
    elif Counter(ranks).most_common()[0][1] == 2 and Counter(ranks).most_common()[1][1] == 2:
        my_hand[7] = 1
    elif Counter(ranks).most_common()[0][1] == 2:
        my_hand[8] = 1
    elif Counter(ranks).most_common()[0][1] == 1:
        my_hand[9] = 1

    # 役を出力
    for flg in range(len(hand)):
        if my_hand[flg] == 1:
            print(hand[flg])
            break


### 標準入力を二次元配列で取得
cards = [[int(x) for x in input().split()] for i in range(5)]

### 手札と役を出力
print_cards(cards)
judge_hand(cards)