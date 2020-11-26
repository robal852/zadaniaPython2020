import math


# f1 = [-1, 2]  # -1/2
# f2 = [0, 1]  # zero
# f3 = [3, 1]  # 3
# f4 = [6, 2]  # 3 (niejednoznaczność)
# f5 = [0, 2]  # zero (niejednoznaczność)

def simplify(nominator, denominator):
    gcd = math.gcd(nominator, denominator)
    return [nominator / gcd, denominator / gcd]


def add_frac(frac1, frac2):
    '''frac1 + frac2'''
    nominator = frac1[0] * frac2[1] + frac1[1] * frac2[0]
    denominator = frac1[1] * frac2[1]
    return simplify(nominator, denominator)


def sub_frac(frac1, frac2):
    '''frac1 - frac2'''
    nominator = frac1[0] * frac2[1] - frac1[1] * frac2[0]
    denominator = frac1[1] * frac2[1]
    return simplify(nominator, denominator)


def mul_frac(frac1, frac2):
    '''frac1 * frac2'''
    nominator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    return simplify(nominator, denominator)


def div_frac(frac1, frac2):
    '''frac1 / frac2'''
    nominator = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[0]
    return simplify(nominator, denominator)


def is_positive(frac):
    '''bool, czy dodatni'''
    if frac[0] > 0:
        return True
    return False


def is_zero(frac):
    '''bool, typu [0, x]'''
    frac = simplify(frac[0], frac[1])
    return not bool(frac[0])


def cmp_frac(frac1, frac2):
    '''-1 | 0 | +1'''
    frac1 = simplify(frac1[0], frac1[1])
    frac2 = simplify(frac2[0], frac2[1])
    if frac1[0] == frac2[0] and frac1[1] == frac2[1]:
        return 0
    elif (frac1[0] / frac1[1]) > (frac2[0] / frac2[1]):
        return 1
    else:
        return -1


def frac2float(frac):
    '''konwersja do float'''
    return float(frac[0] / frac[1])
