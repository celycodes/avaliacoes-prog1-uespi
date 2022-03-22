# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 4:

def main():
    cont = 0
    while True:
        num = int(input())
        if (num == 0):
            quit()

        j1 = input()
        j2 = input()
        resp = list()

        i = 0
        for i in range(i, num):
            n1, n2 = map(int, input().split())
            s = n1+n2

            if (s % 2 == 0):
                resp.append(j1)
            else:
                resp.append(j2)

        cont += 1
        print(f'Teste {cont}')
        for j in resp:
            print(j)

        print()


if __name__ == '__main__':
    main()
