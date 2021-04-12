import time

import pyglet as pyglet
import webview

from da_care_configuration import DACareConfig
from utilities.common_utility import get_video_url_and_duration_based_on_area


def play_video(da_care_config):
    video_url, video_duration = get_video_url_and_duration_based_on_area(da_care_config)
    print(f"Starting the video: '{video_url}'. The video will run for '{video_duration}' seconds . . .")

    window = webview.create_window('DA Care', video_url, resizable=False, easy_drag=True, frameless=True, on_top=True)

    webview.start()  # Start the video

    print("Closing the video pop-up . . .")

    window.hidden = True
    window.destroy()


def load_gif_img(gif_path):
    # pick an animated gif file you have in the working directory
    # ag_file = gif_path
    animation = pyglet.image.load_animation(gif_path)
    anim_sprite = pyglet.sprite.Sprite(animation)

    # create a window and set it to the image size
    win = pyglet.window.Window(width=anim_sprite.width, height=anim_sprite.height)

    # set window background color = r, g, b, alpha
    # each value goes from 0.0 to 1.0
    green = 0, 1, 0, 1
    pyglet.gl.glClearColor(*green)

    @win.event
    def on_draw():
        win.clear()
        anim_sprite.draw()

    pyglet.app.run()


if __name__ == '__main__':
    C = DACareConfig()
    C.set_area_list(["Lower Body"])
    play_video(C)
