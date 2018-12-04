from datetime import datetime, timedelta
import re


class Guard():

    def __init__(self, id):
        self.id = int(id)
        self.shifts = {}

    def get_last_minute(self, day):
        return max(self.shifts[day])

    def mark_minutes(self, day, start, end, mark):
        for m in range(start, end):
            #print(m, mark)
            self.shifts[day][m] = mark        

    def start_shift(self, day, minute):
        self.shifts[day] = {}
        self.mark_minutes(day, 0, minute + 1, ".")

    def falls_asleep(self, day, minute):
        last_minute = self.get_last_minute(day)
        self.mark_minutes(day, last_minute + 1, minute, ".")

    def wakes_up(self, day, minute):
        last_minute = self.get_last_minute(day)
        self.mark_minutes(day, last_minute + 1, minute, "#")

    def get_minutes_asleep(self):
        asleep = 0
        for minutes in self.shifts.values():
            asleep += len([mark for mark in minutes.values() if mark == "#"])
        return asleep

    def get_max_minute(self):
        counter = {}
        for minutes in self.shifts.values():
            for m in [m for (m, mark) in minutes.items() if mark == "#"]:
                counter[m] = counter.get(m, 0) + 1

        # Don't forget the edge case ...
        if not counter:
            return None, None

        max_minute = max(counter, key=counter.get)
        return max_minute, counter[max_minute]


class ReposeRecord():

    def __init__(self, path):
        self.guards = {}
        self.parse(path)

    def get_guard(self, id):
        guard =self.guards.get(id, None)
        if not guard:
            guard = Guard(id)
            self.guards[id] = guard
        return guard

    def parse_time(self, entry):
        # Time stamp: [1518-11-01 00:00]
        match = re.match(r"\[(\d+[-]\d+[-]\d+) (\d+):(\d+)\]", entry)
        day, hour, minute = match.groups()

        # Add a day if the shift started yesterday.
        if hour == "23":
            date = datetime.strptime(day, "%Y-%m-%d")
            date += timedelta(days=1)
            day = date.strftime("%Y-%m-%d")
            minute = "0"

        return day, int(minute)

    def parse(self, path):
        with open(path) as f:
            entries = sorted(f.readlines())

        guard = None

        for entry in entries:
            entry = entry.strip()
            #print(entry)

            # Analyze first part of entry.
            day, minute = self.parse_time(entry)

            # Analyze second part of entry.
            match = re.search(r"Guard [#](\d+)", entry)
            if match:
                id = match.group(1)
                guard = self.get_guard(id)
                guard.start_shift(day, minute)
            elif entry.endswith("falls asleep"):
                guard.falls_asleep(day, minute)
            elif entry.endswith("wakes up"):
                guard.wakes_up(day, minute)
            else:
                print("WTF?")

    def get_most_sleeping_guard(self):
        return max(self.guards.values(), key=lambda g: g.get_minutes_asleep())

    def get_most_frequent_guard_and_minute(self):
        freq_map = {}
        for guard in self.guards.values():
            max_minute, freq = guard.get_max_minute()
            if max_minute:
                freq_map[freq] = (guard, max_minute)
        highest_freq = max(freq_map)
        return freq_map[highest_freq]


rec = ReposeRecord("inputs/04.txt")

# a
max_guard = rec.get_most_sleeping_guard()
max_minute, _ = max_guard.get_max_minute()
print(max_guard.id * max_minute)

# b
max_guard, max_minute = rec.get_most_frequent_guard_and_minute()
print(max_guard.id * max_minute)


# Tests
test_path = "inputs/04_test.txt"

def test_a():
    rec = ReposeRecord(test_path)
    max_guard = rec.get_most_sleeping_guard()
    max_minute, _ = max_guard.get_max_minute()
    assert max_guard.id == 10
    assert max_minute == 24

def test_b():
    rec = ReposeRecord(test_path)
    max_guard, max_minute = rec.get_most_frequent_guard_and_minute()
    assert max_guard.id == 99
    assert max_minute == 45
