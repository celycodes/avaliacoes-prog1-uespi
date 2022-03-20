# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 4:

def e_m(listas):
    resto = listas[0][0] % 2

    for lista in listas:
        for n in lista:
            if n % 2 != resto:
                return False
        resto = 1 if resto == 0 else 0
    return True


def get_m(lista):
    m = 1
    total = 0
    listas = []
    while total < len(lista):
        listas.append(lista[total:total+m])
        total += m
        m += 1
    return m-1 if e_m(listas) else 0


def get_resultado_str(lista):
    m = get_m(lista)
    if m == 0:
        return 'NAO'
    else:
        return m


def main():
    while True:
        quantidade = input()
        lista = input()
        fim = input()
        numeros = list(map(int, lista.split()))

        if fim == '%':
            if int(quantidade) == len(numeros):
                print(get_resultado_str(numeros))
                print('%')


if __name__ == '__main__':
    main()