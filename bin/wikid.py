import webbrowser
import wikipedia
from tkinter import *
import tkinter.messagebox
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion

try:
    print("Hello, I will search wikipedia for you using the wikipedia module. What do you want to do? ")
    print("A - WikiSummary B - Full WikiPage C - Search Wiki with Keyword D - Suggest with KeyWord ")
    print("E - Show links F - Show Short given number of lines summary G - Show reference links ")
    print("H - Categories I - All Links in a Wikipedia Page")
    keyword = str.lower(input("Enter your choice "))
    search = str(input("What is the search term? "))
    if keyword == "a":
        WikiTitle = wikipedia.page(search).title
        print(WikiTitle)
        WikiSummary = wikipedia.summary(search)
        print(WikiSummary)
        print("By NoobScience 2021")
    elif keyword == "b":
        WikiTitle = wikipedia.page(search).title
        print(WikiTitle)
        WikiPage = wikipedia.page(search).content
        print(WikiPage)
        print("By NoobScience 2021")
    elif keyword == "c":
        number_of_results = int(input("Number of search Results "))
        WikiKey = wikipedia.search(search, results=number_of_results)
        print(WikiKey)
        print("By NoobScience 2021")
    elif keyword == "d":
        WikiSuggest = wikipedia.suggest(search)
        print(WikiSuggest)
        print("By NoobScience 2021")
    elif keyword == "e":
        WikiTitle = wikipedia.page(search).title
        print(WikiTitle)
        WikiUrl = wikipedia.page(search).url
        print(WikiUrl)
        print("By NoobScience 2021")
    elif keyword == "f":
        WikiTitle = wikipedia.page(search).title
        print(WikiTitle)
        number_of_sentences = int(input("Number of Lines "))
        WikiShort = wikipedia.summary(search, sentences=number_of_sentences)
    elif keyword == "g":
        WikiTitle = wikipedia.page(search).title
        print(WikiTitle)
        WikiReference == wikipedia.page(search).references
        print(WikiReference)
        print("By NoobScience 2021")
    elif keyword == "h":
        WikiTitle = wikipedia.page(search).title
        print(WikiTitle)
        WikiCategories = wikipedia.page(search).categories
        print("By NoobScience 2021")
    elif keyword == "i":
        WikiTitle = wikipedia.page(search).title
        print(WikiTitle)
        WikiLinks = wikipedia.page(search).links
        print(WikiLinks)
        print("By NoobScience 2021")
    elif keyword == "j":
        WikiTitle = wikipedia.page(search).title
        print(WikiTitle)
        img = int(input("Which Image Number? (1,2,3...)"))
        WikiImages == wikipedia.page(search).images[img]
    elif keyword == "k":
        WikiHtmml == wikipedia.page(search).html
    else:
        print("Invalid Keyword, try again")
        print("By NoobScience 2021")
        quit()



except wikipedia.exceptions.DisambiguationError as e:
    print (e.options)
    print("By NoobScience 2021")


