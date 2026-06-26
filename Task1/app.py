def load_data():
    try:
        with open("database.txt", "r") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        return set()


def save_data(data):
    with open("database.txt", "w") as file:
        for item in data:
            file.write(item + "\n")


database = load_data()

new_data = input("Enter Data : ")

if new_data in database:
    print("Duplicate Data Found")
else:
    database.add(new_data)
    save_data(database)
    print("Unique Data Added Successfully")
