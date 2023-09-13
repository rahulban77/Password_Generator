


import random

pass_chars = []
pass_len_poss = []
pass_str = ""

print("Passowrd Suggesstion")

print("Select the Password Strength:\n 1.Weak\n 2.Medium\n 3.Strong")
a1 = int(input())

if a1==1:
    pass_len_poss.extend(range(4,8))
elif a1==2:
    pass_len_poss.extend(range(9,12))
elif a1==3:
    pass_len_poss.extend(range(13,15))

print("Do you want Uppercase Letters?")
a2 = input()

print("Do you want Lowercase Letters?")
a3 = input()

print("Do you want Digits?")
a4 = input()

print("Do you want Special Characters/Symbols?")
a5 = input()


if a2=='y':
    pass_chars.extend(range(65,91))
if a3=='y':
    pass_chars.extend(range(97,123))
if a4=='y':
    pass_chars.extend(range(48,58))
if a5=='y':
    pass_chars.extend([64,33,34,35,36,37,38,42,45])

a=random.choice(pass_len_poss)

i=1
while i<=a:
    pass_chr = chr(random.choice(pass_chars))
    pass_str = pass_str + pass_chr
    i+=1


print(pass_str)



