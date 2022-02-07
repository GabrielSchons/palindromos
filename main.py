def Reconhecer_palindromo(palavra):
	if palavra == palavra[::-1]:
		return True
	else:
		return False

if __name__ == '__main__':
	palavra = input('Qual sua palavra?')
	definir_palindromo = Reconhecer_palindromo(palavra)
	if definir_palindromo:
		print(f'a palavra {palavra} é um palindromo!')
	else:
		print(f'a palavra {palavra} não é um palindromo!')
