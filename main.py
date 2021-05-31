# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************
import read_file
import calculs

if __name__ == "__main__":
    """
    Main function of the recursive version of the practical case
    """

    i = 1

    for i in range(i, 21):
        if i < 10:
            num = "0" + str(i)
            file = "aqueductes/secret-" + num + ".in"
        else:
            num = str(i)
            file = "aqueductes/secret-" + num + ".in"
        values, n, h, alpha, beta = read_file.read_file(file, data_separation=" ")

        cost = calculs.calculate(n, alpha, beta, h, values)
        print("---------------------------------------")
        print("Fitx", file)
        print("---------------------------------------")
        print("Resultado introducido en el output.ans")
        print("---------------------------------------")
        print("Resultado RECURSIVO: ", cost)
        print("-------------------------")
        file_ans = open('output.ans', 'w')
        file_ans.write(str(cost) + '\n')
        file_ans.close()
        file = "aqueductepont/secret-" + num + ".ap.ans"

        with open(file) as a:
            contentA = set(a)

        with open("output.ans") as b:
            contentB = set(b)

        if contentB == contentA:
            print("OK")
