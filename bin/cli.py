# CLI SEARCH 
# By NoobScience
# Github: https://github.com/newtoallofthis123/python-dev-bin
# Website: https://newtoallofthis123.github.io/About
# Description: Search using the commandline
# Modules used: System , Webbrowser

# Import the necessary modules: sys, webbrowser
import sys
import webbrowser

# Defining function to search
try:
	def search(sear):
		if sear == "-ddg":
			url = "https://duckduckgo.com/?q=" + str(sys.argv[2])
			webbrowser.open(url)
		if sear == "-g":
			url = "https://www.google.com/search?hl=en&q=" + str(sys.argv[2])
			webbrowser.open(url)
		if sear == '-yt':
			url = "https://www.youtube.com/results?search_query=" + str(sys.argv[2])
			webbrowser.open(url)
		if sear == '-q':
			url = "https://www.qwant.com/?q=" + str(sys.argv[2])
			webbrowser.open(url)
		if sear == '--help':
			print("_______________  ___                 ______________________")
			print("|  ____________| | |                 |_____________________|")
			print("| |              | |                           | |")
			print("| |              | |                           | |")
			print("| |              | |                           | |")
			print("| |              | |                           | |")
			print("| |              | |                           | |")
			print("| |              | |                           | |")
			print("| ____________   | _____________       ___________________")
			print("______________|  |______________|     |____________________|")
			print("\n\n\n \t\t\tSEARCH")

			print("-ddg for duckduckgo")
			print("-g for google")
			print("-q for qwant")
			print("-yt for youtube")
			print("--help for help\n")
			print("Example Usage: cli -g \"Hello World\" ")

	if sys.argv[1] == '-ddg':
		print("Searching with duckduckgo")
		search("-ddg")
	elif sys.argv[1] == '-g':
		print("Searching with google")
		search("-g") 
	elif sys.argv[1] == '-yt':
		print("Searching with youtube")
		search("-yt") 
	elif sys.argv[1] == '-q':
		print("Searching with Qwant")
		search("-q") 
	elif sys.argv[1] == '--help':
		search('--help')
except:
	print("Error, Try again or use cli.py --help / cli.exe --help")