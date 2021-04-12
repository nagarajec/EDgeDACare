from datetime import datetime


def get_youtube_time_difference(end_time, start_time="0:00"):
    return (datetime.strptime(end_time, "%M:%S") - datetime.strptime(start_time, "%M:%S")).total_seconds()
