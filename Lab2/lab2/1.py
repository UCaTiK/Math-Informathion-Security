import math
import random
import numpy as np

base = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
        'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я']

# phrase = input("Введите фразу, которую хотите зашифровать: ")
phrase = "нельзя недооценивать противника"
lst = []
for symbol in phrase:
	if symbol in base:
		lst.append(symbol)
		
# code = input("Введите кодовое слово: ")
code = "пароль"
lst2 = []
for symbol in code:
	if symbol in base:
		lst2.append(symbol)

n = len(lst2)
m = math.ceil(len(lst) / n)
print(n, m)

while len(lst) != m*n:
	lst.append(random.choice(base))

a = np.array(lst)
a.resize((m, n))
print(a)

b = []
for character in base:
	if character in code:
		b.append(character)

result = ""
for s in b:
	for i in range(m):
		result += a[i][code.index(s)]
		
print(result)
	
