#!/usr/bin/env python

from boat_serial_driver import BoatDriver
import rospy
from mini_wamv.msg import Motor_cmd

class Engine(object):
    def __init__(self):
        rospy.on_shutdown(self.on_shutdown)
        self.sub = rospy.Subscriber("/motor_value",Motor_cmd,callback=self.cb_setMotor,queue_size=1)
        #self.driver = BoatDriver()
        rospy.spin()

    def cb_setMotor(self,msg):
        #self.driver.setSpeed(msg.left,msg.right)
        rospy.loginfo("received %s",msg)

    def on_shutdown(self):
        #self.driver.setSpeed(0,0)
        pass

if __name__ == '__main__':
    rospy.init_node("motor")
    node = Engine()
