# Pomodoro Clock
# Tomás Sobral Silva 3/2/26
import time


def menu():
    pass


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


def alarm(delay):
    time.sleep(delay)
    print("Time's up!")


def main():
    work = input("How long do you want to work? ")
    # breaks = input("How long is the break? ")

    unit_work, pomodoro = work_units(work)
    second = seconds(pomodoro, unit_work)
    alarm(second)


main()
