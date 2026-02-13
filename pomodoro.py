# Pomodoro Clock
# Tomás Sobral Silva 3/2/26
import os
import time


def menu():
    print("Welcome to the Pomodoro Clock!")
    print("Set Pomodoro time --- 1")
    print("Exit --- 2")

def the_brains(data, alarm_function):
    unit, time_passed = work_units(data)
    minute_to_second = length(data) * 60
    total_seconds = seconds(time_passed, unit) + minute_to_second
    alarm_function(total_seconds)  
    return total_seconds


def hour(time_seconds):
    if time_seconds >= 3600:
        hour = time_seconds // 3600
        minutes = time_seconds % 3600 // 60
        seconds = time_seconds % 3600 % 60
    else:
        hour = 0
        minutes = time_seconds // 60
        seconds = time_seconds % 60
        
    return hour, minutes, seconds



# def save(hour, minute):
#     with open("Pomodoro_data.txta") as file:
#         file.write("Date: {}; Pomodoro time{}; Total breaks{};".format())


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


def choices(choice):
    if choice == "1":
        work = input("How long do you want to work? ")
        breaks = input("How long is the break? ")
        return work, breaks

    elif choice == "2":
        print("Terminating...")
        exit(0)
    else:
        print("Invalid choice")
        exit(1)


def main():
    menu()
    choice = input("The choice: ")
    work, breaks = choices(choice)
    total_work = 0
    total_break = 0
    while choice != "2":
        work_time= the_brains(work, alarm_work)
        total_work += work_time
        
        break_time = the_brains(breaks, alarm_break)
        total_break += break_time
        choice = input("To continue press enter; \nTo exit press 2: ")
    
    
    work_hour, work_minutes, work_seconds = hour(total_work)
    break_hour, break_minutes, break_seconds = hour(total_break) 
    
    
    
    print("------------")
    print("Total work time: {} hours, {} minutes, and {} seconds".format(work_hour, work_minutes, work_seconds))
    print("Total break time: {} hours, {} minutes, and {} seconds".format(break_hour, break_minutes, break_seconds))
    print("------------")
    print("Closing...")
    #teste

main()