from src.seconds_to_time_string import seconds_to_time_string

def test_handles_input_that_evaluates_only_to_seconds():
    assert seconds_to_time_string(1) == "1 second"
    assert seconds_to_time_string(2) == "2 seconds"

def test_handles_input_that_evaluates_only_to_minutes():
    assert seconds_to_time_string(60) == "1 minute"
    assert seconds_to_time_string(120) == "2 minutes"
    assert seconds_to_time_string(180) == "3 minutes"
    assert seconds_to_time_string(360) == "6 minutes"

def test_handles_input_that_evaluates_to_minutes_and_seconds():
    assert seconds_to_time_string(121) == "2 minutes and 1 second"
    assert seconds_to_time_string(122) == "2 minutes and 2 seconds"
    assert seconds_to_time_string(305) == "5 minutes and 5 seconds"

def test_handles_input_that_evaluates_only_to_hours():
    assert seconds_to_time_string(3600) == "1 hour"
    assert seconds_to_time_string(7200) == "2 hours"

def test_handles_input_that_evaluates_to_hours_and_seconds():
    assert seconds_to_time_string(3601) == "1 hour and 1 second"
    assert seconds_to_time_string(3602) == "1 hour and 2 seconds"
    assert seconds_to_time_string(7202) == "2 hours and 2 seconds"

def test_handles_input_that_evaluates_to_hours_and_minutes():
    assert seconds_to_time_string(3660) == "1 hour and 1 minute"
    assert seconds_to_time_string(3720) == "1 hour and 2 minutes"
    assert seconds_to_time_string(7260) == "2 hours and 1 minute"

def test_handles_input_that_evaluates_to_hours_minutes_and_seconds():
    assert seconds_to_time_string(3661) == "1 hour, 1 minute and 1 second"
    assert seconds_to_time_string(3662) == "1 hour, 1 minute and 2 seconds"
    assert seconds_to_time_string(3721) == "1 hour, 2 minutes and 1 second"
    assert seconds_to_time_string(7321) == "2 hours, 2 minutes and 1 second"

def test_handles_input_that_evaluates_only_to_days():
    assert seconds_to_time_string(86400) == "1 day"
    assert seconds_to_time_string(172800) == "2 days"

def test_handles_input_that_evaluates_to_days_and_seconds():
    assert seconds_to_time_string(86401) == "1 day and 1 second"
    assert seconds_to_time_string(86402) == "1 day and 2 seconds"
    assert seconds_to_time_string(172802) == "2 days and 2 seconds"

def test_handles_input_that_evaluates_to_days_and_minutes():
    assert seconds_to_time_string(86460) == "1 day and 1 minute"
    assert seconds_to_time_string(86520) == "1 day and 2 minutes"
    assert seconds_to_time_string(172860) == "2 days and 1 minute"

def test_handles_input_that_evaluates_to_days_and_hours():
    assert seconds_to_time_string(90000) == "1 day and 1 hour"
    assert seconds_to_time_string(93600) == "1 day and 2 hours"
    assert seconds_to_time_string(176400) == "2 days and 1 hour"

def test_handles_input_that_evaluates_to_days_hours_and_minutes():
    assert seconds_to_time_string(90060) == "1 day, 1 hour and 1 minute"
    assert seconds_to_time_string(93720) == "1 day, 2 hours and 2 minutes"
    assert seconds_to_time_string(176520) == "2 days, 1 hour and 2 minutes"

def test_handles_input_that_evaluates_to_days_hours_minutes_and_seconds():
    assert seconds_to_time_string(90061) == "1 day, 1 hour, 1 minute and 1 second"
    assert seconds_to_time_string(93722) == "1 day, 2 hours, 2 minutes and 2 seconds"
    assert seconds_to_time_string(176522) == "2 days, 1 hour, 2 minutes and 2 seconds"

def test_handles_input_that_evaluates_only_to_years():
    assert seconds_to_time_string(31536000) == "1 year"
    assert seconds_to_time_string(63072000) == "2 years"
    
def test_handles_input_that_evaluates_to_years_and_days():
    assert seconds_to_time_string(31622400) == "1 year and 1 day"
    assert seconds_to_time_string(31708800) == "1 year and 2 days"
    assert seconds_to_time_string(63158400) == "2 years and 1 day"

def test_handles_input_that_evaluates_to_years_days_and_hours():
    assert seconds_to_time_string(31626000) == "1 year, 1 day and 1 hour"
    assert seconds_to_time_string(31716000) == "1 year, 2 days and 2 hours"
    assert seconds_to_time_string(63162000) == "2 years, 1 day and 1 hour"

def test_handles_input_that_evaluates_to_years_days_hours_minutes_and_seconds():
    assert seconds_to_time_string(31626061) == "1 year, 1 day, 1 hour, 1 minute and 1 second"
    assert seconds_to_time_string(63252122) == "2 years, 2 days, 2 hours, 2 minutes and 2 seconds"