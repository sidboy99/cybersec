from random import *
random_number=randint(1,500)
flag="<<<FIND OUT>>>"
ct=[]
for f in flag:
   ct.append(str(ord(f)^random_number))
print(ct)
print(random_number)
ciphertext=[chr(int(x)) for x in ct]
output=''.join(ciphertext)
print(output)

#output=Rex*cy*k*Hc~}cyo*Ezoxk~ced
#number = <<<FIND OUT>>>

