word = input("Enter a word: ")
vowels = "aeiouAEIOU"

count = 0 
for number in word:
	if number in vowels:
		count += 1
print(count)
