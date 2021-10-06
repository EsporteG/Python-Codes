from datetime import date, datetime

data_i = date.min.toordinal()
data_f = date.max.toordinal()
print('Formato da data: DD/MM/YYYY')
for i in range(data_f):
	data = data_i + i
	data_a = date.fromordinal(data)
	#print(data_a)
	data_string=data_a.strftime("%d-%m-%Y").replace('-','')
#	print(data_string)
#	print(data_string[::-1])
	if data_string==data_string[::-1]:
		print('Essa é uma data palíndroma:',data_a.strftime("%d/%m/%Y"))