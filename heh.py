f = open('chisla.txt')
a = f.readlines()
a = list(map(int, a))
chisla = []
count = 0
for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) % 117 == 0:
        count += 1
        chisla.append(a[i])
        chisla.append(a[i + 1])
print('число пар кратных 117:', count)
print('самые большие такие пары:',max(chisla) - 1, 'и', max(chisla))
