# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 5

def solve_test_case():
    n = int(input())
    current = 1
    total = 0
    for i in range(n):
        total += current
        current *= 2
    total_in_kg = int(total/12/1000)

    print("{} kg".format(total_in_kg))


def main():
    try:
        test_case_quant = int(input())
        for i in range(test_case_quant):
            solve_test_case()
    except EOFError:
        return


if __name__ == '__main__':
    main()
