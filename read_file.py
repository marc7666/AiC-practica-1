# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

def read_file(filename, data_separation=" ", first_line=False):
    print("************* READING DATA... *************")
    values = []
    # Openning file
    with open(filename, "r") as fn:
        # Strip lines
        strip_reader = (line.strip() for line in fn)
        # Filter empty lines
        filtered_reader = (line for line in strip_reader if line)
        # Skip first line if needed
        if first_line:
            next(filtered_reader)
        # Split line, parse token and append to values
        for line in filtered_reader:
            values.append(
                [filter_token(token) for token in line.split(data_separation)]
            )
        return values


def filter_token(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token
