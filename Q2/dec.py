ct = "Rex*cy*k*Hc~}cyo*Ezoxk~ced"


for i in range(1, 501):
	pt = []
	for char in ct:
		pt.append(chr(ord(char)^i))
	if ''.join(pt).startswith('X'):
		print(''.join(pt))