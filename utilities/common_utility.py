import base64
import json
import random
from pathlib import Path

from utilities.time_utility import get_youtube_time_difference

ROOT = Path(__file__).parent.parent


def get_image_from_file(image_file_name):
    return base64.b64encode(open(f"{Path(f'{ROOT}/media/pictures')}/{image_file_name}", "rb").read())


def open_resource(resource_name, io_action):
    return open(f"{Path(f'{ROOT}/resources')}/{resource_name}", f"{io_action}")


def get_message_type(message_type):
    return json.load(open_resource("messages.json", "r"))[message_type]


def get_video_url_and_duration_based_on_area(da_care_config):
    area = random.choice(da_care_config.get_area_list())

    print(f"The current area is: '{area}'")

    if area in ("Eyes", "Neck", "Shoulder"):
        area = "Upper Body"
        # TODO: Right now, we are making this to point to upper body, change it to eyes as needed

    video_map = json.load(open_resource("video_position_map.json", "r"))["videos"]
    video_url = video_map["url"]

    video_area = random.choice(da_care_config.get_option_map()[area]["videos"])
    video_config = video_map[video_area]
    start, end = video_config["start"], video_config["stop"]

    print(f"Video area: '{video_area}'; Video config: {video_config}; Video start/stop time: '{start}'/'{end}'")

    video_start_time_in_seconds = get_youtube_time_difference(start)
    video_duration = get_youtube_time_difference(end, start)

    return video_url.format(int(video_start_time_in_seconds)), video_duration


def get_gif_path(area):
    if area == "Eyes":
        filename = Path(f'{ROOT}/media/chair-squat.gif')
    elif area == "Lower Body":
        filename = Path(f'{ROOT}/media/calf-raise.gif')
    elif area == "Upper Body":
        filename = Path(f'{ROOT}/media/rear_pulse.gif')
    elif area == "waist":
        filename = Path(f'{ROOT}/media/calf-raise.gif')
    else:
        filename = Path(f'{ROOT}/media/chair-squat.gif')
    return filename
