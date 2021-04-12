import base64
import json
import sys
from pathlib import Path
import random
from utilities.time_utility import get_youtube_time_difference

ROOT = sys.path[1]


def get_image_from_file(image_file_name):
    return base64.b64encode(open(f"{Path(f'{ROOT}/media/pictures')}/{image_file_name}", "rb").read())


def open_resource(resource_name, io_action):
    return open(f"{Path(f'{ROOT}/resources')}/{resource_name}", f"{io_action}")


def get_message_type(message_type):
    return json.load(open_resource("messages.json", "r"))[message_type]


def get_video_based_on_area(list_of_areas):
    video_url = "https://www.youtube.com/embed/xELgfiXSw-s?autoplay=1&modestbranding=1&start={}"
    Video_map = json.load(open_resource("video_position_map.json", "r"))
    Area = random.choice(list_of_areas)
    print(Area)
    if Area == "Eyes":
        start = Video_map["movlee_video"]["upper_back"]["start"]
        end = Video_map["movlee_video"]["upper_back"]["stop"]
    elif Area == "Lower Body":
        start = Video_map["movlee_video"]["lower_back"]["start"]
        end = Video_map["movlee_video"]["lower_back"]["stop"]
    elif Area == "Upper Body":
        start = Video_map["movlee_video"]["upper_back"]["start"]
        end = Video_map["movlee_video"]["upper_back"]["stop"]
    elif Area == "waist":
        start = Video_map["movlee_video"]["waist"]["start"]
        end = Video_map["movlee_video"]["waist"]["stop"]
    else:
        start = Video_map["movlee_video"]["arm"]["start"]
        end = Video_map["movlee_video"]["arm"]["stop"]
        print(start)
        print(end)
    start_time = get_youtube_time_difference(start, end)
    return video_url.format(int(start_time))

def get_gif_path(Area):
    if Area == "Eyes":
        filename = Path(f'{ROOT}/media/chair-squat.gif')
    elif Area == "Lower Body":
        filename = Path(f'{ROOT}/media/calf-raise.gif')
    elif Area == "Upper Body":
        filename = Path(f'{ROOT}/media/rear_pulse.gif')
    elif Area == "waist":
        filename = Path(f'{ROOT}/media/calf-raise.gif')
    else:
        filename = Path(f'{ROOT}/media/chair-squat.gif')
    return filename
