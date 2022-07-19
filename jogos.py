import random
from stringprep import in_table_c21
import time

def jogo_1():
    while True:    
        computador = random.randint(1, 10)
        jogador = int(input('Digite um número: '))
        if jogador == computador:
            print('Você ganhou!!')
        else:
            print(f'Você perdeu!!\nO numero era {computador}')
        resp = input('Deseja continuar? S/N ').upper().strip()
        if resp in 'Ss':
            continue
        else:
            print('Saindo do game....')
            time.sleep(2)
            break

def jogo_2():
    socrates = 'Só sei que nada sei.'
    rene = 'Daria tudo que sei pela metade do que ignoro.'
    frases = [[socrates, '1'], [rene, '2']]
    computador = random.choice(frases)
    print(computador[0])
    print('Esta frase é de qual filósofo? ')
    print('1 = Sócrates ou 2 = René Descartes,')
    resp = (input())
    if resp in computador:
        print('Você ganhou!!')
    else:
        print('Você perdeu..Tente novamente')



def menu():
    while True:
        print('Jogos variados, escolha uma opçao: ')
        print('1. acertar o numero aleatório: ')
        print('2. Frases')
        opcao = int(input('digite um opçao: '))

        if opcao == 1:
            jogo_1()

        if opcao == 2:
            jogo_2()



menu()

