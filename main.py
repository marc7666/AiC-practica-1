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

    fitOutput = open('output.ans', 'w')
    fitOutput.write(str(cost) + '\n')
    fitOutput.close()
