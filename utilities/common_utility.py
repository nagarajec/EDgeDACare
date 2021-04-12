import base64
import json
import sys
from pathlib import Path

ROOT = sys.path[1]


def get_image_from_file(image_file_name):
    return base64.b64encode(open(f"{Path(f'{ROOT}/media/pictures')}/{image_file_name}", "rb").read())


def open_resource(resource_name, io_action):
    return open(f"{Path(f'{ROOT}/resources')}/{resource_name}", f"{io_action}")


def get_message_type(message_type):
    return json.load(open_resource("messages.json", "r"))[message_type]
