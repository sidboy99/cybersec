from factordb.factordb import FactorDB

n = 19473790491178967371
e = 17
ct = 8925700648516910493

f = FactorDB(n)
f.connect()
phi = (f.get_factor_list()[0]-1)*(f.get_factor_list()[1]-1)
d = pow(e, -1, phi)
pt = pow(ct, d, n)
print(pt)