from datetime import datetime


def get_youtube_time_difference(start_time, end_time):
    return (datetime.strptime(end_time, "%M:%S") - datetime.strptime(start_time, "%M:%S")).total_seconds()
