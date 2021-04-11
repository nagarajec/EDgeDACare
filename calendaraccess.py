import csv
import datetime


def get_current_time():
    time_now = datetime.datetime.now().strftime("%H:%M")
    current_time = datetime.datetime.strptime(time_now, '%H:%M')
    current_time = current_time + datetime.timedelta(minutes=5)
    return current_time


def get_calendar_entries():
    try:
        with open('resources/meetings.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            current_time = get_current_time()

            for row in reader:
                start_time = datetime.datetime.strptime(row[0], '%H:%M')
                end_time = datetime.datetime.strptime(row[1], '%H:%M')
                if start_time <= current_time <= end_time:
                    return False

        return True

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    events = get_calendar_entries()
    print(events)
