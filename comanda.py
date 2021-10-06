#Dic with cod and name of the item
d1 = {100:"cachorro quente",101:"bauru simples",102:"bauru com ovo",103:"hamburguer",104:"cheeseburguer",105:"refrigerante"}

#Dic with the cod and price of the item
d2={100:1.20,101:1.30,102:1.50,103:1.50,104:1.30,105:1.00}

#start the variables
comanda={}
item=1
qtd=0
valor=0.0
pagamento=0
valpar=0.0

#Show the menu for the client
print("CARDÁPIO\n", "Cod.","Nome Item","     Preço")
for i in d1:
	print(i, d1[i],"- R$", d2[i])
	
#Ask the input of the client, while the user doesn't type 0 
while item != 0:
	item=int(input("Digite o código do item desejado(quando terminar o pedido digite 0): "))
	qtd=int(input("Digite a quantidade do item escolhido: "))
	
	#Update the dict with the order of the client
	if item != 0 and qtd != 0:
		comanda.update({item:qtd})
	else:
		pass	

#Print the order and the value of all itens
print("O pedido feito foi de: ")

for i in comanda:
	print(comanda[i], d1[i])

for i in comanda:
	valor=valor+comanda[i]*d2[i]
print("R$ ",valor)

#Asks the client the method of payment
pagamento=int(input("Selecione o métofo de pagamento\n1 - À vista\n2 - A prazo: "))

#If the payment is debit, conced 10% of discount
if pagamento == 1:
	valor = valor*0.9
	print('Total do pedido: R$ ', valor)

#If the payment is credit, but more than 3 installments add 10% in the price of the order
elif pagamento == 2:
	parcelas=int(input("Digite o numero de parcelas(acima de 3 parcelas haverá um acréscimo de 10%: "))
	if parcelas <= 3:
		valpar=valor/parcelas
	elif parcelas >3:
		valor=valor*1.1
		valpar=valor/parcelas
	print('Total do pedido: R$ ', valor, "em ", parcelas,"vezes")