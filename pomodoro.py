# Tomás Sobral Silva
# Pomodoro Clock 3/2/26

import time


def minutes_seconds(times):
    if len(times) > 2:
        minutes = int(times[2])
        seconds = int(times[4])
    else:
        minutes = 0
        seconds = 0
    return minutes, seconds


def unit(unit1, unit2):
    pass


def notification():
    pass


def pomodoro(pomodoro):  # this function gives me the hour and the unit of the pomodoro
    pomodoro_parts = pomodoro.split()
    time_pomodoro, pomodoro_unit = int(pomodoro_parts[0]), pomodoro_parts[1]
    return time_pomodoro, pomodoro_unit, pomodoro_parts


def pomodoro_breaks(
    interval,
):  # this function gives me the interval duration and the unit
    interval_parts = interval.split()
    time_interval, interval_unit = int(interval_parts[0]), interval_parts[1]
    return time_interval, interval_unit, interval_parts


def main():
    work = input("How long do u want the pomodoro to be? ")
    breaks = input("How long do u want the interval to be? ")

    time_work, work_unit, work_parts = pomodoro(
        work
    )  # this gives me the hour, the unit, and all of the parts of the input
    time_breaks, breaks_unit, interval_parts = pomodoro_breaks(
        breaks
    )  # this gives me the interval duration, the unit and the parts of it all
    minutes_work, seconds_work = minutes_seconds(
        work_parts
    )  # this gives me the minutes and the seconds of the pomodoro
    minutes_breaks, seconds_breaks = minutes_seconds(
        interval_parts
    )  # this gives me the minutes and the seconds of the interval

    # parts = time.asctime()
    # hora = parts.split()[3]
    # hora = int(hora.split(":")[0])
    # print(hora + pomodoro)


main()
