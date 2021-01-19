from tkinter import *
import time
import RPi.GPIO as io
io.setmode(io.BOARD)
io.setwarnings(False)
Top = Tk()
io.setup(11,io.OUT)
io.setup(15,io.OUT)
io.setup(13,io.OUT)
pr = io.PWM(11,50)
pr.start(5)
pg = io.PWM(15,50)
pg.start(5)
pb = io.PWM(13,50)
pb.start(5)
def updater1(dutyr):
    pr.ChangeDutyCycle(float(dutyr))
    print(dutyr)
def updater2(dutyg):
    pg.ChangeDutyCycle(float(dutyg))
    print(dutyg)    
def updater3(dutyb):
    pb.ChangeDutyCycle(float(dutyb))
    print(dutyb)
w1 = Scale(Top ,from_=0,to =100,orient = HORIZONTAL ,length =500,tickinterval=5,command = updater1)
w1.set(5)
w1.pack()
w2 = Scale(Top ,from_=0,to =100,orient = HORIZONTAL,length =500,tickinterval=5,command = updater2)
w2.set(5)
w2.pack()
w3 = Scale(Top ,from_=0,to =100,orient = HORIZONTAL,length =500,tickinterval=5,command = updater3)
w3.set(5)
w3.pack()
mainloop()
