# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 5

def solve_test_case():
    n, d = map(int, input().split())
    if n == d == 0:
        raise EOFError()
    valid_dates = []
    for i in range(d):
        arr = input().split()
        date = arr.pop(0)
        if '0' not in arr:
            day, month, year = map(int, date.split('/'))
            valid_dates.append('{}/{}/{}'.format(year, month, day))
    if len(valid_dates) == 0:
        return 'N/P'
    valid_dates.sort()
    year, month, day = valid_dates[0].split('/')
    return '{}/{}/{}'.format(day, month, year)


def main():
    try:
        while True:
            print(solve_test_case())
    except EOFError:
        return


if __name__ == '__main__':
    main()
