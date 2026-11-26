import itertools as it

def pos_com(alm:int, grup:int):
    return list(it.combinations(range(1, alm + 1), grup))

if __name__ == '__main__':
    alm = int(input())
    grup = int(input())

    print(pos_com(alm,grup))

