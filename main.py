# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

import read_file
import calculs

if __name__ == "__main__":

    values, n, h, alpha, beta = read_file.read_file("testing/test5-7.in", data_separation=" ")
    print(values)
    print(h)
    print(alpha)
    print(beta)
    d, alt, disX=calculs.obtainValues(values)
    print(" d",d, " alt", alt, " disX ", disX)
    print(calculs.calculate(n, alpha, beta, h, values))
