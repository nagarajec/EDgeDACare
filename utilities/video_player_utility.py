import pafy
import webview


def play_video(url, area):
    # video = pafy.new(url)
    # best = video.getbest()
    video_url = "https://www.youtube.com/embed/{url}?autoplay=1&modestbranding=1&start={}".format(url)
    if area == "Neck":
        video_url = video_url.format("77")
    elif area == "Shoulder":
        video_url = video_url.format("77")
    elif area == "Lower Body":
        video_url = video_url.format("77")
    elif area == "Upper Body":
        video_url = video_url.format("77")
    else:
        video_url = video_url.format("77")
    webview.create_window('Video Player', video_url)
    webview.start()
