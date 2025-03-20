#!/usr/bin/env python3
# Student ID: 133245233

def sec_to_time(seconds):
    """Convert a given number of seconds to a Time object in 
       hour, minute, second format"""
    hour = seconds // 3600
    remaining = seconds % 3600
    minute = remaining // 60
    second = remaining % 60
    return Time(hour, minute, second)

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, __str__, __repr__
                            time_to_sec, format_time,
                            change_time, sum_times
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        """return a string representation for the object self"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
    
    def __repr__(self):
        """return a string representation for the object self"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'
    
    def format_time(self):
        """Return time object (t) as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
 
    def sum_times(self, other):
        """Add two time objects and return the sum."""
        total_seconds = self.time_to_sec() + other.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Modify time object by adding/subtracting seconds"""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour = new_time.hour
        self.minute = new_time.minute
        self.second = new_time.second
        return None

    def time_to_sec(self):
        """convert a time object to a single integer representing the 
        number of seconds from mid-night"""
        return (self.hour * 3600) + (self.minute * 60) + self.second

    def valid_time(self):
        """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
           return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
           return False
        return True