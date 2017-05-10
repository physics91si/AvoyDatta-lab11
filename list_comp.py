import string


def main():
	alphabet = string.ascii_lowercase

	listTenLetters = [char for char in alphabet if alphabet.index(char) < 10] 
	#returns first 10 letters

	listTenLettersExceptSixth = [char for char in alphabet if alphabet.index(char) < 10 and alphabet.index(char) != 5] 
	#returns first 10 letters except 'f'

	repeatTenExceptSixth = sorted([char for char in alphabet if alphabet.index(char) < 10 and alphabet.index(char) != 5] * 3)
	#returns first 10 letters repeated, doesnt return f

	repeatTenExceptSixthGrid = [[c, c*2, c*3] for c in [char for char in alphabet if alphabet.index(char) < 10 and alphabet.index(char) != 5] ]
	#returns first 10 letters repeated, doesnt return f; returns in a grid
	print(repeatTenExceptSixthGrid)

	repeatTenExceptSixthGridCap = [[str.upper(c), c*2, c*3] for c in [char for char in alphabet if alphabet.index(char) < 10 and alphabet.index(char) != 5] ]
	#returns first 10 letters repeated, doesnt return f; returns in a grid, first char in each grid Capitalized
	print(repeatTenExceptSixthGridCap)

main()
