from collections import Counter
f = open('chisla.txt')
a = f.readlines()
a = list(map(int, a))

chisla = [i % 117 for i in a] #массив чисел %117

chislaCount = Counter(chisla) #все возможные остатки

total = 0
# учитываем числа, которые сами делятся на 117 без остатка
total += (chislaCount[0]*(chislaCount[0]-1)/2)

print('число пар кратных 117:', total)