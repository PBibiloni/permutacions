import copy
import numbers


class Permutacio:

    def __init__(self, diccionari_assignacio=None):
        self.d = diccionari_assignacio or {}

    @staticmethod
    def de_cicles(*multiples_cicles):
        resultat = Permutacio()
        for c in multiples_cicles:
            d = {c[-1]: c[0]}
            for idx in range(1, len(c)):
                d[c[idx-1]] = c[idx]
            resultat = resultat * Permutacio(d)
        return resultat

    def llista_de_cicles(self):
        assignacio = copy.deepcopy(self.d)
        llista_cicles = []
        while assignacio:
            primer_item = min(assignacio.keys())
            item = assignacio.pop(primer_item)
            if primer_item != item:
                cicle = [primer_item]
                while item != primer_item:
                    cicle += [item]
                    item = assignacio.pop(item)
                llista_cicles += [tuple(cicle)]
        return llista_cicles

    def mostra_com_cicles(self):
        cicles = self.llista_de_cicles()
        if not cicles:
            return '()'
        return ', '.join([str(c) for c in cicles])

    def calcula_inversa(self):
        return Permutacio({v: k for k, v in self.d.items()})

    def __str__(self):
        return self.mostra_com_cicles()

    def __call__(self, item):
        try:
            return self.d[item]
        except KeyError:
            return item

    def __mul__(self, altre):
        # Composició començant per l'esquerra: primer aplicam self, després other.
        if not isinstance(altre, Permutacio):
            raise Exception('Només podem composar permutacions amb permmutacions!')
        composicio_assignacio = {}
        for item in self.d.keys():
            composicio_assignacio[item] = altre(self(item))
        for item in set(altre.d.keys()).difference(self.d.values()):
            composicio_assignacio[item] = altre(item)
        return Permutacio(composicio_assignacio)

    def __truediv__(self, altre):
        return self * altre.calcular_inversa()

    def exp(self, exponent):
        if not isinstance(exponent, int):
            raise Exception('Només podem composar permutacions un nombre enter de vegades')
        if exponent == 0:
            return Permutacio()
        permutacio_base = self if exponent > 0 else self.calcula_inversa()
        resultat = Permutacio()
        for i in range(abs(exponent)):
            resultat *= permutacio_base
        return resultat


