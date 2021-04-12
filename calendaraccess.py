import csv
import datetime


def get_current_time():
    time_now = datetime.datetime.now().strftime("%H:%M")
    current_time = datetime.datetime.strptime(time_now, '%H:%M')
    current_time = current_time + datetime.timedelta(minutes=5)
    return current_time


def does_user_have_meeting_within_5_minutes():
    try:
        with open('resources/meetings.csv', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            current_time = get_current_time()

            for row in reader:
                start_time = datetime.datetime.strptime(row[0], '%H:%M')
                end_time = datetime.datetime.strptime(row[1], '%H:%M')

                # If the current time is within the start time and end time, then the user is in a meeting
                if start_time <= current_time <= end_time:
                    print("The User is in a meeting now!")
                    return True

        print("The User is in not a meeting now!")
        return False

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    events = does_user_have_meeting_within_5_minutes()
    print(events)
