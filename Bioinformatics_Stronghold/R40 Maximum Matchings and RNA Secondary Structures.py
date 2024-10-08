from math import factorial


def problem(rna):
    a, u, g, c = map(rna.count, ["A", "U", "G", "C"])
    a = factorial(max(a, u)) / factorial(max(a, u) - min(a, u))
    b = factorial(max(g, c)) / factorial(max(g, c) - min(g, c))
    return a * b

if __name__ == '__main__':
    import doctest
    from os.path import dirname
    from util import parse_fasta

    doctest.testmod()

    dataset = open(dirname(__file__) + "/rosalind_mmch.txt").read()
    for name, rna in parse_fasta(dataset).iteritems():
        print(problem(rna))
