# NoobScience

import os
import sys

list_ = ('dir', 'cd', 'clear', 'cls')

print("Hello World, type you command\n")
while True:
	command = str.lower(input("@ "))
	if command in list_:
		x = os.system(command)
		print(x)