# Grupo: Celenny Cristhyne, Daniel Farias e João Neto Castro
# Problema 3:

sufixos = ['o', 'ei', 'ai', 'os', 'es', 'ais', 'a', 'e', 'i',
           'om', 'em', 'aem', 'ons', 'est', 'aist', 'am', 'im', 'aim']


def get_sufixo(palavra):
    sufixo_atual = ''
    for sufixo in sufixos:
        if palavra.endswith(sufixo) and len(sufixo) > len(sufixo_atual):
            sufixo_atual = sufixo
    return sufixo_atual


def e_verbo(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    sufixo = get_sufixo(palavra)
    len_sufixo = len(sufixo)
    consoante = palavra[-len_sufixo-1:-len_sufixo]
    return sufixo != '' and consoante.lower() not in vogais


def get_verbo(palavra):
    sufixo = get_sufixo(palavra)
    len_sufixo = len(sufixo)
    return palavra[0:-len_sufixo]+'en'


def get_tempo_verbal(palavra):
    tempos = ['presente', 'pretérito', 'futuro']
    sufixo = get_sufixo(palavra)
    index = sufixos.index(sufixo) % 3
    return tempos[index]


def get_pessoa_verbal(palavra):
    pessoas = ['1a', '2a', '3a', '4a', '5a', '6a']
    sufixo = get_sufixo(palavra)
    index = int(sufixos.index(sufixo) / 3)
    return pessoas[index]


def get_resultado_palavra(palavra):
    if not e_verbo(palavra):
        return "{} - não é um tempo verbal".format(palavra)

    verbo = get_verbo(palavra)
    tempo = get_tempo_verbal(palavra)
    pessoa = get_pessoa_verbal(palavra)

    return "{} - verbo {}, {}, {} pessoa".format(palavra, verbo, tempo, pessoa)


def main():
    while True:
        palavra = input()
        if palavra == '':
            break
        print(get_resultado_palavra(palavra))


if __name__ == '__main__':
    main()