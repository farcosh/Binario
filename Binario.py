l = list();
print("Dame la posicion hasta donde se calcularan los binarios impares: ")
num = input()
x = 0
for i in range(0, int(num)):
    l.append(i)
for a in l:
    n = str(bin(l[a])).count("1")
    if n % 2 != 0:
        x += 1
        print(l[a])
