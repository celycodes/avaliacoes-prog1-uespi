# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 2:

def get_factorial(number):
	sum, i = 1, 1

	while i <= number:
		sum *= i
		i += 1
		
	return sum

def main():
	while True:
		number = input()
			
		if (number == '0'):
			quit()

		length = int(len(number))
		number_converted = 0

		for a in number:
			factorial = get_factorial(length)
			number_converted += int(a) * factorial
			length = length - 1
			
		print(number_converted)

if __name__ == '__main__':
  main()