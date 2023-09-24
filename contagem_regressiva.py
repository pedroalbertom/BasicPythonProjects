import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60) #divmod pega o primeiro argumento e divide pelo segundo, retorna 2 valores, o primeiro valor é o resultado inteiro da divisao e o segundo valor é o resto, o valor inteiro vai ser atribuido para a variavel mins e o resto para a variavel secs
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\n")
        time.sleep(1)
        t -= 1
    print('Contagem regressiva efetuada!')
t = input('Tempo em segundos\n')

countdown(int(t))