import json
from random import randint

from utilities.notification_utilities.user_reaction_notification import display_side_notification


def get_welcome_message():
    welcome_messages = json.load(open("../resources/messages.json", "r"))["welcome_messages"]
    current_message = welcome_messages[randint(0, len(welcome_messages) - 1)]

    return current_message["title"], current_message["message"]


def show_focus_selection():
    print("Show selection pop-up")


def set_focus_areas(focus_area_list):
    print(focus_area_list)


def welcome_the_user():
    title, message = get_welcome_message()
    display_side_notification(title, message, user_reaction_handlers=(
        [show_focus_selection, ()], [set_focus_areas, ([1, 2, 3],)]))


if __name__ == '__main__':
    welcome_the_user()
