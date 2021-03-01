from time import sleep
from datetime import timedelta
from playsound import playsound

import argparse


class Period:
    def __init__(self, type_, duration, gui = False):
        self.type_ = type_
        self.duration = duration
        self.gui = gui
    
    def start_countdown(self):
        print('Starting ' + self.type_ + ' period.')

        seconds = self.duration * 60
    
        if self.gui:
            ...
        else:
            update_timer = lambda second : print('\r' + str(timedelta(seconds = second)), end = '')

        for second in range(seconds, -1, -1):
            sleep(1)

            update_timer(second)

        print(' - finished')

        playsound('marimba-do-re-mi-fa-so.wav', block = False)


def run(type_, duration, gui):
    if duration == None:
        duration = 25 if type_ == 'work' else 5

    period = Period(type_, duration, gui)

    period.start_countdown()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help = False)

    parser.add_argument(
        'type_',
        type = str,
        choices = ('work', 'rest')
    )

    parser.add_argument(
        '-d',
        '--duration',
        type = int
    )

    parser.add_argument(
        '-g',
        '--gui',
        action = 'store_true'
    )

    args = parser.parse_args()

    run(**args.__dict__)