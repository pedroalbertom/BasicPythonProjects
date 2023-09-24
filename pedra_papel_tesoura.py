import random

def play():
    jogar = True
    while jogar:
        user = input("Escolha: 'r' para pedra, 'p' para papel ou 't' para tesoura\n").lower()
        computer = random.choice(['r', 'p', 't']) #aleatoriamente escolhe um elemento dessa lista
        
        # r > t, t > p, p > r
        if user == computer:
            print(f'Empate! O computador também escolheu: {computer}')
        elif is_win(user, computer):
            print(f'Você ganhou! O computador escolheu: {computer}')
        else:
            print(f'Você perdeu! O computador escolheu: {computer}')
        
        alternativa = input("Quer jogar novamente? 's' para sim ou 'n' para não\n")
        if alternativa == 's':
            jogar = True
        elif alternativa == 'n':
            jogar = False
            return print('Até a próxima')
        else:
            print("Alternativa inválida, o jogo será finalizado")
            jogar = False
            return print('Até a próxima')
def is_win(player, opponent): #retorna true se player ganha
    if (player == 'r' and opponent == 't') or (player == 't' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False
    
play()

