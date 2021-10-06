# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

palavra = str(input("Digite a palavra: "))
#palavra = "CELSOE"
palavra = palavra.strip()


qtdChar = int(len(palavra))
print(palavra)
resultado = "_" * qtdChar

resultadoForca = []
resultadoForca.extend(resultado)
palavraForca = []
palavraForca.extend(palavra)


chances = qtdChar + 3
while int(chances) > 0:
	if resultadoForca.count("_") == 0:
		print("Parabéns, você conseguiu advinhar a palavra da forca: {}" .format(palavra))
		exit()

	escolha = input("Inisira sua tentativa", )
	escolha = (escolha.strip())
	escolha = escolha[0]

	for x in palavraForca:
		#print(x, end="")
		if escolha == x:
			posicao = palavraForca.index(x)
			palavraForca[palavraForca.index(x)] = "*"

			resultadoForca[posicao] = escolha
			print("\n\n")
			print(" ".join(map(str, resultadoForca)))

	print("faltam {} tentativa(s)".format((chances) - 1))

	chances = chances - 1
	if (chances == 0):
		print("Game over |-_-|")