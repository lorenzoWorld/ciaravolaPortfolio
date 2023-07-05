import random
import re

def genera_password(lunghezza):
    caratteri = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                 '!£$%#&=?0123456789')
    while True:
        password = ''
        for i in range(0, int(lunghezza)):
            password += random.choice(caratteri)
        if valida_password(password):
            break
        else:
            print('{}: non valida, la scarto ..'.format(password))
    return password

def valida_password(password):
    condizione_valida = ('^.*(?=.{'+str(len(password))+',})(?=.*\d)(?=.*[a-z])'
                        '(?=.*[A-Z])(?=.*[!£$%&#=?]).*$')
    return re.findall(condizione_valida, password)


if __name__ == '__main__':
    lunghezza = input('lunghezza password -> ')
    password_generata = genera_password(lunghezza)
    print()
    print('Password generata: {}'.format(password_generata))
    
