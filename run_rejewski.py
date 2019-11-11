from constants import *
from permutacions import Permutacio

# Fonts:
#   [1] Rejewski, M., Mathematical solution of the Enigma cipher, Cryptologia, 6(1), 8, 1982.
#   [2] Bauer, Craig P. Secret history: The story of cryptology. Chapman and Hall/CRC, 2016.
#       Capítol 8: World War II: The Enigma of Germany

# Wiring from plugboard to rotors: obtingut d'enigma comercial [2]
# No utilitzada a l'article de Rejewski [1], comentada (però NO utilitzada) al llibre de The Story of Cryptology [2]
H = Permutacio.de_cicles((a, j, p, r, d, l, z, f, m, y, s, k, q), (b, w), (c, u, g, n, x, t, e), (h, o, i), (v))

# Informacio comprada a l'espia Schmidt [2] (plug connections on the given day [1]), obtinguda de [1]
S = Permutacio.de_cicles((a, p), (b, l), (c, z), (f, h), (j, k), (q, u))


# Permutació de gir de rotor

P = Permutacio.de_cicles((a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z))

print(f''' Cicles coneguts
    P: {P}
    S: {S}
    H (no utilitzat): {H}
''')

# Productes AD, BE, CF: coincideixen tots [1, 2], els missatges de 6 lletres utilitzats per contruir-los semblen
# "reconstruits artificialment", apareixen a [2] (però no a [1], on es diu que aquest procediment és una simplifació!)

AD = Permutacio.de_cicles(
    (b, c),
    (r, w),
    (d, v, p, f, k, x, g, z, y, o),
    (e, i, j, m, u, n, q, l, h, t)
)
D = Permutacio.de_cicles(
    (a, s), (e, p), (i, v), (j, d), (m, o), (u, y), (n, z), (q, g), (l, x), (h, k), (t, f), (b, w), (c, r)
)
A = AD * D

BE = Permutacio.de_cicles(
    (h, j, p, s, w, i, z, r, n),
    (b, l, f, q, v, e, o, u, m),
    (c, g, y),
    (a, x, t)
)
B = Permutacio.de_cicles(
    (a, y), (x, g), (t, c), (b, j), (l, h), (f, n), (q, r), (v, z), (e, i), (o, w), (u, s), (m, p), (d, k)
)
E = B * BE

CF = Permutacio.de_cicles(
    (a, b, v, i, k, t, j, g, f, c, q, n, y),
    (d, u, z, r, e, h, l, x, w, p, s, m, o),
)
C = Permutacio.de_cicles(
    (a, x), (b, l), (v, h), (i, e), (k, r), (t, z), (j, u), (g, d), (f, o), (c, m), (q, s), (n, p), (y, w)
)
F = Permutacio.de_cicles(
    (a, w), (b, x), (v, l), (i, h), (k, e), (t, r), (j, z), (g, u), (f, d), (c, o), (q, m), (n, s), (y, p)
)


print(f'''
    A: {A}
    B: {B}
    C: {C}
    D: {D}
    E: {E}
    F: {F}
''')


# Expressions per U-Z de [1].

U = P.exp(-1) * S.exp(-1) * A * S.exp(+1) * P.exp(+1)
V = P.exp(-2) * S.exp(-1) * B * S.exp(+1) * P.exp(+2)
W = P.exp(-3) * S.exp(-1) * C * S.exp(+1) * P.exp(+3)
X = P.exp(-4) * S.exp(-1) * D * S.exp(+1) * P.exp(+4)
Y = P.exp(-5) * S.exp(-1) * E * S.exp(+1) * P.exp(+5)
Z = P.exp(-6) * S.exp(-1) * F * S.exp(+1) * P.exp(+6)

print(f'''
    U = {U}
    V = {V}
    W = {W}
    X = {X}
    Y = {Y}
    Z = {Z}
''')


print(f'''
    U*V: {U*V}
    V*W: {V*W}
    W*X: {W*X}
    X*Y: {X*Y}
    Y*Z: {Y*Z}
''')