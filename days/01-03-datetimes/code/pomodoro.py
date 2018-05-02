from datetime import datetime
from datetime import timedelta
import time


def main():
    # print a header
    print_header()
    # get user input
    start_timer()
    # start timer
    # print update (every 5-mins?)
    # play a sound when finished


def print_header():
    print('--------------------------------')
    print('\tPomodoro Timer')
    print('--------------------------------\n')


def start_timer():
    while True:
        cmd = input('Would you like to [s]tart the pomodoro timer or e[x]it? ')
        cmd = cmd.lower().strip()

        if cmd == 'x':
            print('Goodbye.')
            break
        elif cmd == 's':
            pomodoro_timer()
            break
        else:
            print("Sorry I didn't understand you answer.")


def pomodoro_timer():
    start_time = datetime.today()
    end_time = start_time + timedelta(0, 25 * 60)
    print('Timer started you have {} minutes left.'.format(
        (end_time - start_time).seconds / 60))

    while True:
        now = datetime.today()
        diff = (end_time - now).seconds
        diff_min = diff / 60

        if diff <= 0:
            print('Times up')
            break
        elif (diff_min % 5) == 0:
            print('You have {} minutes left'.format(diff_min))
            time.sleep(60)


if __name__ == '__main__':
    main()
