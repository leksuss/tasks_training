# https://www.codewars.com/kata/52742f58faf5485cae000b9a


def format_duration(seconds):
    if not seconds:
        return 'now'
    time_segments = {
        31536000: 'year',
        86400: 'day',
        3600: 'hour',
        60: 'minute',
        1: 'second',
    }
    friendly_duration = []
    for time_segment in time_segments.keys():
        div, mod = divmod(seconds, time_segment)
        if div:
            segment_name = time_segments[time_segment] + int(div > 1) * 's'
            friendly_duration.append(f'{div} {segment_name}')
        seconds = mod
    *lst, last = friendly_duration
    return f"{', '.join(lst)} and {last}" if lst else last


assert format_duration(1), "1 second"
assert format_duration(62), "1 minute and 2 seconds"
assert format_duration(120), "2 minutes"
assert format_duration(3600), "1 hour"
assert format_duration(3662), "1 hour, 1 minute and 2 seconds"
