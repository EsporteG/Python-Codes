# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:54:57 2021

@author: gusta
"""

def processInput (x):

    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    L = []
    L = (x.split())
    LS=[]
    string = str()
    for i in range(len(L)):
        LS.append(list(L[i]))

   
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == 'Z': 
                LS[i][j] = 'C'
            elif L[i][j] == 'Y':
                LS[i][j] = 'B'  
            elif L[i][j] == 'X':
                LS[i][j] = 'A'  

            else:
                for k in range(len(alfabeto)):
                    if LS[i][j] == alfabeto[k]:
                        LS[i][j]=alfabeto[k+3]
                        break
                    
    for l in range(len(LS)):
        if string == "":
            string = (",".join(LS[l])).replace(",","")
        else:
            string = string + " "+ (",".join(LS[l])).replace(",","")
            
    return string


#Este e um exemplo de processamento de entradas (inputs), sinta-se a vontade para altera-lo conforme necessidade da questao.
value = input("DIGITE EM LETRAS MAIÚSCULAS O TEXTO A SER ENCRIPTADO: ")
while (value):
    print(processInput(value))
    try:
        value = input("DIGITE EM LETRAS MAIÚSCULAS O TEXTO A SER ENCRIPTADO: ")
    except EOFError:
        break