import json
import requests
from utilities.config_setter import Config
import PySimpleGUI as sg
from random import randint

from utilities.notification_utilities.user_reaction_notification import display_side_notification

# Create a session object to hold all the configs
ses = requests.Session()

global config_setter


def get_welcome_message():
    welcome_messages = json.load(open("../resources/messages.json", "r"))["welcome_messages"]
    if not config_setter.get_is_started():
        current_message = welcome_messages[randint(0, 0)]
        config_setter.set_is_started(True)
        return current_message["title"], current_message["message"]


def show_focus_selection():
    print("Show selection pop-up")
    event, values = sg.Window('Choose an option', [
        [sg.Text('Select one->'), sg.Listbox(config_setter.get_option_list(), size=(50, 5), key='LB')],
        [sg.Button('Ok'), sg.Button('Cancel')]]).read(close=True)

    if event == 'Ok':
        sg.popup(f'You chose {values["LB"][0]}')
    else:
        sg.popup_cancel('User aborted')


def set_focus_areas(focus_area_list):
    print(focus_area_list)


def welcome_the_user():
    title, message = get_welcome_message()
    display_side_notification(title, message, user_reaction_handlers=(
        [show_focus_selection, ()], [set_focus_areas, ([1, 2, 3],)]))


if __name__ == '__main__':
    config_setter: Config = Config()
    welcome_the_user()
