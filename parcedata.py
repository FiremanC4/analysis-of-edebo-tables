import json

FILE = '' #name of file to be generated

users = []

with open('inp.txt', 'r', encoding='utf-8') as f:
    for line in f:
        t_users = json.loads(line)["requests"]
        users.extend(t_users)
        del t_users

to_write = {"requests": users}

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(json.dumps(to_write))