word = input("Enter a word: ")
letter = ''
for number in word:
		if number.islower():
			word = number.upper()
			print(word)
