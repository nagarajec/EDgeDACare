from random import randint

from utilities.common_utility import get_message_type
from utilities.notification_utilities.user_reaction_notification import display_side_notification
from welcome_process.focus_area_selection_handler import display_focus_area_selector, set_user_focus_area


def get_welcome_message(da_care_config):
    welcome_messages = get_message_type("welcome_messages")

    # Get a random welcome message
    # all welcome messages prompt the user to indicate if (s)he'd like a focus area or not
    if not da_care_config.get_is_started():
        current_message = welcome_messages[0]
        da_care_config.set_is_started(True)
        return current_message["title"], current_message["message"]


def welcome_the_user(da_care_config):
    title, message = get_welcome_message(da_care_config)

    # Display the notification prompt for User focus areas
    display_side_notification(title, message, display_duration_in_ms=600000, user_reaction_handlers=(
        [display_focus_area_selector, (da_care_config,)],
        [set_user_focus_area, (da_care_config, da_care_config.get_option_map().keys(),)],
        [set_user_focus_area, (da_care_config, da_care_config.get_option_map().keys(),)]))
