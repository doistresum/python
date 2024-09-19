#Exercício 2: Jogo de Adivinhação com Tentativas Limitadas
#Descrição: Crie um programa onde o computador escolhe um número aleatório entre 1 e 50, e o usuário deve adivinhar qual é o número. O usuário tem um número limitado de tentativas (definido por uma variável max_tentativas). A cada tentativa, o programa deve informar se o número digitado é maior ou menor do que o número secreto. Se o usuário acertar ou esgotar as tentativas, o jogo termina.
#Instruções:
#Defina um número aleatório entre 1 e 50 usando random.randint(1, 50).
#Defina um número máximo de tentativas (max_tentativas).
#Use um ciclo while para permitir que o usuário adivinhe o número.
#Use if/else para verificar se o número inserido é maior, menor ou igual ao número secreto.
#Termine o jogo quando o usuário acertar ou esgotar as tentativas.

import random
num_secreto = random.randint(1, 50)
    
max_tentativas = 5
        
tentativas = 0

while tentativas < max_tentativas:
    palpite = int(input("Adivinhe o número (entre 1 e 50): "))
        
    if palpite == num_secreto:
        print("Acertou o número!")
        break
    
    elif palpite < num_secreto:
        print("O número secreto é maior...")
    
    else:
        print("O número secreto é menor...")
        
    tentativas += 1
    
if tentativas == max_tentativas and palpite != num_secreto:
    print(f"Esgotou as tentativas. O número secreto era {num_secreto}!")