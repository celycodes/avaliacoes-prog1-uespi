# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 1:

def main():
    while True:
        cod_ISBN = input().strip()
        if (cod_ISBN == '0-00000-000-0'):
            quit()

        numbers = list(cod_ISBN.replace('-', ''))
        invalido = False

        if len(numbers) != 10:
            invalido = True

        for n in numbers[:-1]:
            if not n.isnumeric():
                invalido = True

        if invalido:
            print(f'{cod_ISBN} está incorreto.')
            continue

        sum = 0
        s1_numbers = []
        s2_numbers = []
        result = ''

        for num in range(0, len(numbers)):
            # Se 'X' no digito ISBN
            if (numbers[num] == 'X'):
                numbers[num] = '10'

        # tranformar a lista de strings 'numbers' para int
        int_numbers = [int(i) for i in numbers]

        for num in int_numbers:
            # calculo do s1 (somas parciais)
            sum += num
            s1_numbers.append(sum)

        sum = 0

        for num in s1_numbers:
            # calculo do s2 (soma das somas parciais)
            sum += num
            s2_numbers.append(sum)

        for num in range(0, len(s2_numbers)):
            if (num == 9 and s2_numbers[num] % 11 == 0):
                result = 'correto'
            else:
                result = 'incorreto'

        print(f'{cod_ISBN} está {result}.')


if __name__ == '__main__':
    main()