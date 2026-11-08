
#Exercícios de Prática em Python (Sintaxe)


#8. Contagem Progressiva:  Escreva um loop  for  que imprima  os números de 1 a 10 no console
for i in range(1, 11):
    print(i)


#9. Contagem Regressiva:  Crie um loop que faça uma  contagem regressiva para o lançamento de um foguete, de 5 até 1, e termine imprimindo "Decolar!"
for i in range(5, 0, -1):
    print(i)
print("Decolar!")

#10. Tabuada do 2:  Use um loop para imprimir a tabuada  do número 2 (de 2x1 até 2x10)
for i in range(1, 11):
    print(f"2 x {i} = {2 * i}")

#11. Soma Acumulada:  Crie um script que use um loop  para somar todos os números de 1 a 5 e mostre o resultado final (1+2+3+4+5)
soma = 0
for i in range(1, 5):
    soma += i
print(f"A soma dos números de 1 a 5 é: {soma}")

#12. O Loop de Confirmação:  Use um  while  para pedir  ao usuário que digite "S" para continuar. O programa deve repetir a pergunta enquanto ele digitar qualquer outra coisa.
resposta = ""
while resposta != "S":
    resposta = input("Digite 'S' para continuar: ")

#13. Contagem de Itens:  Crie um loop que peça ao usuário para digitar 5 nomes de personagens e armazene-os em uma lista. Depois, imprima a lista completa.
personagens = []
for i in range(5):
    nome = input(f"Digite o nome do personagem {i + 1}: ")
    personagens.append(nome)
print("Lista de personagens:")
for personagem in personagens:
    print(personagem)

#14. Lista de Convidados:  Crie um loop que pergunte  o nome de 3 amigos e, ao final de cada entrada, imprima "[Nome] foi adicionado à guilda!"
convidados = []
for i in range(3):
    amigo = input(f"Digite o nome do amigo {i + 1}: ")
    convidados.append(amigo)
    print(f"{amigo} foi adicionado à guilda!")
