import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_bux = sg.InputText(tooltip="Enter todo", key="todo") # Sets the dict key name to to-do
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10]) # Takes in a string so we pass the todos here
edit_button = sg.Button("Edit")


window = sg.Window('My To-Do App',
                   layout=[[label], [input_bux, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))


'''
for example, 

x, y = (3, 4) 

(3, 4) is a tuple. x is assigned 3 and y is assigned 4

so instead of (Add, {todo: Hi})
its just Add
then {todo:Hi}

'''

while True:
    event, values = window.read()  # splitting up the values of the tuple. event grabs the label
    # of the event
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit) # grabs the index of the selected to-do to be edited
            todos[index] = new_todo # replaces
            functions.write_todos(todos) # updates the list
            window['todos'].update(values=todos) # updayes the list window with new to-dos
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()