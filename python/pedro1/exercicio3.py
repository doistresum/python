#Exercício 3: Coletando Informações com input() 2 Pontos
#Crie um programa que pergunte ao usuário o nome de seu filme, livro e música favoritos usando a função input(). 
# Em seguida, exiba uma frase formatada com essas informações usando print().
#
#Exemplo de Entrada:

#Qual é o seu filme favorito? Matrix 
#Qual é o seu livro favorito? O Pequeno Príncipe 
#Qual é a sua música favorita? Imagine

#Exemplo de Saída:
#Seu filme favorito é "Matrix", seu livro favorito é "O Pequeno Príncipe" e sua música favorita é "Imagine".

filme = input("Qual é o seu filme favorito? ")
livro = input("Qual é o seu livro favorito? ")
musica = input("Qual é a sua música favorita?")

print("O seu filme favorito é " + filme + "," + " o seu livro favorito é " + livro + " e a sua música favorita é a " + musica + "." )