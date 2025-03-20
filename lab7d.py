#!/usr/bin/env python3
# Student ID: 133245233

def sec_to_time(seconds):
    """Convert a given number of seconds to a Time object."""
    hour = seconds // 3600
    remaining = seconds % 3600
    minute = remaining // 60
    second = remaining % 60
    return Time(hour, minute, second)

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def time_to_sec(self):
        return (self.hour * 3600) + (self.minute * 60) + self.second

    def sum_times(self, other):
        total_seconds = self.time_to_sec() + other.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour = new_time.hour
        self.minute = new_time.minute
        self.second = new_time.second

    def valid_time(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

    def __str__(self):
        return self.format_time()