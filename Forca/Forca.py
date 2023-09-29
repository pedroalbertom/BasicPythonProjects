import random
from palavras import palavras
import string

def get_valid_word(palavras):
    palavra = random.choice(palavras)
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)
    return palavra.upper()

def forca():
    palavra = get_valid_word(palavras)
    letras_palavra = set(palavra) #separa por letras a palavra escolhida
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set() # armazena as letras usadas pelo usuario
    vidas = 6
    
    #coletando entrada do usuário
    while len(letras_palavra) > 0 and vidas > 0:
        #letras usadas
        #' '.join(['a', 'b', 'c']) --> 'a b c'
        print('Você já utilizou essas letras: ', ' '.join(sorted(letras_usadas)))
        
        #palavra atual tipo: P - L A V R A
        lista_palavras = [letra if letra in letras_usadas else '-' for letra in palavra]
        print('Palavra atual: ', ' '.join(lista_palavras))
        print("--------------------------------------------------\n")
        
        
        letra_usuario = input('Chute uma letra: ').upper()
        if letra_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letra_usuario)
            if letra_usuario in letras_palavra:
                letras_palavra.remove(letra_usuario)
                print(f'Chutou certo, a letra {letra_usuario} está na palavra.')
            else:
                vidas = vidas - 1
                print(f'Chutou errado. Você tem {vidas} vidas.')
        elif letra_usuario in letras_usadas:
            print('Você já chutou essa letra. Tente novamente.')
            
        else:
            print('Letra inválida. Tente novamente.')
            
    if vidas == 0:
        print(f'Parabéns, voce acertou a palavra {palavra}')
    else:
        print(f'Infelizmente você perdeu, a palavra era: {palavra}')

forca()