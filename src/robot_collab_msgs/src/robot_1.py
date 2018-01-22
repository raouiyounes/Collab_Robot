#!/usr/bin/env python

import rospy
from  robot_collab.multi_slam import Robot
from std_msgs.msg import String

from robot_collab_msgs.msg import data_col as robot_collabMsg


myrobot=Robot()

N=1000

for i in range(3):
    print "jkjj"
    r=Robot()
    r.set_noise(0.05,0.05,5.0)
 

def computeData(pub_data):
    print "kleeeeeeeeeklklk"
    rb1=robot_collabMsg()
    myrobot.move(0.1,0.5)
    
    Z=myrobot.sense()
    p2=[]
    for i in range(N):
        p2.append(p[i].move(0.1,0.5))
    p=p2
    w=[]
    for i in range(N):
        w.append(p[i].measurement_prob(Z))
    p3=[]
    index=int(random.random()*N)
    beta=0.0
    mw=max(w)
    
    for i in range(N):
        beta+=random.random()*2.0*mw
        while beta>w[index]:
            beta-=w[index]
            index=(index+1)%N
        p3.append(p[index])
    p=p3
    
    # copy the data of pose and observation into the message arrays
    
    
    
    for i in range(len(p)):
        rb1.particlesX[i]=p[i].x
        rb1.particlesY[i]=p[i].y
        rb1.particlesTh[i]=p[i].orientation
        rb1.weight[i]=w[i]
    for j in range(len(Z)):
        rb1.observation[j]=Z[j]
        
    
    pub_data.publish(rb1)
    
    
def listener():
    
    print "klklkl"
    
    pub_data=rospy.Publisher("/robot/robot1",robot_collabMsg,queue_size=0)
    sub=rospy.Subscriber("chatter",robot_collabMsg,computeData,pub_data)
    rospy.spin()
if __name__=='__main__':
    rospy.init_node('robotHoward',anonymous=True)
    listener()


