word = input('Enter a word: ')
letters = 'e'
count = ''
counter = 0
for numbers in word:
	if (numbers == letters):
		count = numbers
		counter += len(count)
print(counter)
print(len('helloniggass'))
