# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

def read_file(filename, data_separation=" "):
    print("************* READING DATA... *************")
    values = []
    # Openning file
    with open(filename, "r") as fn:
        # Strip lines
        strip_reader = (line.strip() for line in fn)
        # Filter empty lines
        filtered_reader = [line for line in strip_reader if line]
        # Skip first line if needed
        n, h, alpha, beta = map(int, filtered_reader[0].split(data_separation))
        # Split line, parse token and append to values
        for line in filtered_reader[1:]:
            x, y = map(int, line.split(data_separation))
            values.append((x, y))
        return values, n, h, alpha, beta


def filter_token(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token
