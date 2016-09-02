def calculate_electric(electric):
	electic_split = float(electric) / 4
	return electic_split

def cable_bill(total, movie, hbo=17.0, cable_box=23.50, adapter=6.50,):
	base = (float(total) - hbo - cable_box - adapter - movie) / 4
	hbo_split = hbo / 2
	cable_box_split = cable_box / 2
	adapter_split = adapter / 2

	return base, hbo_split, cable_box_split, adapter_split, movie

def check_yo_self(total, electric, cable, movie):
	total_utilities = 0.0
	for money in total:
		total_utilities += total[money]

	print total_utilities
	print float(cable)
	print float(movie)
	print (float(electric) - 1550.00)
	if float(total_utilities) == float(cable) + (float(electric) - 1550.00) + float(movie):
		print "SUCCESS!"
	else:
		print "You fucked up!"

	
b = "Ben"
m = "Matt"
s = "Sam"
r = "Ricky"

totals = {b: 0, m: 0, s: 0, r: 0}

total_rent = raw_input('Enter total amount of rent + electric: ')

electric_bill = calculate_electric(float(total_rent) - 1550.00)

total_cable = raw_input('Enter total cable bill: ')
movie_amt_choice = (raw_input("Enter total movie amount (if none, enter 'no': ")).lower()

if movie_amt_choice == 'no' or movie_amt_choice == 'n':
	movie_amt = 0.0
else:
	try:
		movie_amt = float(movie_amt_choice)
	except:
		print "That's not an integer! Using 0 instead..."
		movie_amt = 0.0

if movie_amt != 0:
	movie_split = raw_input("Enter the number of people splitting the movie(s): ")
	print float(movie_amt) / float(movie_split)

base, hbo_split, cable_box_split, adapter_split, movie = cable_bill(total=total_cable, movie=movie_amt)

print cable_bill(total=total_cable, movie=movie_amt)

for roommate in totals:
	totals[roommate] += electric_bill
	totals[roommate] += base
	
totals[b] += cable_box_split
totals[r] += adapter_split
totals[s] += (hbo_split + adapter_split)
totals[m] += (hbo_split + cable_box_split)

print totals

check_yo_self(totals, total_rent, total_cable, movie_amt)