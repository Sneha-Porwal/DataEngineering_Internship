data = [
    {"name": "Ajay Jain", "age": 25},
    {"name": "Babita Soni", "age": 20},
    {"name": "Palak Tiwari", "age": 30}
]

# Function to return age
def get_age(person):
    return person["age"]

# Sort the list using the function
data.sort(key=get_age)

# Print each dictionary on a new line
for person in data:
    print(person)

