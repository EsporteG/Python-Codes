import itertools

l = input("Digite os números que deseje montar seu jogo separados por vírgula: ")

n = input("Digite a quantidade de numeros por combinaçao: ")

n=int(n)

a=l.split(',')

comb = list(itertools.combinations(a, n))

print("A quantidade de jogos gerados foram: ",len(comb))
print("Preço total de fazer ", len(comb), " jogos de Mega-Sena é: R$", len(comb)*4.5)

for i in enumerate(comb):
	print(i)

