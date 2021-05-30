# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************
import argparse

import read_file
import calculs

'''
Main function of the iterative version of the practical case
'''

if __name__ == "__main__":
    #parser = argparse.ArgumentParser(description='calculs')
    #parser.add_argument('testing', help='Fichero del aqueducto')
    #argumento = parser.parse_args()
    i = 1
    for i in range(i,21):
        if i < 10:
            num = "0"+str(i)
            fitx = "aqueductes/secret-" + num + ".in"
        else:
            num = str(i)
            fitx = "aqueductes/secret-" + num + ".in"
        values, n, h, alpha, beta = read_file.read_file(fitx, data_separation=" ")

        cost = calculs.calculate(n, alpha, beta, h, values)
        print("---------------------------------------")
        print("Fitx",fitx)
        print("---------------------------------------")
        print("Resultado introducido en el output.ans")
        print("---------------------------------------")
        print("Resultado: ", cost)
        print("-------------------------")
        file_ans = open('output.ans', 'w')
        file_ans.write(str(cost) + '\n')
        file_ans.close()
        fitx = "aqueductepont/secret-" + num + ".ap.ans"

        with open(fitx) as a:
            contentA = set(a)

        with open("output.ans") as b:
            contentB = set(b)

        if contentB == contentA:
            print("OK")
