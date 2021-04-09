import tkinter.filedialog
import tkinter as tk
import csv
from PIL import Image, ImageTk
from datetime import datetime
from pytz import timezone
from time import sleep
import webbrowser

location = {}

first = tk.Tk()
first.title("DA-Care")

w = 400     # popup window width
h = 400     # popup window height
sw = first.winfo_screenwidth()
sh = first.winfo_screenheight()
x = (sw - w)/2
y = (sh - h)/2
first.geometry('%dx%d+%d+%d' % (w, h, x, y))

welcome = tk.Label(first, text='Welcome to DA-Care! \n Please let us help you keep energized.', width=120, height=10).pack()

def first_close():
    first.destroy()

def first_open():
    first.filename = tk.filedialog.askopenfilename(initialdir="C:/Users/rb929/", title="Select A File", filetypes=(("all files", "*.*"),))
    location['name'] = first.filename
    filename = tk.Label(first, text=first.filename, width=120).pack()
    confirm = tk.Button(first, text="Confirm", command=first_close, width=10).pack()

upload = tk.Button(first, text="Upload your Calendar.", command=first_open, width=40).pack()

first.mainloop()

second = tk.Tk()

def second_close():
    second.destroy()

second.title("DA-Care")
second.geometry('%dx%d+%d+%d' % (w, h-200, x, y))
thanks = tk.Label(second, text='Thank you!\nPlease resume your normal day activity and we will keep you posted.', width=120, height=10).pack()
ok = tk.Button(second, text="OK", command=second_close, width=10).pack()
second.mainloop()

third = tk.Tk()
third.title("DA-Care")
third.geometry('%dx%d+%d+%d' % (1200, 700, 1, 1))
my_image = ImageTk.PhotoImage(Image.open('test2.jpg'))
my_image_label = tk.Label(third, image=my_image).pack()
third.mainloop()


# data={}

# csv_file = location['name']

# id = 0

# thirty_minutes = 30 * 60
# one_hour = 2 * thirty_minutes
# two_hours = 2 * one_hour

# with open(csv_file, encoding="utf-8", errors="ignore") as csvFile:
#     csvReader = csv.DictReader(csvFile)
#     for rows in csvReader:
#         data[id] = rows
#         id = id + 1

# def get_seconds(x):
#     a = x.split(':')
#     b = a[2].split(' ')
#     s = int(a[0])*60*60 + int(a[1])*60 + int(b[0])
#     if (b[1] == 'PM'):
#         s = s + 12*60*60
#     return s

# fmt = '%Y-%m-%d %H:%M:%S %Z%z'
# eastern = timezone('US/Eastern')
# nw = datetime.now(eastern)
# print(nw.strftime(fmt))
# sleep(6)
# nv = datetime.now(eastern)
# print(nv.minute)
# if(nv.minute == 39):
#   webbrowser.get('windows-default').open('https://cheezburger.com/9416471040/this-cat-doesnt-get-enough-sleep')

import pyglet

# pick an animated gif file you have in the working directory
ag_file = "person.gif"
animation = pyglet.resource.animation(ag_file)
sprite = pyglet.sprite.Sprite(animation)

# create a window and set it to the image size
win = pyglet.window.Window(width=sprite.width, height=sprite.height)

# set window background color = r, g, b, alpha
# each value goes from 0.0 to 1.0
green = 0, 1, 0, 1
pyglet.gl.glClearColor(*green)

@win.event
def on_draw():
    win.clear()
    sprite.draw()

pyglet.app.run()