from time import sleep
from playsound import PlaysoundException, playsound
from threading import Thread

class Period:
    def __init__(self, duration):
        self.duration = duration
    
    def start(self):
        seconds = self.duration * 60

        for n in range(seconds+1):
            sleep(1)
            print(n)
        
        alarm = Thread(
            target = playsound, 
            args = ('marimba-do-re-mi-fa-so.wav',)
        )

        alarm.start()


if __name__ == '__main__':
    print('Testing for 3 seconds')
    work = Period(3)
    work.start()