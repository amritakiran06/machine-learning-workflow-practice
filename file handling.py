
def save_to_file(filename, items):
    with open(filename, 'w') as file:
        file.writelines([item + '\n' for item in items])

def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

data_file = "data.txt"
my_list = ["Apple", "Banana", "Cherry"]

save_to_file(data_file, my_list)
loaded_list = load_from_file(data_file)

print(loaded_list)