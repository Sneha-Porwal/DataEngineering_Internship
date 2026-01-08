def sort_people_by_age(people):
    return sorted(people, key=lambda x: x["age"])


if __name__ == "__main__":
    people = [
        {"name": "Ajay Jain", "age": 25},
        {"name": "Babita Soni", "age": 20},
        {"name": "Palak Tiwari", "age": 30}
    ]

    sorted_people = sort_people_by_age(people)
    print(sorted_people)
