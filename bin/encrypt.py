# This is an example of my custom awesome encryption concept.
# You can use this, but as this is public, I recommend you build your own

print("Encrypt Me")

def encrpyt(word):
	x = list()
	for letter in word:
		x.append(letter)
	for item in x:
		if item == 'E' or 'b':
			item = 'a'
	print(x)

encrpyt("Encrypt")

# Incomplete, wait for it to be complete