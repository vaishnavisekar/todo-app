def get_todo(filepath='todos.txt'):
    with open(filepath, 'r') as file:
        items = file.readlines()
    return items


def write_todo(items, filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(items)


