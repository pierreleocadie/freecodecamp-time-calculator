def add_time(start, duration, starting_day = None):
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    n_days_display = ""
    
    data_processing = lambda data, isDuration: (data.split()[0].split(":"), data.split()[1]) if not isDuration else data.split(":")
    
    start_time = data_processing(start, False)
    duration_time = data_processing(duration, True)
    
    compute_hours = int(start_time[0][0])+int(duration_time[0])
    compute_minutes = int(start_time[0][1])+int(duration_time[1])
    day_period = start_time[1]
    
    n_days = 0
    if int(duration_time[0]) > 12:
        n_days += int(duration_time[0])//24
    if compute_hours > 12 and day_period == "PM":
        n_days += 1

    starting_day_index = days.index(starting_day.lower().capitalize()) if starting_day  else None
    if starting_day:
        if starting_day_index+n_days > len(days):
            ending_day_index = (starting_day_index+n_days)%len(days) 
        else:
            ending_day_index = starting_day_index+n_days
            
    
    if compute_minutes > 59:
        compute_hours+=1
        compute_minutes%=60
    
    if day_period == "AM" and round(compute_hours//10)%2 == 1:
        day_period = "PM"
    elif day_period == "PM" and round(compute_hours//10)%2 == 1:
        day_period = "AM"
    
    if compute_hours >= 12:
        compute_hours%=12
        if compute_hours == 0:
            compute_hours = 12
    
    if n_days > 1:
        n_days_display = f" ({n_days} days later)"
    elif n_days == 1:
        n_days_display = " (next day)"
    
    return f"{compute_hours}:{'0'+str(compute_minutes) if len(str(compute_minutes)) < 2 else compute_minutes} {day_period}{', '+days[ending_day_index] if starting_day else ''}"+n_days_display

print(add_time("3:00 PM", "23:30"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))

assert add_time("3:00 PM", "3:10") == "6:10 PM", "ERROR 1"
assert add_time("11:30 AM", "2:32", "Monday") == "2:02 PM, Monday", "ERROR 2"
assert add_time("11:43 AM", "00:20") == "12:03 PM", "ERROR 3"
assert add_time("10:10 PM", "3:30") == "1:40 AM (next day)", "ERROR 4"
assert add_time("11:43 PM", "24:20", "tueSday") == "12:03 AM, Thursday (2 days later)", "ERROR 5"
assert add_time("6:30 PM", "205:12") == "7:42 AM (9 days later)", "ERROR 6"