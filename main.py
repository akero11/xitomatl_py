from time import sleep

import tkinter as tk


_BASIC_PACK = {
    'side' : tk.LEFT,
    'padx' : 5,
    'pady' : 5
}

_BASIC_CONFIG = {
    'font' : ("Arial", 18),
    'foreground' : 'white',
    'background' : 'black'
}

class Period:
    def __init__(self, type_, duration):
        self.type_ = type_
        self.duration = duration
    
    def start(self):
        sleep(self.duration)


class Session:
    def __init__(self, work_minutes = 30, rest_minutes = 6):
        self.work_minutes = work_minutes
        self.rest_minutes = rest_minutes

    def start(self):
        work = Period('Work', self.work_minutes)
        work.start()

        rest = Period('Rest', self.rest_minutes)
        rest.start()


class Block:
    def __init__(self, sessions = 4, work_minutes = 30, rest_minutes = 6):
        self.sessions = sessions
        self.work_minutes = work_minutes
        self.rest_minutes = rest_minutes

    def start(self):
        for _ in range(self.sessions):
            session = Session(self.work_minutes, self.rest_minutes)
            session.start()


if __name__ == '__main__':
    print('Welcome')

    # Window [0]
    window = tk.Tk()
    window.title('Xitomatl')

    # Options [1]
    frm_options = tk.Frame()

    # Sessions per block [1.1]
    frm_sessions_per_block = tk.Frame(master = frm_options)
    # Label [1.1.1]
    lbl_sessions_per_block = tk.Label(
        master = frm_sessions_per_block,
        text = 'Sessions per block :',
        **_BASIC_CONFIG
    )
    lbl_sessions_per_block.pack(**_BASIC_PACK)
    # Entry [1.1.2]
    ent_sessions_per_block = tk.Entry(
        master = frm_sessions_per_block,
        **_BASIC_CONFIG,
        width = 3,
        justify = tk.CENTER
    )
    ent_sessions_per_block.pack(**_BASIC_PACK)
    ent_sessions_per_block.insert(0, '0')
    # Packing
    frm_sessions_per_block.pack(side = tk.LEFT)

    # Periods [1.2]
    frm_periods = tk.Frame(master = frm_options)

    # Work_minutes [1.2.1]
    frm_work = tk.Frame(master = frm_periods)
    # Label [1.2.1.1]
    lbl_work = tk.Label(
        master = frm_work,
        text = 'Working minutes',
        **_BASIC_CONFIG
    )
    lbl_work.pack(**_BASIC_PACK)
    # Entry [1.2.1.2]
    ent_work = tk.Entry(
        master = frm_work,
        **_BASIC_CONFIG,
        width = 5,
        justify = tk.CENTER
    )
    ent_work.pack(**_BASIC_PACK)
    ent_work.insert(0, '000')
    # Packing
    frm_work.pack()

    # Rest minutes[1.2.2]
    frm_rest = tk.Frame(master = frm_periods)
    # Label [1.2.2.1]
    lbl_rest_minutes = tk.Label(
        master = frm_rest,
        text = 'Resting minutes',
        **_BASIC_CONFIG
    )
    lbl_rest_minutes.pack(**_BASIC_PACK)
    # Entry [1.2.2.2]
    ent_rest_minutes = tk.Entry(
        master = frm_rest,
        **_BASIC_CONFIG,
        width = 5,
        justify = tk.CENTER
    )
    ent_rest_minutes.pack(**_BASIC_PACK)
    ent_rest_minutes.insert(0, '000')
    # Packing
    frm_rest.pack()

    # Packing
    frm_periods.pack(side = tk.LEFT)

    # Packing
    frm_options.pack()

    # Start [2]
    btn_start = tk.Button(
        text = 'Start block',
        **_BASIC_CONFIG,
        command = ...
    )
    #Packing
    btn_start.pack(padx = 5, pady = 5)

    window.mainloop()