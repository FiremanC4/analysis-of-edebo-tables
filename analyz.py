import json

FILE = '' #path to file generated via parcedata.py
KV = 200 #your competitive score
STAT = [0] * 5
KW_STAT = [0] * 5

def user_above(user):
    if user['kv'] > KV:
        return 'nokwota'
    elif len(user['rss']) == 4:
        return 'kwota'
    return False


def increse_stats(p, kw):
    global STAT, KW_STAT
    if not p:
        return
    
    if kw == 'kwota':
        for i in range(p, 6):
            KW_STAT[i-1] += 1

    elif kw == 'nokwota':
        for i in range(p, 6):
            STAT[i-1] += 1
            KW_STAT[i-1] += 1


with open(FILE, 'r', encoding='utf-8') as f:
    users = json.loads(f.read())["requests"]

for user in users:
    if kw := user_above(user):
        increse_stats(user['p'], kw)

print(
    f'з квотою: , без: \n{KW_STAT}{STAT}'
)