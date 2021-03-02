from time import sleep
from datetime import timedelta
from playsound import playsound
from threading import Thread

import tkinter as tk

import argparse


_BASIC_CONFIG = {
    'font' : ("Arial", 18),
    'foreground' : 'white',
    'background' : 'black'
}


class GraphicTimer:
    def __init__(self, period_type):
        window = tk.Tk()
        window.title('Xitomatl')

        lbl_period_type = tk.Label(
            text = period_type,
            **_BASIC_CONFIG
        )
        lbl_period_type.pack(padx = 5, pady = 5)

        time = tk.StringVar()
        lbl_time = tk.Label(
            textvariable = time,
            width = 4,
            **_BASIC_CONFIG
        )
        lbl_time.pack(padx = 5, pady = 5)

        self.window = window
        self.time = time
    
    def update(self):
        self.window.update()

    def end(self):
        sleep(1)
        self.window.destroy()


class Period:
    def __init__(self, type_, duration, gui = False):
        self.type_ = type_
        self.duration = duration
        if gui:
            self.gui = GraphicTimer(self.type_)
        else:
            self.gui = gui
    
    def start_countdown(self):
        print('Starting ' + self.type_ + ' period.')

        seconds = self.duration * 60

        for second in range(seconds, -1, -1):
            sleep(1)

            str_time = str(timedelta(seconds = second))[2:]

            if self.gui:
                self.gui.time.set(str_time)
                self.gui.update()

            print('\r' + str_time, end = '')

        if self.gui:
            self.gui.end()

        print('\nFinished')

        playsound('marimba-do-re-mi-fa-so.wav')


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