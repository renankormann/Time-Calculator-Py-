'''
Created on Jul 12, 2023

@author: renan
'''

def add_time(begin, addtime, day=""):
    
    # Break the beginning time in hours, minutes and AM-PM.
    start = begin.split(":")
    minu_apm = start[1].split(" ")
    
    start.pop(1)
    start.append(minu_apm[0])
    start.append(minu_apm[1])

    init_h = int(start[0])
    init_m = int(start[1])
    am_pm = start[2]

    # Let's do the same with the time adding.
    add = addtime.split(":")

    add_h = int(add[0])
    add_m = int(add[1])

    # Let's convert the hours to 24h style.
    if am_pm.lower() == "pm":
        init_h += 12

    # Now, we start by adding the minutes.
    final_h = 0
    final_m = init_m + add_m
    while final_m > 59:
        final_m -= 60
        final_h += 1
    
    # Let's edit the minutes already.
    if final_m == 0:
        final_m = "00"
    elif final_m > 0 and final_m < 10:
        hold = str(final_m)
        final_m = "0" + hold
    else:
        final_m = str(final_m)

    # Now, we add the hours.
    add_days = 0
    final_h += init_h
    final_h += add_h
    while final_h > 23:
        final_h -= 24
        add_days += 1
    
    # We have to find out if the final time is in the morning or night. To do that, since we are in a 24h style
    # we can just check if the final_h is greater than 12, if it is, it is "PM". At the same time we can convert
    # Back to 12h style.
    final_ampm = ""
    if final_h < 12:
        if final_h == 0:
            final_ampm = "AM"
            final_h = 12
        else:
            final_ampm = "AM"
    elif final_h == 12:
        final_ampm = "PM"
    else:
        final_ampm = "PM"
        final_h -= 12

    final_h = str(final_h)

    # OPTIONAL ARGUMENT:
    # Defining a list with the weekdays:
    week_days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    # Now, we have to check which of the week_days is the starting one:
    day_pos = 0
    for i in range(len(week_days)):
        if day.lower() == week_days[i].lower():
            day_pos = i
            
    # This loop is counting which will be the position of the final day.
    if add_days > 0:
        for i in range(add_days):
            if day_pos == 6:
                day_pos = 0
            else:
                day_pos += 1

    final_day = week_days[day_pos]

    # Now we got to the end. Just concatenate strings to get the desired result.
    new_time = ""
    if day == "":
        if add_days == 0:
            new_time = final_h + ":" + final_m + " " + final_ampm
        elif add_days == 1:
            new_time = final_h + ":" + final_m + " " + final_ampm + " (next day)"
        elif add_days > 1:
            new_time = final_h + ":" + final_m + " " + final_ampm + " (" + str(add_days) + " days later)"
    else:
        if add_days == 0:
            new_time = final_h + ":" + final_m + " " + final_ampm + ", " + final_day
        elif add_days == 1:
            new_time = final_h + ":" + final_m + " " + final_ampm + ", " + final_day + " (next day)"
        elif add_days > 1:
            new_time = final_h + ":" + final_m + " " + final_ampm + ", " + final_day + " (" + str(add_days) + " days later)"
                
    return(new_time)