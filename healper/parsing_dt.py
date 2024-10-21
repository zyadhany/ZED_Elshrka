from datetime import datetime

def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def Time_left(target_time):    
    current_time = datetime.now()
    time_difference = target_time - current_time
    seconds_left = int(time_difference.total_seconds())
    return seconds_left