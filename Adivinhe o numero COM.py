# o computador vai ter um número aleatório escolhido e a gente tem que adivinhar
import random

def guess(x,y):
    if (x < y):
        random_number = random.randint(x, y) #random.randint(a,b) -> retorna um inteiro aleatório entre a e b
        guess = 0
        while guess != random_number:
            guess = int(input(f"Guess a number between {x} and {y}\n"))
            if guess > random_number:
                print(f"o número é menor que {guess}\n")
                y = guess - 1
            elif guess < random_number:
                print(f"o número é maior que {guess}\n")
                x = guess + 1
    else:
        print(f"{x} é maior que {y}, tente novamente!")
    
    print(f"Parabéns, {guess} é o número certo\n")

guess(1,100)