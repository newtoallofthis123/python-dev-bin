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
	if isgitthere() == "do detect git here" and isSysThere() == "-a" :
		timePeriod = int(input("By The way, can you tell me the time period in seconds: "))
		commitMessage = str(input("The Commit message, it is 'Update to All Files' by deflaut"))
		def commithem():
			os.system("git add .")
			if commitMessage == "":
				commitMessage_ = "Update to All Files"
			else:
				commitMessage_ = commitMessage
			x = f'git commit -m "{commitMessage_}"'
			os.system(x)
			y = "Hello"
			y.after(1000, commithem)
		commithem()

gitdoit()


