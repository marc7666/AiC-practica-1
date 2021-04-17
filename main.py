# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************
import argparse

import read_file
import calculs

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='calculs')
    parser.add_argument('testing', help='Fichero del aqueducto')
    argumento = parser.parse_args()

    values, n, h, alpha, beta = read_file.read_file(argumento.testing, data_separation=" ")

    cost = calculs.calculate(n, alpha, beta, h, values)
    print("---------------------------------------")
    print("Resultado introducido en el output.ans")
    print("---------------------------------------")
    print("Resultado: ", cost)
    print("-------------------------")
    file_ans = open('output.ans', 'w')
    file_ans.write(str(cost) + '\n')
    file_ans.close()