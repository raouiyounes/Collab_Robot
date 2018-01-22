#! /usr/bin/env python
import rospy
import numpy as np
from robot_collab_msgs.msg import data_col as robot_collabMsg



def callback_robot2(msg_data):
    print msg_data.particlesX[0],"particle of index 0"





def listener_robot2():
    sub=rospy.Subscriber("/robot/robot1",robot_collabMsg,callback_robot2)
    rospy.spin()
    
    
    
if __name__=='__main__':
    rospy.init_node("robot_1_node")
    listener_robot2()