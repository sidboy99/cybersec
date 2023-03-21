ct = "SYNT{Oehgrsbepr_vf_Rnfl}"

for shift in range(0,26):
    shifted = ""
    for char in ct:
        if char.islower():
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            shifted = shifted + shifted_char
        elif char.isupper():
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            shifted = shifted + shifted_char
        else:
            shifted = shifted + char
    print(shift, shifted)