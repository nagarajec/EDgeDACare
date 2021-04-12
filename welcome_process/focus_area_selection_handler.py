import PySimpleGUI as sg

# colors
from utilities.common_utility import get_image_from_file

WIN_COLOR = "#282828"
TEXT_COLOR = "#ffffff"


def set_user_focus_area(da_care_config, focus_area_list):
    da_care_config.set_area_list(focus_area_list)
    print(f"The User selected the following areas: {da_care_config.get_area_list()}")


def display_focus_area_selector(da_care_config):
    print("The user indicated that (s)he has a focus area today. Prompting the User to select a focus area . . .")

    # Add a title for the screen
    frame_layout = [[sg.Image(data=get_image_from_file("DA Care Window Logo Small.png"), background_color=WIN_COLOR),
                     sg.Text('Please, tell me where it hurts', pad=((0, 10), (0, 0)), auto_size_text=True,
                             background_color=WIN_COLOR, text_color=TEXT_COLOR)]]

    # Add the checkboxes and descriptions
    frame_layout += [[sg.CBox(option, key=f"{option}", auto_size_text=True, background_color=WIN_COLOR,
                              text_color=TEXT_COLOR)] for option in da_care_config.get_option_map().keys()]

    # Add the buttons for the selection pop-up
    frame_layout += [
        [sg.Column(layout=([[sg.Button(image_data=get_image_from_file("Final Yes.png"), pad=((0, 15), (0, 0)),
                                       key="-Submit-"),
                             sg.Button(image_data=get_image_from_file("Final No.png"), key="-Exit-")]]),
                   background_color=WIN_COLOR, key="-Buttons-",
                   justification="right", vertical_alignment="center")]]

    window_layout = [
        [sg.Frame('', layout=frame_layout, border_width=0, background_color=WIN_COLOR, pad=((0, 0), (5, 5)))]]

    window = sg.Window('', window_layout, keep_on_top=True, background_color=WIN_COLOR, grab_anywhere=True,
                       no_titlebar=True, auto_size_text=True, finalize=True, resizable=False, alpha_channel=0.97)

    # Set cursor format for the buttons and the checkboxes
    window["-Buttons-"].Widget.config(cursor="hand2")
    for option in da_care_config.get_option_map():
        window[f"{option}"].Widget.config(cursor="hand2")

    while True:
        event, values = window.read()
        # print(event, values)

        if event in (None, '-Exit-'):
            break
        elif event == '-Submit-':
            focus_area_list = [option for option in values if values[option]]
            set_user_focus_area(da_care_config, focus_area_list)
            break

    window.close()
