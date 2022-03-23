# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 2:

def get_number(letter):
  assigns = {
    1: ['a', 'j', 's'],
    2: ['b', 'k', 't'],
    3: ['c', 'l', 'u'],
    4: ['d', 'm', 'v'],
    5: ['e', 'n', 'w'],
    6: ['f', 'o', 'x'],
    7: ['g', 'p', 'y'],
    8: ['h', 'q', 'z'],
    9: ['i', 'r'],
  }

  for key in list(assigns.keys()):
    if (letter in assigns[key]):
      return key

  return 0

def sum_digits(number):
  if (number) < 10:
    return number
  else:
    sum = 0
    for char in str(number):
      sum += int(char)

    return sum_digits(sum) 

def main():
	try:
		while True:
			name = ((input()).replace(" ", "")).lower()
			number = 0

			for char in name:
				number += get_number(char)

			print(sum_digits(number))
	except EOFError:
		return

if __name__ == '__main__':
    main()