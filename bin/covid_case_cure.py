import math

x = 400000
y = 100000
i = 0
month = int(input("What is number of months/days: "))
while i < month:
    x = x - y
    x += 400000
    i += 1  
    if x == 1392642289:
        print("Covid beat us!")
    else:
        pass

x = x - 300000
print(x)
