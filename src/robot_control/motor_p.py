#import RPi.GPIO as IO
import time
import os, sys
import rospy
from std_msgs.msg import String
#import msvcrt
import getch
#initializer Ros Publisher
pub = rospy.Publisher('chatter', String, queue_size=10)
rospy.init_node('motor_p', anonymous=True)
rate = rospy.Rate(10) # 10hz


while not rospy.is_shutdown():
   #if msvcrt.kbhit():
   	 key_stroke = getch.getch()
    #    key_stroke = msvcrt.getch()
    	 print(key_stroke)
    	 if key_stroke.decode("utf-8") == "w":
            motor_control = "forward"
            rospy.loginfo(motor_control)
            pub.publish(motor_control)
    	 elif key_stroke.decode("utf-8") == "s":
            motor_control = "backward"
            rospy.loginfo(motor_control)
            pub.publish(motor_control)
    	 elif key_stroke.decode("utf-8") == "d":
            motor_control = "right"
            rospy.loginfo(motor_control)
            pub.publish(motor_control)
    	 elif key_stroke.decode("utf-8") == "a":
            motor_control = "left"
            rospy.loginfo(motor_control)
            pub.publish(motor_control)
rate.sleep()

