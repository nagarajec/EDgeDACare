import time

from utilities.common_utility import get_message_type
from utilities.notification_utilities.user_reaction_notification import display_side_notification
from welcome_process.focus_area_selection_handler import display_focus_area_selector, set_user_focus_area


def start_scheduled_process(da_care_config):
    # Wait for the number of seconds left in the "seconds_counter" - 600000 ms (10 minutes)
    time.sleep(da_care_config.get_second_counter(millisecond=True) - 600000)

    # Capture the timestamp and send the warning notification to the user
    reminder = get_message_type("reminder")[0]
    title, message = reminder["title"], reminder["message"]

    display_side_notification(title, message, display_duration_in_ms=600000, user_reaction_handlers=(
        [display_focus_area_selector, (da_care_config,)],
        [set_user_focus_area, (da_care_config, da_care_config.get_option_list().keys(),)],
        [set_user_focus_area, (da_care_config, da_care_config.get_option_list().keys(),)]))

    # If the user says yes or the notification times out
    pass
