name = "Chris T"
age = 37 # truth
height = 71 # inches
weight = 175 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Largely Missing'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on coffee intake." % teeth

# this line is tricky, but I'll try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight,
	age + height + weight)
	