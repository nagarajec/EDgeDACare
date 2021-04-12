import PySimpleGUI as sg

# colors
from utilities.config_setter import Config

WIN_COLOR = "#282828"
TEXT_COLOR = "#ffffff"

CONFIG = Config()

# Add a title
layout = [[
    sg.Text('Please, tell me where it hurts', auto_size_text=True, background_color=WIN_COLOR, text_color=TEXT_COLOR)]]

layout += [[sg.CBox(option, auto_size_text=True, background_color=WIN_COLOR, text_color=TEXT_COLOR)]
           for option in CONFIG.get_option_list()]  # the checkboxes and descriptions
layout += [[sg.Button('Save'), sg.Button('Load', pad=((10, 10), (10, 10)))]]  # the buttons

window = sg.Window('To Do List Example', layout, keep_on_top=True, background_color=WIN_COLOR, grab_anywhere=True,
                   no_titlebar=True)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    elif event == 'Save':
        window.save_to_disk('mywindow.out')
    elif event == 'Load':
        window.load_from_disk('mywindow.out')
window.close()
