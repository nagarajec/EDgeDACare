import time
from tkinter import *

import pafy
import pyglet as pyglet
import webview

from utilities.common_utility import get_video_based_on_area


def play_video(da_care_config):
    selected_area_list = da_care_config.get_area_list()
    video_url = get_video_based_on_area(selected_area_list)
    webview.create_window('DA Care', video_url)
    webview.start()


def load_gif_img(gif_path):
    # pick an animated gif file you have in the working directory
    # ag_file = gif_path
    animation = pyglet.image.load_animation(gif_path)
    animSprite = pyglet.sprite.Sprite(animation)

    # create a window and set it to the image size
    win = pyglet.window.Window(width=animSprite.width, height=animSprite.height)

    # set window background color = r, g, b, alpha
    # each value goes from 0.0 to 1.0
    green = 0, 1, 0, 1
    pyglet.gl.glClearColor(*green)

    @win.event
    def on_draw():
        win.clear()
        animSprite.draw()

    pyglet.app.run()


if __name__ == '__main__':
    load_gif_img()
