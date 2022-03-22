# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 2:

def reverse_number(number):				
    return int(''.join(number[::-1]))

def main():
		while True:
				operation = input()
				numbers, result = operation.split("=")
				a, b = numbers.split("+")

				if(reverse_number(a) + reverse_number(b) == reverse_number(result)):
						print('V')
				else:
						print('F')
				
				if(operation == '0+0=0'):
						quit()

if __name__ == '__main__':
    main()