import time

import pyglet as pyglet
import webview

from da_care_configuration import DACareConfig
from utilities.common_utility import get_video_url_and_duration_based_on_area
#from scheduled_process.scheduled_process_handler import start_scheduled_process




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
