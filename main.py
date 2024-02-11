import os
import random
import sys
import numpy as np


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAX_USER = 1000
RAND = random.Random(1234)


def parse_user(line):
    return int(line[2:])


def parse_click(line):
    return int(line[2:])


def select_ad(user, n, m, summary, user_segment, total):
    """
    user: user_id
    m: numbers of ads
    summary: List[List[int]]: user_id, ad_id, number of displays, clicks
    total: n, m, 2
    """        
    start = (user - 1) * m
    end = user * m
    user_ab = np.array([row[2] for row in summary[start:end]])
    user_a = np.array([row[3] for row in summary[start:end]])
    total_ab = np.array([model[0] for model in total[user_segment[user]-1]])
    total_a = np.array([model[1] for model in total[user_segment[user]-1]])
    total_sum = np.sum(total_ab) + 0.1
    total_ab = total_ab / total_sum
    total_a = total_a / total_sum

    gamma_ab = 1
    miu_ab = 5000

    alph = user_a * gamma_ab + 0.5 + miu_ab * total_a
    beta_ = (user_ab - user_a) * gamma_ab + 1 + miu_ab * (total_ab - total_a)
    ad = np.argmax(np.random.beta(alph, beta_)) + 1
    return ad


def update_summary(user, m, ad, click, summary, user_segment, total):
    """
    with info(ad, click), for (user, m), update summary
    """
    row = (user - 1) * m + ad - 1
    summary[row][2] += 1
    summary[row][3] += int(click)
    total[user_segment[user]-1][ad-1][0] += 1 
    total[user_segment[user]-1][ad-1][1] += int(click)


def send_msg(msg):
    print(msg)
    sys.stdout.flush()


def read_user_segment():
    with open(os.path.join(BASE_DIR, "data", "segments.csv"), "rt") as f:
        lines = [line.rstrip().split(",") for line in f.readlines()]
        user_segment = [(
            int(line[0]),  # ユーザID / User ID
            int(line[1])   # セグメントID / Segment ID
        ) for line in lines]
    return dict(user_segment)


def read_summary():
    with open(os.path.join(BASE_DIR, "data", "summary.csv"), "rt") as f:
        lines = [line.rstrip().split(",") for line in f.readlines()]
        summary = [[
            int(line[0]),  # ユーザID / User ID
            int(line[1]),  # アドID / Ad Id
            int(line[2]),  # 表出数 / Impressions
            int(line[3])   # クリック数 / Clicks
         ] for line in lines]
    return summary


def main():
    n, m = map(int, input().split())
    user_segment = read_user_segment()
    summary = read_summary()

    total = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    for u in range(len(user_segment)):
        for i in range(m):
            row = u * m + i
            total[user_segment[u + 1] - 1][i][0] += summary[row][2]
            total[user_segment[u + 1] - 1][i][1] += summary[row][3]

    while True:
        line = input()
        if line == "bye":
            break
        user = parse_user(line)
        assert (1 <= user <= MAX_USER)
        ad = select_ad(user, n, m, summary, user_segment, total)
        send_msg("a:{}".format(ad))
        click = parse_click(input())
        assert (0 <= click <= 1)
        update_summary(user, m, ad, click, summary, user_segment, total)


if __name__ == '__main__':
    main()
