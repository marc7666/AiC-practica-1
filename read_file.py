# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

def read_file(filename, data_separation=" "):
    print("************* READING DATA... *************")
    values = []  # List of tuples (x, y)
    # Openning file
    with open(filename, "r") as fn:
        # Strip lines
        strip_reader = (line.strip() for line in fn)
        filtered_reader = [line for line in strip_reader if line]
        # First line is the problem data
        n, h, alpha, beta = map(int, filtered_reader[0].split(data_separation))
        # Split lines, parse token and append to values (2 to last)
        for line in filtered_reader[1:]:
            x, y = map(int, line.split(data_separation))
            values.append((x, y))
        return values, n, h, alpha, beta

