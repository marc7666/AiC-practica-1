# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

import read_file
import calculs

if __name__ == "__main__":

    values, n, h, alpha, beta = read_file.read_file("aqueductes/secret-02.in", data_separation=" ")



    print(calculs.costsAque(n, alpha, beta, h, values))
    print(calculs.costPont(n, alpha, beta, h, values))
