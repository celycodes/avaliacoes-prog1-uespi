# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 1:

def main():
    try:
        while True:
            n = int(input().strip())
            if (n == 0):
                quit()
            lista = list(map(int, input().split()))
            lista.sort()
            
            total = 0
            qtd = 1
            for i in range(len(lista)):
                if i != 0 and lista[i] > lista[i-1]:
                    qtd += 1
                total += qtd
            
            print(total)
    except EOFError:
        return

if __name__ == '__main__':
    main()