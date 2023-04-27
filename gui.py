import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_bux = sg.InputText(tooltip="Enter todo", key="todo") # Sets the dict key name to to-do
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_bux, add_button]],
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
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()