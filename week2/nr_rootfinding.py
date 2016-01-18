def find(y):
	epsilon = 0.01
	guess = y / 2.0

	while abs(guess * guess - y) >= epsilon:
		guess = guess - (((guess**2) - y) / (2 * guess))

	return guess

if __name__ == '__main__':
	print("Square root of %.3f is about %.3f" 
		  % (25, find(25)))
