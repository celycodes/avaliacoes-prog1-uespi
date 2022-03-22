# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 1

def get_last_soldier(soldiers, k):
    if len(soldiers) == 1:
        return '{}'.format(soldiers[0])
    current_kill = k-1
    while len(soldiers) > 1:
        soldiers.pop(current_kill)
        current_kill += k - 1
        if current_kill > len(soldiers) - 1:
            current_kill %= len(soldiers)
    return '{}'.format(soldiers[0])


def resolve_input(str):
    n, k = list(map(int, str.split()))
    soldiers = list(range(1, n+1))
    last_soldier = get_last_soldier(soldiers, k)

    return '{}'.format(last_soldier)


def main():
    quant = int(input())
    for i in range(quant):
        try:
            print(resolve_input(input()))
        except EOFError:
            return


if __name__ == '__main__':
    main()
