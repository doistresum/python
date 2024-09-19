#Exercício 1: Cálculo de Média de Notas
#Descrição: Crie um programa que peça ao usuário um número n que representa a quantidade de notas a serem inseridas. 
# Em seguida, utilize um ciclo for para coletar n notas (valores entre 0 e 20) e calcule a média. 
# Se o usuário inserir uma nota fora do intervalo permitido, 
# exiba uma mensagem de erro e peça novamente até que a nota seja válida.
#Instruções:
#Solicite ao usuário o número de notas a serem inseridas (n).
#Use um ciclo for para solicitar as notas ao usuário.
#Verifique se a nota está dentro do intervalo válido (0 a 20). Se não estiver, exiba uma mensagem de erro e peça a nota novamente.
#Calcule e exiba a média das notas.

n = int(input("Digite o número de notas: "))
    
    
notas = []
contador = 0
    
    
while contador < n:
    nota = int(input("Digite uma nota entre 0 e 20: "))
    if 0 <= nota <= 20:
            notas.append(nota)
            contador += 1
            
    else:
        print("Nota inválida. Por favor, insira uma nota entre 0 e 20.")
    
   
    media = sum(notas) / n
    
    
    print(f"A média das notas é: {media:.1f}")
        

  










