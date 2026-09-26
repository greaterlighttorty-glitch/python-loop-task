word = input("Enter a word: ")
letter = ''
for number in word:
		if number.isupper():
			word = number.lower()
			print(word)
