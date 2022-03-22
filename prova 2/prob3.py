# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 3:

def checkIfExistDuplicates(number):
		status = False
		chars = list()

		for n in number:
			if (n in chars):
				status = True
				break
			else:
				chars.append(n)

		return status

def main():
		while True:
			try:
				start, end = map(int, input().split())

				if (start == end == 0):
					quit()
				
				numbers = list(range(start, end + 1))
				filtered_numbers = list()

				for number in numbers:
					if (not checkIfExistDuplicates(str(number))):
						filtered_numbers.append(number)
		
				print(len(filtered_numbers))
			except EOFError:
					return

if __name__ == '__main__':
    main()
