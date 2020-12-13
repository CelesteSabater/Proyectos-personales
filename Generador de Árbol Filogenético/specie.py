class Specie:
    def __init__(self, name, dna, k):
        self.name = name
        self.dna = dna
        self.kmer = self.generate_kmer(dna, k)

    def generate_kmer(self, dna, k):
        conjuntos = []
        for i in range(len(dna)-k+1):
            letras = ""
            for j in range(i, i+k):
                letras = letras + dna[j]
            conjuntos.append(letras)
        kmer = {}
        for letras in conjuntos:
            if letras in kmer.keys():
                kmer[letras] += 1
            else:
                kmer[letras] = 1
        conjunto = {}
        for letras in sorted(kmer.keys()):
            conjunto[letras] = kmer[letras]
        return conjunto