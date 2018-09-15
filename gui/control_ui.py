#!/usr/bin/env python

from Tkinter import *
import math

class commandCanvas(Canvas):
    def __init__(self,infoCanvas,master=None,cnf={},**kw):
        Canvas.__init__(self,master,cnf,**kw)
        self.focus_force()
        self.spCanvas = infoCanvas
        self.bind("<Configure>",self.repaint)
        self.bind("<Motion>",self.draw_dir)
        self.bind("<space>",self.switchToggle)
        self.bind("b",self.boost)
        self.dir = self.create_arc(0,0,0,0)
        self.maxR = 0
        self.switch = False
        self.boosted = False
        self.radius = 0
        self.degree = 0
        self.drawCircle()

    def repaint(self,Event):
        self.delete(ALL)
        self.config(width=Event.width, height=Event.height)
        self.drawCircle()

    def drawCircle(self):
        h = self.winfo_height()
        w = self.winfo_width()
        d = h/4*3
        if(h>w): d=w/4*3
        self.maxR = d/2
        self.circle = self.create_oval(w/2-d/2,h/2-d/2,w/2+d/2,h/2+d/2,dash=(7,3,2,3))

    def boost(self,Event):
        self.boosted = not self.boosted
        self.setState()

    def setState(self):
        if(self.switch):
            r = self.radius
            if(self.boosted):
                self.itemconfigure(self.dir,fill='firebrick3')
                r = self.radius*2
            else:
                self.itemconfigure(self.dir,fill="RoyalBlue1")
            self.spCanvas.drawSpeed(self.degree,r/self.maxR)
        else:
            self.itemconfigure(self.dir,fill='')
            self.spCanvas.drawSpeed(self.degree,0/self.maxR)

    def switchToggle(self,Event):
        #print(self.switch)
        self.switch = not self.switch
        self.setState()
        
    def draw_dir(self,Event):
        self.delete(self.dir)
        h = self.winfo_height()
        w = self.winfo_width()
        x = Event.x-w/2
        y = Event.y-h/2
        self.radius = math.sqrt(math.pow(x,2)+math.pow(y,2))
        if(self.radius>self.maxR): self.radius=self.maxR
        pos = w/2-self.radius,h/2-self.radius,w/2+self.radius,h/2+self.radius
        self.degree = math.atan2(-y,x)*180/math.pi
        self.dir = self.create_arc(pos,start=self.degree-4,extent=8)
        self.setState()
        
    
    def getDir(self):
        return self.dir
        
        
class speedCanvas(Canvas):
    def __init__(self,master=None,cnf={},**kw):
        Canvas.__init__(self,master,cnf,**kw)
        self.bind("<Configure>",self.repaint)
        self.leftBar = self.create_rectangle(0,0,0,0)
        self.rightBar = self.create_rectangle(0,0,0,0)
        self.leftSpeed = 0
        self.rightSpeed = 0
        self.drawBox()

    def repaint(self,Event):
        self.delete(ALL)
        self.config(height=Event.height)
        self.drawBox()

    def drawBox(self):
        y = self.winfo_reqheight()
        x = self.winfo_reqwidth()
        w = 30
        self.leftBox = self.create_rectangle(x/4-w,y/8,x/4+w,y*7/8,dash=(7,3,2,3))
        self.rightBox = self.create_rectangle(x*3/4-w,y/8,x*3/4+w,y*7/8,dash=(7,3,2,3))
    
    def modifySpeed(self,value):
        v = min(value,63)
        v = max(v,-63)
        return v

    def drawSpeed(self,dir,value):
        self.delete(self.leftBar)
        self.delete(self.rightBar)
        rad = math.radians(dir)
        self.leftSpeed = self.modifySpeed(int((math.cos(rad) + math.sin(rad))*value*64/math.sqrt(2)))
        self.rightSpeed = self.modifySpeed(int((-math.cos(rad) + math.sin(rad))*value*64/math.sqrt(2)))
        print "leftSpeed=",self.leftSpeed,"rightSpeed=",self.rightSpeed,"dir=",dir
        y = self.winfo_reqheight()
        x = self.winfo_reqwidth()                    
        print "y=",y               
        w = 30
        m = y*3./8./63.
        self.leftBar = self.create_rectangle(x/4-w,y/2,x/4+w,y/2-self.leftSpeed*m,fill="orange red")
        self.rightBar = self.create_rectangle(x*3/4-w,y/2,x*3/4+w,y/2-self.rightSpeed*m,fill="lawn green")



root = Tk()
root.minsize(700,500)
root.geometry("700x500")
spCanvas = speedCanvas(master=root,width=200,height=500,bg="light gray",highlightthickness=1.5)
cmdCanvas = commandCanvas(infoCanvas=spCanvas,master=root,width=500,height=500,bg="light gray",highlightthickness=0)
spCanvas.pack(side="left",fill=BOTH,expand=TRUE)
cmdCanvas.pack(side="left",fill=BOTH,expand=TRUE)
root.mainloop()


def getLeftSpeed():
    return spCanvas.leftSpeed
def getRightSpeed():
    return spCanvas.rightSpeed
