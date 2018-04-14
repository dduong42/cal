import argparse
from datetime import date

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

WIDTH = 7 * 2 + 6

parser = argparse.ArgumentParser(description='Calendar')
parser.add_argument('-m', type=int, choices=list(range(1, 13)))


def main():
    args = parser.parse_args()
    today = date.today()
    highlight = not args.m or (args.m == today.month)
    month = args.m or today.month

    for day in range(28, 32):
        try:
            last_day = date(year=today.year, month=month, day=day)
        except ValueError:
            break

    first_day_month = date(year=today.year, month=month, day=1)
    nb_spaces = (first_day_month.weekday() + 1
                 if first_day_month.weekday() < SUNDAY else 0)
    days = ['  ' for _ in range(nb_spaces)]
    days.extend(
        '\x1B[7m{:2d}\x1b[0m'.format(day) if day == today.day and highlight
        else '{:2d}'.format(day)
        for day in range(1, last_day.day + 1))

    calendar_month = first_day_month.strftime('%B %Y').center(WIDTH)
    print(calendar_month)
    print('Su Mo Tu We Th Fr Sa')
    for i in range(0, len(days), 7):
        line = days[i:i+7]
        print(' '.join(line))


if __name__ == '__main__':
    main()
