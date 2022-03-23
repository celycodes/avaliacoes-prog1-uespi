# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 4:
from math import floor, ceil

def main():
   while True:
      min = int(input())
      if (min == 0):
          quit()

      A = B = 0

      # a função ceil arredonda o valor para cima, até o inteiro mais próximo.
      A = ceil(7 * min / 90)
      # a função floor arredonda para baixo, até o inteiro mais próximo.
      B = floor(min / 90)

      print(f'Brasil {B} x Alemanha {A}')


if __name__ == '__main__':
    main()