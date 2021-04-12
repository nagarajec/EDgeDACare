from tkinter import RAISED

import PySimpleGUI as sg

# colors
from utilities.common_utility import get_image_from_file
from utilities.config_setter import Config

WIN_COLOR = "#282828"
WIN_TITLE_COLOR = "#282232"
TEXT_COLOR = "#ffffff"

CONFIG = Config()

# Add a title
layout = [[sg.Image(data=get_image_from_file("DA Care Window Logo Small.png"), background_color=WIN_COLOR),
           sg.Text('Please, tell me where it hurts', pad=((0, 10), (0, 0)), auto_size_text=True,
                   background_color=WIN_COLOR, text_color=TEXT_COLOR)]]

layout += [[sg.CBox(option, auto_size_text=True, background_color=WIN_COLOR, text_color=TEXT_COLOR)]
           for option in CONFIG.get_option_list()]  # the checkboxes and descriptions

# Add the buttons for the selection pop-up
layout += [[sg.Frame('', layout=([[sg.Button(image_data=get_image_from_file("Final Yes.png"), ),
            sg.Button(image_data=get_image_from_file("Final No.png"))]]), background_color=WIN_COLOR,
                     border_width=0).Widget.config(cursor="hand2")]]

window = sg.Window('', layout, keep_on_top=True, background_color=WIN_COLOR, grab_anywhere=True,
                   no_titlebar=True, auto_size_text=True)

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
