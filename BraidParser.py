
def parse(string: str):
    tuples_strings = string.split("/")
    tuples = []
    for s in tuples_strings:
        tup = s.split(",")
        tuples.append( (int(tup[0]), int(tup[1])) )
    return tuples
