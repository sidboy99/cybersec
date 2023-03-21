alpha_to_num = {}
num_to_alpha = {}

for i in range(ord('A'), ord('Z')+1):
    temp = {i-ord('A'): chr(i)}
    num_to_alpha.update(temp)
    temp = {chr(i): i-ord('A')}
    alpha_to_num.update(temp)


ct = 'BQOSRU'
pt = 'PILANI'
keys = []

for k in range(0, 26):
    decrypted = []
    for x,y in zip(ct,pt):
        decrypted_letter = (alpha_to_num.get(x) - k + 26) % 26
        decrypted.append(num_to_alpha.get(decrypted_letter))
    loc = 0
    for letter, decrypted_letter in zip(pt,decrypted):
        if letter == decrypted_letter:
            keys.append((k, decrypted, loc))
        loc += 1

sorted_keys = sorted(keys, key=lambda l: l[2])

for key, value, loc in sorted_keys:
    print(num_to_alpha.get(key), end="")