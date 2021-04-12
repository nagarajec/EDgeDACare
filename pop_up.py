import PySimpleGUI as sg

# colors
WIN_COLOR = "#282828"
TEXT_COLOR = "#ffffff"

sg.change_look_and_feel('SystemDefaultForReal')  # Add a little color for fun

# layout = [[sg.Text('Please, select the focus area(s)', font='Helvetica 12', key="-GRAPH-")]]  # a title line t
# layout += [[sg.Text(f'{i}. '), sg.CBox(''), sg.Input()] for i in range(1, 6)]  # the checkboxes and descriptions
# layout += [[sg.Button('Save'), sg.Button('Load'), sg.Button('Exit')]]  # the buttons

layout = [[sg.Text('Please, select the focus area(s)', auto_size_text=True, key="-GRAPH-", background_color=WIN_COLOR, text_color=TEXT_COLOR)]]  # a title line t
layout += [[sg.CBox('sdfgsdfgs', auto_size_text=True, background_color=WIN_COLOR, text_color=TEXT_COLOR)] for i in range(1, 6)]  # the checkboxes and descriptions
layout += [[sg.Button('Save'), sg.Button('Load'), sg.Button('Exit')]]  # the buttons

window = sg.Window('To Do List Example', layout, keep_on_top=True, background_color=WIN_COLOR, grab_anywhere=True, no_titlebar=True)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event == 'Save':
        window.save_to_disk('mywindow.out')
    elif event == 'Load':
        window.load_from_disk('mywindow.out')
window.close()
