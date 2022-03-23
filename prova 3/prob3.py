# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 3:

def solve_test_case(n,m):
    total = {}
    for i in range(n):
        ranking = list(map(int, input().split()))
        for player in ranking:
            total[player] = total[player] + 1 if player in total else 1

    positions = list(total.values())
    positions.sort()
    best_player_times = positions.pop()
    positions_filtered = list(filter(lambda views: views != best_player_times, positions))
    second_best_player_times = positions_filtered.pop()

    second_bests = []
    for key in total:
        if total[key] == second_best_player_times:
            second_bests.append(key)
    second_bests.sort()
    print(' '.join(list(map(str, second_bests))))

def main():
    while True:
        n, m = map(int, input().split())
        if n == m == 0:
            return
        solve_test_case(n,m)

if __name__ == '__main__':
    main()
