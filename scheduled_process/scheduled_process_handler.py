import time
import random
from utilities.common_utility import get_message_type,get_gif_path
from utilities.notification_utilities.user_reaction_notification import display_side_notification
from utilities.video_gif_utility import play_video, load_gif_img
from welcome_process.focus_area_selection_handler import display_focus_area_selector, set_user_focus_area


def start_scheduled_process(da_care_config):
    # Wait for the number of seconds left in the "seconds_counter" - 600000 ms (10 minutes)
    time.sleep(da_care_config.get_second_counter(millisecond=True) - 600000)

    # Capture the timestamp and send the warning notification to the user
    reminder = get_message_type("reminder")[0]
    title, message = reminder["title"], reminder["message"]

    display_side_notification(title, message, display_duration_in_ms=600000, user_reaction_handlers=(
        [play_video, (da_care_config,)],
        [snooze_handler, (da_care_config,)],
        [set_user_focus_area, (da_care_config, da_care_config.get_option_map().keys(),)]))

    # If the user says yes or the notification times out
    pass


def snooze_handler(da_care_config):
    if (da_care_config.get_snooze_count() == 0):
        da_care_config.set_snooze_count(da_care_config.get_snooze_count() + 1)
        reminder = get_message_type("snooze_messages")[0]
        title, message = reminder["title"], reminder["message"]
        display_side_notification(title, message, display_duration_in_ms=5000, user_reaction_handlers=(
        [display_focus_area_selector, (da_care_config,)],
        [snooze_handler, (da_care_config,)],
        [set_user_focus_area, (da_care_config, da_care_config.get_option_map().keys(),)]))
        da_care_config.set_second_counter(60*10)
        start_scheduled_process(da_care_config)

    elif (da_care_config.get_snooze_count() == 1):
        da_care_config.set_snooze_count(da_care_config.get_snooze_count() + 1)
        reminder = get_message_type("snooze_messages")[1]
        title, message = reminder["title"], reminder["message"]
        display_side_notification(title, message, display_duration_in_ms=2000, user_reaction_handlers=(
        [display_focus_area_selector, (da_care_config,)],
        [snooze_handler, (da_care_config,)],
        [set_user_focus_area, (da_care_config, da_care_config.get_option_map().keys(),)]))
        set_user_focus_area(da_care_config, da_care_config.get_option_map().keys())
        selected_area_list = da_care_config.get_area_list()
        print("Selected Area List:"+ str(selected_area_list))
        print(type(selected_area_list))
        entry_list = list(selected_area_list)
        Area = random.choice(entry_list)
        filename = get_gif_path(Area)
        load_gif_img(filename)