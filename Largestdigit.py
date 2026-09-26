number = int(input("Enter a number: "))
largest_digit = 0

if number == 0:
	largest_digit = 0

while number > 0:
	digit = number % 10
	
	if digit > largest_digit:
		largest_digit = digit
		
	number //= 10
	
print(f"The largest digits is:  {largest_digit}")
