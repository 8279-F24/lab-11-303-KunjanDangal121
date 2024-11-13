# A contact list is a place where you can store a specific contact with
# other associated information such as a phone number, email address,
# birthday, etc. Write a program that first takes in word pairs that
# consist of a name and a phone number (both strings), separated by a
# comma. That list is followed by a name, and your program should output
# the phone number associated with that name. Assume the search name is 
# always in the list.

# Get the input string of contact pairs
contacts_input = input()

# Get the search name
search_name = input()

# Split the contacts string into individual contact pairs
contact_pairs = contacts_input.split()

# Create a dictionary to store name-phone pairs
contacts = {}

# Process each contact pair and add to dictionary
for pair in contact_pairs:
    name, phone = pair.split(',')
    contacts[name] = phone

# Output the phone number for the search name
print(contacts[search_name])