def calculate_electric(electric):
	electic_split = float(electric) / 4
	return electic_split

def cable_bill(total, movie, hbo=17.0, cable_box=23.50, adapter=6.50,):
	base = (float(total) - hbo - cable_box - adapter - movie) / 4
	hbo_split = hbo / 2
	cable_box_split = cable_box / 2
	adapter_split = adapter / 2

	return base, hbo_split, cable_box_split, adapter_split, movie

b = "Ben"
m = "Matt"
s = "Sam"
r = "Ricky"

totals = {b: 0, m: 0, s: 0, r: 0}

electric = raw_input('Enter electric bill for this month: ')
electric_bill = calculate_electric(electric)

total_cable = raw_input('Enter total cable bill: ')
movie_amt_choice = raw_input("Enter total movie amount (if none, enter 'no': ")

try:
	movie_amt = int(movie_amt_choice)
except:
	print "That's not an integer! Using 0 instead..."
	movie_amt = 0

print movie_amt_choice

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