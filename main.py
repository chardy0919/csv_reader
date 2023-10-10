import csv
user_input = input("Ya wanna dog or cat?")
if user_input.lower() == "cat":
    with open('./data/cats.csv') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            print(f"{row['name']} is a{row[' age']} year old{row[' breed']}")
elif user_input.lower() == "dog":
    with open('./data/dogs.csv') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            print(f"{row['name']} is a{row[' age']} year old{row[' breed']}")
else:
    print(f"We ain't got no {user_input}s")

