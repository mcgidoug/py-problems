string = "1,2,3,4"


def array(string):
    seq = string.split(",")

    if len(seq) <= 2:
        return None

    new = " ".join(seq[1:-1])
    return new


print(array(string))
