import PySimpleGUI as sg

# colors
from utilities.common_utility import get_image_from_file
from utilities.config_setter import Config

WIN_COLOR = "#282828"
TEXT_COLOR = "#ffffff"

CONFIG = Config()

# Add a title for the screen
frame_layout = [[sg.Image(data=get_image_from_file("DA Care Window Logo Small.png"), background_color=WIN_COLOR),
                 sg.Text('Please, tell me where it hurts', pad=((0, 10), (0, 0)), auto_size_text=True,
                         background_color=WIN_COLOR, text_color=TEXT_COLOR)]]

# Add the checkboxes and descriptions
frame_layout += [[sg.CBox(option, key=f"-Option-#{option}-", auto_size_text=True, background_color=WIN_COLOR,
                          text_color=TEXT_COLOR)] for option in CONFIG.get_option_list()]

# Add the buttons for the selection pop-up
frame_layout += [[sg.Column(layout=([[sg.Button(image_data=get_image_from_file("Final Yes.png"), pad=((0, 15), (0, 0)),
                                                key="-Submit-"),
                                      sg.Button(image_data=get_image_from_file("Final No.png"), key="-Exit-")]]),
                            background_color=WIN_COLOR, key="-Buttons-",
                            justification="right", vertical_alignment="center")]]

window_layout = [[sg.Frame('', layout=frame_layout, border_width=0, background_color=WIN_COLOR, pad=((0, 0), (5, 5)))]]

window = sg.Window('', window_layout, keep_on_top=True, background_color=WIN_COLOR, grab_anywhere=True,
                   no_titlebar=True, auto_size_text=True, finalize=True, resizable=False)

# Set cursor format for the buttons and the checkboxes
window["-Buttons-"].Widget.config(cursor="hand2")
for option in CONFIG.get_option_list():
    window[f"-Option-#{option}-"].Widget.config(cursor="hand2")

while True:
    event, values = window.read()

    print(event, values)

    if event in (None, '-Exit-'):
        break
    elif event == 'Save':
        window.save_to_disk('mywindow.out')
    elif event == 'Load':
        window.load_from_disk('mywindow.out')
window.close()
