from specie     import *

#########FUNCIONES PRIVADAS
def juntar(kmer1, kmer2):
    it1 = 0
    it2 = 0
    llaves1 = sorted(kmer1.keys())
    llaves2 = sorted(kmer2.keys())
    conjunto = []
    while it1 < len(llaves1) and it2 < len(llaves2):
        if llaves1[it1] < llaves2[it2]:
            conjunto.append((kmer1[llaves1[it1]],0))
            it1 += 1
        elif llaves1[it1] > llaves2[it2]:
            conjunto.append((0,kmer2[llaves2[it2]]))
            it2 += 1
        else:
            conjunto.append((kmer1[llaves1[it1]],kmer2[llaves2[it2]]))
            it1 += 1
            it2 += 1
    while it1 < len(kmer1):
        conjunto.append((kmer1[llaves1[it1]], 0))
        it1 += 1
    while it2 < len(kmer2):
        conjunto.append((0, kmer2[llaves2[it2]]))
        it2 += 1
    return conjunto

def intersection(conjunto):
    numero = 0
    for par in conjunto:
        one = par[0]
        two = par[1]
        if one < two:
            numero += one
        else:
            numero += two
    return numero

def unionmap(conjunto):
    numero = 0
    for par in conjunto:
        one = par[0]
        two = par[1]
        if one > two:
            numero += one
        else:
            numero += two
    return numero


#########FUNCIONES PÚBLICAS
class Cjt_Species:
    def __init__(self):
        self.ssp = []
        self.dist = []
        self.modified = False

    def add_specie(self, specie):
        if specie not in self.ssp:
            self.ssp.append(specie)
            self.modified = True
            return 1
        else:
            return -1

    def print_dna(self, name):
        existe = False
        for i in range(len(self.ssp)):
            if self.ssp[i].name == name:
                existe = True
                break
        if existe:
            return self.ssp[i].dna
        else:
            devuelta = "-1"
            return devuelta

    def distance(self, name1, name2):
        kmer1 = -1
        kmer2 = -1
        for i in range(len(self.ssp)):
            if self.ssp[i].name == name1:
                kmer1 = i
            if self.ssp[i].name == name2:
                kmer2 = i
        if kmer1 == -1 or kmer2 == -1:
            return "-1"
        kmer1 = self.ssp[kmer1].kmer
        kmer2 = self.ssp[kmer2].kmer
        conjunto = juntar(kmer1, kmer2)
        ene1 = intersection(conjunto)
        ene2 = unionmap(conjunto)
        num = ((1 - (ene1 / ene2)) * 100)
        num = round(num, 3)
        return num

    def deletos(self, name):
        encontrada = False
        fuera = None
        for i in range(len(self.ssp)):
            if self.ssp[i].name == name:
                encontrada = True
                fuera = i
                break
        if encontrada:
            self.ssp.pop(fuera)
            self.modified = True
            return 1
        else:
            return -1

    def full_deletos(self):
        i = 0
        self.modified = True
        while i < len(self.ssp):
            self.ssp.pop(i)

    def esiste(self, name):
        for i in range(len(self.ssp)):
            if self.ssp[i].name == name:
                return True
        return False

    def get_cjt(self):
        lista = []
        for especie in self.ssp:
            lista.append((especie.name.lower(), especie.dna.lower()))
        return lista

    def make_matrix(self):
        dist = []
        for i in range(len(self.ssp)-1):
            dist.append([])
            j = i +1
            while j < len(self.ssp):
                kmer1 = self.ssp[i].kmer
                kmer2 = self.ssp[j].kmer
                conjunto = juntar(kmer1, kmer2)
                ene1 = intersection(conjunto)
                ene2 = unionmap(conjunto)
                num = ((1 - (ene1 / ene2)) * 100)
                num = round(num, 3)
                dist[i].append(num)
                j += 1
        return dist

    def matrix_distance(self):
        if self.modified:
            self.dist = self.make_matrix()
            self.modified = False
        return self.dist