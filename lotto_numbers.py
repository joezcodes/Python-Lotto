import random

LottoNum1 = input("Lotto Number1: ")
LottoNum2 = input("Lotto Number2: ")
LottoNum3 = input("Lotto Number3: ")
LottoNum4 = input("Lotto Number4: ")
LottoNum5 = input("Lotto Number5: ")
LottoNum6 = input("Lotto Number6: ")

a = [int(LottoNum1), int(LottoNum2), int(LottoNum3), int(LottoNum4), int(LottoNum5), int(LottoNum6)]

b = range(1,54)

c = [] #New range

d = [] # Picked numbers

#Pick #1
for num in b:
    if num not in a:
        c.append(num)
rand1 = random.choice(c) # entire range minus num
d.append(rand1) # adds rand1 to d

# Pick #2
for num2 in c:
    if num2 == rand1:
        c.remove(num2) # if num2 is in c remove it
rand2 = random.choice(c) 
d.append(rand2)

# Pick #3
for num3 in c:
    if num3 == rand2:
        c.remove(num3) 
rand3 = random.choice(c) 
d.append(rand3)

# Pick #4
for num4 in c:
    if num4 == rand3:
        c.remove(num4) 
rand4 = random.choice(c) 
d.append(rand4)

# Pick #5
for num5 in c:
    if num5 == rand4:
        c.remove(num5) 
rand5 = random.choice(c) 
d.append(rand5)

# Pick #6
for num6 in c:
    if num6 == rand5:
        c.remove(num6) 
rand6 = random.choice(c) 
d.append(rand6)

print("Your Lotto Numbers are: ", d) # crtl+s