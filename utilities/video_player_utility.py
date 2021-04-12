import pafy
import webview


def play_video(url):
    video = pafy.new(url)
    best = video.getbest()
    webview.create_window('Video Player', best.url)
    webview.start()

