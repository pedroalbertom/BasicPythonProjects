# o computador vai adivinhar um número aleatório que o usuário quiser
import random

def guess(x,y):
    if x < y:
        feedback = ''
        while feedback != 'c':
            if x != y:
                guess = random.randint(x,y)
            else:
                guess = x #podia ser y também pq x e y são iguais
            feedback = input(f'{guess} é maior (H), menor (L) ou está correto? (C)?\n').lower()
            if feedback == 'h':
                y = guess - 1
            elif feedback == 'l':
                x = guess + 1 
        print(f'O computador acertou o número, {guess}\n')
    else:
        print(f'{x} é maior que {y}, tente novamente!\n')

guess(1,10000)