# Create variables
cars =  100
# No, we do not need a floating point here
space_in_a_car = 4.0
# Luckily, passengers is a multiple of drivers so there is an even number in each car, so it matters not
drivers = 30
# Including the space around math operators and assignment statements is good form 
passengers = 90
# Are capital letters required in comments? Do grammar rules apply?
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
