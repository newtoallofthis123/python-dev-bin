# By the way, the ideal gas equation is PV = nRT
R_cal = 1.987
R_j = 8.314
R_atm = 0.0821

choice = str.lower(input("What do you want to calculate(P, V, n, R, T)"))
if choice == 'p':
	n = int(input("What is the number of moles"))
	v = float(input("What is the volume of the gas"))
	t = float(input("Input temperature in kelvin"))
	choice_R = str.lower(input("What is the value of R in? (calorie, Joule, Atmosphere)")
	if choice_R == 'cal':
		p = n * R_cal * t * 1/v
		print(p)
