from ast import While
import random
import time

def linha(tam=42):
    return '-'*tam


def jogo_1():
    while True:    
        computador = random.randint(1, 10)
        jogador = int(input('Digite um número de 1 a 10: '))
        if jogador == computador:
            print('\033[32mVocê ganhou!!\033[m')
        else:
            print(f'\033[31mVocê perdeu!!\033[m\nO numero era {computador}')
        resp = input('Deseja continuar? S/N ').upper().strip()
        if resp in 'Ss':
            continue
        else:
            print('Saindo do game....')
            time.sleep(0.5)
            break

def jogo_2():
    while True:
        socrates = ['Só sei que nada sei.', 'Sábio é aquele que conhece os limites da própria ignorância.','A vida irrefletida não vale a pena ser vivida','Existe apenas um bem, o saber, e apenas um mal, a ignorância.']
        rene = ['Daria tudo que sei pela metade do que ignoro.','Penso, logo existo.','O bom senso é a coisa do mundo melhor partilhada.','Não existem métodos fáceis para resolver problemas difíceis.']
        platão = ['Quem comete uma injustiça é sempre mais infeliz que o injustiçado', 'Tente mover o mundo – o primeiro passo será mover a si mesmo.','Não espere por uma crise para descobrir o que é importante em sua vida','O livro é um mestre que fala, mas que não responde.']
        frases = [['Sócrates',socrates, '1'], ['René Desacartes',rene, '2'], ['Platão',platão, '3']]
        ran = random.choice(frases)
        computador = random.choice(ran[1])
        print(linha())
        print(f'\033[33m"{computador}"\033[m')
        print('\033[35mEsta frase é de qual filósofo?\033[m')
        print(linha())
        c = 1
        for f in frases:
            print(f'{c} = {f[0]}')
            c += 1
        print(linha())
        resp = (input())
        if resp in ran:
            print('\033[32mVocê acertou!!\033[m')
        else:
            print('\033[31mVocê errou!..Tente novamente\033[m')    
        perg = str(input('Quer tentar jogar denovo? S/N ')).upper()
        if perg not in 'Ss':
            break
        print(linha())


def menu():
    while True:
        opcoes = ['Número aleatório','Frases', 'Sair']
        print('Jogos variados, escolha uma opçao: ')
        c = 1
        for op in opcoes:
            print(f'{c} - \033[36m{op}\033[m')
            c += 1
        opcao = int(input('digite um opçao: '))
        if opcao == 1:
            jogo_1()
        if opcao == 2:
            jogo_2()
        if opcao == 3:
            break

menu()