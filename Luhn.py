#LuhnValid:
#Função que usa o algoritmo de Luhn para validar numeros (cartão de crédito, or exemplo)
#Parametro 'num' deve ser informado como string. Os caracteres '.' (ponto) e ' ' (espaço) são aceitos, porém nenhum outro caracter, somente numeros.
#Retorna 1 se o numero é válido,
# retorna 0 se o numero não é válido
# e retorna -1 em caso de erro (se for informado caracteres não numéricos, se o numero informado é menor que 2 caracteres ou se o parametro não for uma string)

import os
import json



def LuhnValid (num):

	if isinstance(num,str) == False:
		return -1
		
	num = num.replace(" ", "")
	num = num.replace(".", "")

	if num.isdecimal() and len(num)>2:
		numtrim = []
		
		for counter in range(len(num)):
			numtrim.append(int(num[counter]))
			
			if (counter == 0) or (counter%2 == 0):
				numtrim[counter] = numtrim[counter]*2
				
				if(numtrim[counter]>9):
					numtrim[counter] = numtrim[counter]-9
					
		numsum = 0
		
		for counter2 in range(len(numtrim)):
			numsum = numsum + numtrim[counter2]
			
		if(numsum%10 == 0):
			return 1
		else:
			return 0
			
	else:
		return -1
#------------------------------------------------------------------------------------------------
#CardProvider:
#Função que verifica o numero do cartão e retorna o provedor do serviço de cartão em formato string
#Inclui apenas cartões de uso mais comum no Brasil
#Parametro 'num' deve ser informado como string. Os caracteres '.' (ponto) e ' ' (espaço) são aceitos, porém nenhum outro caracter, somente numeros.
	
	
def CardProvider (num, arq):
	
	if isinstance(num,str) == False:
		return "Erro! Numero de cartão fornecido não esta em formato string"
		
	num = num.replace(" ", "")
	num = num.replace(".", "")
	
	if os.path.exists(arquivo):
		with open(arquivo, "r") as arq_json:
			dicionario=json.load(arq_json)
	else:
		return "Erro! Arquivo JSON não encontrado"
	
	company_name = "Provedor do serviço de cartão não encontrado"
	for company, value in dicionario.items():
		dict2 = value[0]                       #Python salva a variável value como uma lista com um elemento dict. Portanto a variavel dict2 salva esse valor como dicionario
		for num_len, prefix in dict2.items():
			if len(num) == int(num_len):
				for digits in prefix:
					if num[:len(digits)] == digits:
						company_name = company
	
	return company_name
		
		