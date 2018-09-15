import time
import serial

class BoatDriver(object):
    def __init__(self):
        self.port = serial.Serial(
	            port = "/dev/ttyUSB0",
	            baudrate = 9600,
	            bytesize=serial.EIGHTBITS
                )
    def setSpeed(self,left,right):
        vl = int(left*64)
        rl = int(right*64)
        if(vl==rl):
            vl=rl=vl*2
        vl=min(63,vl)
        rl=min(63,rl)
        #print("vl=",vl,"rl=",rl)
        self.port.write(chr(self.encodeToByte(0,rl)))
        time.sleep(0.01)
        self.port.write(chr(self.encodeToByte(1,vl)))
        time.sleep(0.01)
        
    
    def encodeToByte(self,side,value):
        v = abs(value)
        byte = v<<1
        if(value<0):
            byte |= 1
        byte = byte<<1
        byte = byte|side
        return byte
