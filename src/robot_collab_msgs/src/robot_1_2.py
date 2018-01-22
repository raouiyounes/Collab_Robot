

import rospy
from robot_collab_msgs.msg import data_col as robot_collabMsg
from robot_collab import multi_slam

def talker_robot1():
    
    rospy.Publisher("talker_robot1",robot_collabMsg,queue_size=10)
    
    







if __name__=='__main__':
    
    
    

