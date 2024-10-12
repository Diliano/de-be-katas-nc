def seconds_to_time_string(seconds):
    if type(seconds) != int:
        raise TypeError("Input must be an integer")
    if seconds < 0:
        raise ValueError("Input must be 0 or greater")

    years = seconds // 31536000  
    seconds = seconds % 31536000

    days = seconds // 86400
    seconds = seconds % 86400

    hours = seconds // 3600
    seconds = seconds % 3600

    minutes = seconds // 60
    seconds = seconds % 60

    results = []

    if years > 0:
        if years == 1:
            results.append(f"{years} year")
        else:
            results.append(f"{years} years")

    if days > 0:
        if days == 1:
            results.append(f"{days} day")
        else:
            results.append(f"{days} days")

    if hours > 0:
        if hours == 1:
            results.append(f"{hours} hour")
        else:
            results.append(f"{hours} hours")

    if minutes > 0:
        if minutes == 1:
            results.append(f"{minutes} minute")
        else:
            results.append(f"{minutes} minutes")

    if seconds > 0:
        if seconds == 1:
            results.append(f"{seconds} second")
        else:
            results.append(f"{seconds} seconds")

    if not results:
        return "0 seconds"
    elif len(results) == 1:
        return results[0]
    elif len(results) == 2:
        return f"{results[0]} and {results[1]}"
    else:
        return (", ").join(results[:-1]) + " and " + results[-1]