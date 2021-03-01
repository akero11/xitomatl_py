from time import sleep
from datetime import time


class Period:
    def __init__(self, duration):
        self.duration = duration
    
    def start(self):
        seconds = self.duration * 60

        for second in range(seconds+1):
            sleep(1)

            print('\r' + str(time(second = second)), end = '')


if __name__ == '__main__':
    print('Testing for 1 minute.')
    work = Period(1)
    work.start()