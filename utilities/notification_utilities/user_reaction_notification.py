import textwrap
import time

import PySimpleGUI as sg

from utilities.common_utility import get_image_from_file

'''
    Retrieved and modified from PySimpleGUI user ncotrb
'''

# -------------------------------------------------------------------
# fade in/out info and default window alpha
WINDOW_ALPHA = 0.9  # Opacity of the window

# colors
WIN_COLOR = "#282828"
TEXT_COLOR = "#ffffff"

HANDLERS = ()

DEFAULT_DISPLAY_DURATION_IN_MILLISECONDS = 600000


# -------------------------------------------------------------------


def handle_user_reaction(window, actions, reaction_displacement=0):
    while True:
        event, values = window.read(timeout=DEFAULT_DISPLAY_DURATION_IN_MILLISECONDS)
        print(event, values)

        if event == "-GRAPH-":
            if values["-GRAPH-"][0] in range(276, 300) and \
                    values["-GRAPH-"][1] in range(55 + (15 * int(reaction_displacement)),
                                                  80 + (15 * int(reaction_displacement))):
                # Get the positive reaction handler function info
                reaction_function, reaction_function_inputs = actions[0]
                reaction_function(*reaction_function_inputs)
                break
            if values["-GRAPH-"][0] in range(319, 343) and \
                    values["-GRAPH-"][1] in range(55 + (15 * int(reaction_displacement)),
                                                  80 + (15 * int(reaction_displacement))):
                reaction_function, reaction_function_inputs = actions[1]
                reaction_function(*reaction_function_inputs)
                break
        if event == "__TIMEOUT__":
            print(f"There were no actions selected within {DEFAULT_DISPLAY_DURATION_IN_MILLISECONDS/1000}s")
            break


def validate_user_reaction_handlers(user_reaction_handlers):
    # User Reaction Validation
    try:
        if 0 < len(user_reaction_handlers) < 2 or len(user_reaction_handlers) > 3 \
                or any((not type(handler) == list) or (not type(handler[0]) == type(display_side_notification))
                       or(not type(handler[1]) == tuple) for handler in user_reaction_handlers):
            raise RuntimeError("There is a problem with the User Reaction Handlers. "
                               "Please see the expected type in the doc string.")
    except Exception as _:
        raise RuntimeError("There is a problem with the User Reaction Handlers. "
                           "Please see the expected type in the doc string.")


def display_side_notification(notification_title, notification_message, user_reaction_handlers=HANDLERS,
                              use_fade_in=True, display_duration_in_ms=DEFAULT_DISPLAY_DURATION_IN_MILLISECONDS):
    """
            Places an image onto your canvas.  It's a really important method for this element as it enables so much

            :param notification_title: TODO: Add method descriptions
            :type notification_title: (str)
            :param notification_message: if image is in Base64 format or raw? format then use instead of filename
            :type notification_message: str | bytes
            :param user_reaction_handlers: the (x,y) location to place image's top left corner
            :type user_reaction_handlers: Tuple[int, int] | Tuple[float, float]
            :param use_fade_in: the (x,y) location to place image's top left corner
            :type use_fade_in: Tuple[int, int] | Tuple[float, float]
            :param display_duration_in_ms: the (x,y) location to place image's top left corner
            :type display_duration_in_ms: Tuple[int, int] | Tuple[float, float]
            :return: id returned from tkinter that you'll need if you want to manipulate the image
            :rtype: int | None
    """
    validate_user_reaction_handlers(user_reaction_handlers)

    # Compute location and size of the window
    notification_message_list = notification_message.split("\n")  # Split the message based on line breaks
    lines_in_message = 0
    for line_index in range(len(notification_message_list)):
        # Text wrap each line in the message
        notification_message_list[line_index] = textwrap.fill(notification_message_list[line_index], 55)
        lines_in_message += notification_message_list[line_index].count("\n") + 1.5
    # print(lines_in_message)

    screen_res_x, screen_res_y = sg.Window.get_screen_size()
    win_margin = 60  # distance from screen edges
    win_width = 374
    # Set the pop-up's width and height relative to the message
    if user_reaction_handlers:
        win_height = 85 + (15 * lines_in_message)
    else:
        win_height = 50 + (15 * lines_in_message)

    layout = [[sg.Graph(canvas_size=(win_width, win_height), graph_bottom_left=(0, win_height),
                        graph_top_right=(win_width, 0), key="-GRAPH-", background_color=WIN_COLOR, enable_events=True)]]

    window = sg.Window(notification_title, layout, background_color=WIN_COLOR, no_titlebar=True,
                       location=(screen_res_x - win_width - win_margin, screen_res_y - win_height - win_margin),
                       keep_on_top=True, alpha_channel=0, margins=(0, 0), element_padding=(0, 0),
                       finalize=True)

    # Add the message's icon, title and body on a rectangular background
    window["-GRAPH-"].draw_rectangle((win_width, win_height), (-win_width, -win_height), fill_color=WIN_COLOR,
                                     line_color=WIN_COLOR)
    window["-GRAPH-"].draw_image(data=get_image_from_file("DA Care 40 PX.png"),
                                 location=(10, 14))
    window["-GRAPH-"].draw_text(notification_title, location=(64, 15), color=TEXT_COLOR, font=("Arial", 12, "bold"),
                                text_location=sg.TEXT_LOCATION_TOP_LEFT)
    current_line_height = 39  # Start the message lines from Y-AXIS 39
    for message_line in notification_message_list:
        window["-GRAPH-"].draw_text(message_line, location=(64, current_line_height), color=TEXT_COLOR,
                                    font=("Arial", 9), text_location=sg.TEXT_LOCATION_TOP_LEFT)
        current_line_height += (15 * (message_line.count("\n") + 1.5))
        # print(current_line_height)

    if user_reaction_handlers:
        # Add the positive and negative reaction buttons to the rectangular background
        window["-GRAPH-"] \
            .draw_image(data=get_image_from_file("Yes 26 px.png"), location=(274, 47 + (15 * lines_in_message)))
        window["-GRAPH-"] \
            .draw_image(data=get_image_from_file("No 26 px.png"), location=(317, 47 + (15 * lines_in_message)))

    window["-GRAPH-"].Widget.config(cursor="hand2")  # Set cursor to be a hand in the notification

    if use_fade_in:
        for i in range(1, int(WINDOW_ALPHA * 100)):  # fade in
            window.set_alpha(i / 10)
            window.refresh()
            time.sleep(.0001)

        handle_user_reaction(window, user_reaction_handlers, lines_in_message)

        for i in range(int(WINDOW_ALPHA * 100), 1, -1):  # fade out
            window.set_alpha(i)
            window.refresh()
    else:
        window.set_alpha(WINDOW_ALPHA)
        handle_user_reaction(window, user_reaction_handlers, lines_in_message)

    window.close()  # Close the window after the reactions have been handled


if __name__ == '__main__':
    # title = "Hi There!"
    # message = "How are you doing today?\nI'll be here to help you stay healthy throughout the day.\n" \
    #           "Any areas you would like to focus on today?"
    # display_side_notification(title, message, True)
    pass