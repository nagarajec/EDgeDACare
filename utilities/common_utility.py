import base64
from pathlib import Path


def get_image_from_file(image_file_name):
    return base64.b64encode(open(f"{Path('../media/pictures')}/{image_file_name}", "rb").read())
