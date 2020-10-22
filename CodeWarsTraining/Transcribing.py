import string


def DNA_strand(dna):

    old_dna = str(dna)
    new_dna = []

    for string in dna:
        if string == "A":
            new_dna.append("T")
        if string == "T":
            new_dna.append("A")
        if string == "C":
            new_dna.append("G")
        if string == "G":
            new_dna.append("C")
    return '{}'.format(''.join(new_dna))


### OR ###


def DNA_strand1(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))


### OR ###


def DNA_strand2(dna):
    pairs = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join([pairs[x] for x in dna])


print(DNA_strand2("ATTGC"))


