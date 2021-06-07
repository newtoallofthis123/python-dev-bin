# v = u+at

choice = str.lower(input("What do you want to calculate? (v, u, a, t)"))
if choice == 'v':
    u = float(input("What is the value of u(m/s): "))
    a = float(input("What is the value of a(ms^-2): ")) 
    t = float(input("What is the value of t(sec): "))
    print(u + a *t)
elif choice == 'u':
    v = float(input("What is the value of v(m/s): "))
    a = float(input("What is the value of a(ms^-2): ")) 
    t = float(input("What is the value of t(sec): "))
    print(v - a *t)
elif choice == 'a':
    u = float(input("What is the value of u(m/s): "))
    v = float(input("What is the value of v(m/s): ")) 
    t = float(input("What is the value of t(sec): "))
    print((v-u)/t)
elif choice == 't':
    u = float(input("What is the value of u(m/s): "))
    a = float(input("What is the value of a(ms^-2): ")) 
    v = float(input("What is the value of v(m/s): "))
    print((v-u)/a)
else:
    print("Error Something went wrong!")
