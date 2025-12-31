# Given a list of dictionaries, sort the list based on a specific key in the dictionaries
people = [
    {"name": "Ajay Jain", "age": 25},
    {"name": "Babita Soni", "age": 20},
    {"name": "Palak Tiwari", "age": 30}
]

sorted_people = sorted(people, key=lambda x: x["age"])
print(sorted_people)
