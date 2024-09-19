#Exercício 2: Solicitando Dados com input() 2 Pontos
#Crie um programa que pergunte ao usuário seu nome, sua idade e sua cidade usando a função input(). 
# Em seguida, exiba uma mensagem formatada com esses dados usando print(). # type: ignore
#
#Exemplo de Entrada:
#
#Qual é o seu nome? Ana 
#Quantos anos você tem? 25 
#De qual cidade você é? São Paulo
#
#Exemplo de Saída:
#Olá, Ana! Você tem 25 anos e é de São Paulo.


nome = input("Qual o seu nome? ")
idade = input("Que idade tem? ")
cidade = input("De que cidade é? ")

print("Olá, " + nome + "!" + " Você tem " + idade + " anos" + " e é de " + cidade + "." )

