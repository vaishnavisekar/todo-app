import function
import time
now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is",now)

while True:
    user_action = input("Enter show ,add ,complete, edit or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        items = function.get_todo()
        items.append(todo + '\n')
        function.write_todo(items)

    elif user_action.startswith('show'):
            items = function.get_todo()
            new_items = [i.strip("\n") for i in items]

            for index, item in enumerate(new_items):
             # print("{}.{}".format(index,item))
                print(f"{index}-{item}")

    elif user_action.startswith('edit'):
        try:

            number = int(user_action[5:])
            edit_index = number - 1
            items = function.get_todo()
            new_todo = input("enter the todo : ")
            items[edit_index] = new_todo + ' \n'
            function.write_todo(items)
        except ValueError:
            print("invalid command")
            continue
    elif user_action.startswith('complete'):
        try:
            num = int(user_action[9:])
            items = function.get_todo()
            index = num - 1
            todo_to_remove = items[index].strip("\n")
            items.pop(index)
            function.write_todo(items)
            message = f"Todo {todo_to_remove} is removed from list"
            print(message)
        except IndexError:
            print("there is no item in number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("command is invalid")
print("bye!!!!!!!")
