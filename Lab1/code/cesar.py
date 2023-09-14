base = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
        'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']

k = int(input("Введите число, на которое хотите сдвинуть шифр: "))

k = k % len(base)

pswd = input("Введите кодовое слово: ").lower()
unique_characters = []

for character in pswd:
	if character not in unique_characters:
		unique_characters.append(character)

for character in base:
	if character not in unique_characters:
		unique_characters.append(character)

begin = unique_characters[len(unique_characters)-k:]
end = unique_characters[:len(unique_characters)-k]

cypher = begin + end

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
