base = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
        'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я']

base_copy = base.copy()
matrix = [base_copy]
for i in range(len(base_copy)-1):
	array_copy = base_copy.copy()
	array_copy.append(array_copy.pop(0))
	matrix.append(array_copy)
	base_copy = array_copy.copy()

for i in range(len(matrix)):
	print(matrix[i])


# phrase = input("Введите фразу, которую хотите зашифровать: ")
phrase = "криптография серьезная наука"
lst = []
for symbol in phrase:
	if symbol in base:
		lst.append(symbol)

# code = input("Введите кодовое слово: ")
code = "математика"
lst2 = []
for symbol in code:
	if symbol in base:
		lst2.append(symbol)

while len(lst) != len(lst2):
	if len(lst) < len(lst2):
		lst2 = lst2[0:len(lst)]
	
	elif len(lst) > len(lst2):
		lst2 = lst2 * (len(lst) // len(lst2) + 1)

print("Начальная фраза:", phrase)
print("Кодовое слово:", code)

print(lst)
print(lst2)

result = ""
for i in range(len(lst)):
	result += matrix[base.index(lst[i])][base.index(lst2[i])]
	
print(result)
	