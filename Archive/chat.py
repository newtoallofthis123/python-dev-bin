# About
about = "who created you"
about1 = "created by who"
about2 = "where are you living"
about3 = "how can i install you"

# About Ans

# Friends
friends = "who is your favourite character in friends"
friends1 = "do you like chandler"
friends2 = "do you like monica"
friends3 = "do you like ross"
friends4 = "do you like rachel"
friends5 = "do you like phoebe"
friends6 = "do you like joey"
friends7 = "were ross and rachel on a break"
friends8 = "name all characters of friends"
friends9 = "friends wiki"
friends10 = "tell me a chandler joke"
friends11 = "play the friends theme song"
friends12 = "cheated on rachel"

# Friends Ans
friends_ans = "I like Chandler Bing, or should I say Miss Chalander Bong"
friends1_ans = "Yes I like Chandler, could he be more funnier"
friends2_ans = "Monica is so sweet but so intense. 'She is maintained by Chandler'"
friends3_ans = "We were on a break"
friends4_ans = "All my life, people have told me I am a shoe, but what if I don't want to be a shoe, what if I want to be a purse?"
friends5_ans = "Smelly Cat Smelly Cat, What are they feeding you?"
friends6_ans = "How you Do'ng ?"
friends7_ans = "Maybe, ask Ross or Rachel, you get different answer, best not to go down that again"
friends8_ans = "Ross Geller, Rachel Green, Chandler Bing, Joey Tribbiani, Phoebe, Monica Geller, Janice, Carol Willick, Susan Bunch, Ben Geller Willick Bunch, Emma Geller Green"
friends9_ans = "Friends"
friends10_ans = "You have to stop the Q-Tip when there is Resistance"
#friends11_ans = playsound("friends.mp3")
friends12_ans = "We were on a break"

# Big Bang Theory
bbt1 = "who is favourite character in big bang theory"
bbt2 = "do you like sheldon"
bbt3 = "about sheldon"
bbt4 = "about penny"
bbt5 = "about leonard"

# Big Bang Theory Answers
bbt1_ans = "Dr. Sheldon Copper, Bazinga"
bbt2_ans = "Yes I like Sheldon, He is my favourite Character"
bbt3_ans = "Sheldon is a genius from an young age but lacks social skills. He is a theortical physicist. He loves Amy."
bbt4_ans = "Penny is an aspiring actresses and works as an waitress. She is not that smart but has good social skills which is in stark contrast to the guys who are socially akward scientists"
bbt5_ans = "Leonard is a Exoerimental Physicist. He loves Penny and I like him. He has a Mother who is like Sheldon Though. Funny Dynamic. Sheldon's roomate and one of his best friends"

def friends():
        choice3 = str.lower(input("Ask me another friends one?"))
        if choice3 == friends:
            print(friends_ans)
            friends()
        elif choice3 == friends1:
            print(friends1_ans)
            friends()
        elif choice3 == friends2:
            print(friends2_ans)
            friends()
        elif choice3 == friends3:
            print(friends3_ans)
            friends()
        elif choice3 == friends4:
            print(friends4_ans)
            friends()
        elif choice3 == friends5:
            print(friends5_ans)
            friends()
        elif choice3 == friends6:
            print(friends6_ans)
            friends()
        elif choice3 == friends7:
            print(friends7_ans)
            friends()
        elif choice3 == friends8:
            print(friends8_ans)
            friends()
        elif choice3 == friends9:
            print(friends9_ans)
            friends()
        elif choice3 == friends10:
            print(friends10_ans)
            friends()
        elif choice3 == friends11:
            print(friends11_ans)
            friends()
        elif choice3 == friends12:
            print(friends12_ans)
            friends()
        elif choice3 == "exit":
            print("Bye")
            exit()
        elif choice3 == "quit":
            print("Bye")
            exit()
        elif choice3 == "e":
            print("Bye")
            exit()
        elif choice3 == "q":
            print("Bye")
            exit()
        else:
            print("Don't know the answer to that, please just ask me another one.")
            friends()

def bbt():
    choice3 = str.lower(input("Ask me a Big Bang Theory Questiion?"))
    if choice3 == bbt1:
        print(bbt1_ans)
        bbt()
    if choice3 == bbt2:
        print(bbt2_ans)
        bbt()
    if choice3 == bbt3:
        print(bbt3_ans)
        bbt()
    if choice3 == bbt4:
        print(bbt4_ans)
        bbt()
    if choice3 == bbt5:
        print(bbt5_ans)
        bbt()
    elif choice3 == "exit":
        print("Bye")
        exit()
    elif choice3 == "quit":
        print("Bye")
        exit()
    elif choice3 == "e":
        print("Bye")
        exit()
    elif choice3 == "q":
        print("Bye")
        exit()
    else:
        print("Don't know the answer to that, please just ask me another one.")
        bbt()

choice2 = str.lower(input("Hello, I am Noob, do you want to talk with me?"))
if choice2 == 'y':
    choice4 = str.lower(input("Okay, come let's talk, what do you want to talk about?"))
    if choice4 == "friends":
        friends()
    elif choice4 == "bbt":
        bbt()
    elif choice4 == "big bang theory":
        bbt()
else:
        print("Sorrry, In valid request, try again")
        exit()
        
            
