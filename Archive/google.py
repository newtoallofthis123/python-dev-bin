from googlesearch import search
print("                    Google Search in python                  ")
query = str(input("What is the search query: "))
numb = int(input("Enter number of searching: "))
print("Searching for links related to " + query + " on google")
for sear in search(query, tld="co.in", num=numb, stop=10, pause=2):
    print(sear)
