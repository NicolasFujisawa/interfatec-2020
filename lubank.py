config = {}
users = {}


def get_keys():
    for i in range(0, 12):
        entrada = input().split(";")
        tecla = entrada[0]
        teclas = entrada[1:]
        config[tecla] = teclas


def get_users():
    while(True):
        user, password = input().split(";")
        userLen = len(user)
        passwordLen = len(password)
        if(userLen >= 3 and passwordLen >= 3 and userLen <= 50 and passwordLen <= 60):
            if(user == "fim" and password == "fim"):
                break
            else:
                users[user] = {'senha': password, 'blocked': 0}


def verify_password(user, password):
    if(users[user]['blocked'] > 2):
        print('{}: usuario bloqueado'.format(user))
        return False
    senha = users[user]['senha']
    lenSenha = 0
    for i in range(0, len(password)):
        digit = password[i]
        if(i < len(senha) and senha[i] in config[digit]):
            lenSenha += 1
            continue
        else:
            users[user]['blocked'] += 1
            if(users[user]['blocked'] > 2):
                print('{}: usuario bloqueado'.format(user))
            else:
                print('{}: acesso negado'.format(user))
            return False
    if(lenSenha == len(senha)):
        users[user]['blocked'] = 0
        print('{}: acesso concedido'.format(user))
        return True
    else:
        users[user]['blocked'] += 1
        if(users[user]['blocked'] > 2):
            print('{}: usuario bloqueado'.format(user))
        else:
            print('{}: acesso negado'.format(user))
        return False


def try_login(user, password):
    if(user in users):
        verify_password(user, password)
    else:
        print('{}: usuario inexistente'.format(user))


def solution():
    get_keys()
    get_users()
    while True:
        login = ''
        try:
            login = input()
        except:
            break
        login = login.split(";")
        user = login[0]
        senha = login[1:]
        try_login(user, senha)


solution()
