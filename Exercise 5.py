# Initialize a list of dinner guests
dinner_guests = ['Lateef', 'Sana', 'Johnny']

# Print an invitation to each guest in the list
for guest in dinner_guests:
    print("Dear " + guest + ", I would like to invite you to dinner.")

# Print a blank line
print()

# Inform the guests that Johnny will not be attending
print("Unfortunately, Johnny is unable to make it to the dinner.")

# Replace Marie Curie with Isaac Newton in the list of guests
dinner_guests[1] = 'Eren'

# Print an updated invitation to each guest in the list
for guest in dinner_guests:
    print("Dear " + guest + ", I would like to invite you to dinner.")