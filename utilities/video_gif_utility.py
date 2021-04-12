import pafy
import webview
from utilities.common_utility import get_video_based_on_area
import time
from tkinter import *


def play_video(da_care_config):
    # video = pafy.new(url)
    # best = video.getbest()
    #time.sleep(da_care_config.get_second_counter(10))
    selected_area_list = da_care_config.get_area_list()
    video_url = get_video_based_on_area(selected_area_list)
    webview.create_window('Video Player', video_url)
    webview.start()


def load_gif_img(gif_path):
    window = Toplevel()
    window.title('GIF')
    canvas = Canvas(window, width=500, height=500)
    canvas.pack()
    print(gif_path)
    my_image = PhotoImage(file=gif_path)
    print(my_image)
    canvas.create_image(0, 0, anchor=NW, image=my_image)
