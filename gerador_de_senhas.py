import random

def senhas(number, length):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()0123456789'
    for n in range(number):
        senhas = ''
        for l in range(length):
            senhas += random.choice(chars)
        print(senhas)

print('===================================\nBem vindo ao seu gerador de senhas.\n===================================\n\n')

number = int(input('Quantas senhas você precisa?\n'))
length = int(input('Qual o tamanho da senha?\n'))

print('Aqui estão suas senhas:')

senhas(number, length)