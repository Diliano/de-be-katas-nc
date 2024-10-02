def seconds_to_time_string(total_seconds):
    if total_seconds < 60:
        return get_seconds(total_seconds)

    if total_seconds < 3600:
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        if minutes and seconds:
            return f"{get_minutes(minutes)} and {get_seconds(seconds)}"
        if minutes and not seconds:
            return f"{get_minutes(minutes)}"
        if seconds:
            return f"{get_seconds(seconds)}"

    if total_seconds < 86400:
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        if hours and minutes and seconds:
            return f"{get_hours(hours)}, {get_minutes(minutes)} and {get_seconds(seconds)}"
        if hours and minutes:
            return f"{get_hours(hours)} and {get_minutes(minutes)}"
        if hours and seconds:
            return f"{get_hours(hours)} and {get_seconds(seconds)}"
        if hours:
            return f"{get_hours(hours)}"
        
    if total_seconds < 31536000:
        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        if days and hours and minutes and seconds:
            return f"{get_days(days)}, {get_hours(hours)}, {get_minutes(minutes)} and {get_seconds(seconds)}"
        if days and hours and minutes:
            return f"{get_days(days)}, {get_hours(hours)} and {get_minutes(minutes)}"
        if days and hours:
            return f"{get_days(days)} and {get_hours(hours)}"
        if days and minutes:
            return f"{get_days(days)} and {get_minutes(minutes)}"
        if days and seconds:
            return f"{get_days(days)} and {get_seconds(seconds)}"
        if days:
            return f"{get_days(days)}"
        
    years = total_seconds // 31536000
    remaining = total_seconds % 31536000
    days = remaining // 86400
    hours = (remaining % 86400) // 3600
    minutes = (remaining % 3600) // 60
    seconds = remaining % 60
    if years and days and hours and minutes and seconds:
            return f"{get_years(years)}, {get_days(days)}, {get_hours(hours)}, {get_minutes(minutes)} and {get_seconds(seconds)}"
    if years and days and hours:
            return f"{get_years(years)}, {get_days(days)} and {get_hours(hours)}"  
    if years and hours:
        return f"{get_years(years)} and {get_hours(hours)}"
    if years and days:
        return f"{get_years(years)} and {get_days(days)}"
    if years:
        return f"{get_years(years)}"


def get_seconds(seconds):
    if seconds == 1:
        return f"{seconds} second"
    return f"{seconds} seconds"

def get_minutes(minutes):
    if minutes == 1:
        return f"{minutes} minute"
    return f"{minutes} minutes"

def get_hours(hours):
    if hours == 1:
        return f"{hours} hour"
    return f"{hours} hours"

def get_days(days):
    if days == 1:
        return f"{days} day"
    return f"{days} days"

def get_years(years):
    if years == 1:
        return f"{years} year"
    return f"{years} years"

"""
60 seconds = 1 minute
3600 seconds = 1 hour
86400 seconds = 1 day
31536000 seconds = 1 year
"""