# Pomodoro Clock
# Tomás Sobral Silva 3/2/26
import os
import time


def length(string):  # this function returns the minutes if the input as any
    parts = string.split()
    if len(parts) > 2:
        minutes = int(parts[2])
        return minutes
    else:
        minutes = 0
        return minutes


def work_units(hours):  # returns the unit and the time inputed
    parts = hours.split()
    work_time = int(parts[0])
    unit = parts[1]
    return unit, work_time


def seconds(hours, unit):  # transforms the various units of time all in seconds
    if unit == "hr" or unit == "hour":
        return hours * 3600
    elif unit == "min" or unit == "minute":
        return hours * 60
    elif unit == "sec" or unit == "second":
        return hours
    else:
        raise ValueError("Invalid unit")


def alarm_work(
    delay,
):  # It delays the alarm during the work time and when finished it will notify the user
    time.sleep(delay)
    title = "Work is Over!"
    message = "You have completed the time. Well Done!"
    command = f'notify-send "{title}" "{message}"'
    os.system(command)
    return True


def alarm_break(
    delay,
):  # It delays the alarm during the work time and when finished it will notify the user
    time.sleep(delay)
    title = "Break Over!"
    message = "You have done your Break time! Time to work!"
    command = f'notify-send "{title}" "{message}"'
    os.system(command)
    return True


def main():
    work = input("How long do you want to work? ")
    breaks = input("How long is the break? ")

    while True:
        # from here
        unit_work, pomodoro = work_units(work)
        minute_to_second = length(work) * 60

        total_seconds = seconds(pomodoro, unit_work) + minute_to_second
        alarm_work(total_seconds)
        # to here the code counts the work time
        if alarm_work:
            unit_break, break_time = work_units(breaks)
            minute_to_second = length(breaks) * 60

            total_seconds = seconds(break_time, unit_break) + minute_to_second
            alarm_break(total_seconds)


main()
