while True:
    user_action = input("Type add, show, edit or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
           todos = file.readlines()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            # item = item.strip('\n') works too
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        number = int(user_action[5:])
        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        #print('Here is todos existing', todos)

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo +'\n'

        #print('Here is how it will be', todos)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)


    elif user_action.startswith("complete")
        number = int(user_action[9:])


        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        index = number -1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was remove from teh list."
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("Command not recognized")
print("Bye!")


