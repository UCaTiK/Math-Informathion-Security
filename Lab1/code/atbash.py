base = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
        'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']

cypher = base.copy()
cypher.reverse()

print(base)
print(cypher)

while True:
	string = input("Введите строку, которую хотите зашифровать: ").lower()
	if string == "q":
		break
	
	result = ""
	for character in string:
		result += cypher[base.index(character)]
	
	print(result)