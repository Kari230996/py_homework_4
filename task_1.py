# 1) Вычислить число c заданной точностью d

def calc(eps):
    s = 0
    d = 1
    sgn = 1
    while True:
        a = 4/d
        s = s + sgn * a
        if a < eps:
            return s
        sgn = -sgn
        d = d + 2

print(calc(1.0e-5))
