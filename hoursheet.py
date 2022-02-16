from random import gauss
from datetime import timedelta
from datetime import date
import sys

def get_rand_hours(mean):
    return gauss(mean,0.5)

def to_time(flt_hours):
    hours = int(flt_hours)
    minutes = int(float(flt_hours - hours)*60)
    if minutes < 10:
        str_minutes = "0" + str(minutes)
    else:
        str_minutes = str(minutes)
    if hours < 10:
        str_hours = "0" + str(hours)
    else:
        str_hours = str(hours)
    return str_hours + ":" + str_minutes

def get_rand_day(date):
    start = get_rand_hours(10)
    end = get_rand_hours(18)
    diff = end - start
    return date.isoformat() + " " + to_time(start) + " " + to_time(end) + " " + to_time(diff) , diff

def print_sum(sum_hours):
    return "Total: " + to_time(sum_hours)

def get_stundenzettel(startdate,weeks):
    str_out = "Date Start End Total\n"
    sum_hours = 0
    month = -1
    for i in range(weeks):
        day_date = startdate + timedelta(weeks=i)
        if month > 0 and month != day_date.month:
            str_out += print_sum(sum_hours) + "\n"
            sum_hours = 0
        month = day_date.month
        str_day, diff = get_rand_day(day_date)
        sum_hours += diff
        str_out += str_day + "\n"
    return str_out + print_sum(sum_hours) + "\n"

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 hoursheet.py <date> <weeks>")
        print("   Example: python3 hoursheet.py 2021-12-01 12")
    else:
        print(get_stundenzettel(date.fromisoformat(sys.argv[1]),int(sys.argv[2])))

if __name__ == "__main__":
    main()