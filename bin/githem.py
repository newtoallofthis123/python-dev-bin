import os
import subprocess
import sys

working_dir = os.path.dirname(os.path.realpath(__file__))
def isgitthere():
	check = f'{working_dir}\.git'
	isitthere = os.path.exists(check)
	if isgitthere:
		return "do detect git here"
	else:
		return "sorry, no git detected, do you want me to initiate it?"

print(f'Hello, You are current working on your project in the {working_dir} directory and I {isgitthere()} \n')

def gitdoit():
	def isSysThere():
		try:
			x = sys.argv[1]
			return x
		except:
			return "Nah"
	if isgitthere() == "do detect git here" and isSysThere() == "Nah":
		print("I got no other command, so here,\n")
		x = subprocess.run(['git' ,'status'], capture_output=True)
		y = str(x.stdout)
		os.system("git status")

gitdoit()


