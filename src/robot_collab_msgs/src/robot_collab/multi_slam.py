'''
Created on 2 janv. 2018

@author: younes
'''
from math import *
import random
from matplotlib import pyplot as plot
from threading import Thread
import threading
from multiprocessing.pool import ThreadPool

import thread
from docutils.nodes import thead
from bzrlib.errors import TargetNotBranch
landmarks  = [[20.0, 20.0], [80.0, 80.0], [20.0, 80.0], [80.0, 20.0]]

world_size=100.0
class Robot: 
    def __init__(self):
        self.x=random.random()*world_size
        self.y=random.random()*world_size
        self.orientation=random.random()*2.0*pi
        self.forward_noise=0.0
        self.turn_noise=0.0
        self.sense_noise=0.0
       #def set
    def set_noise(self,new_f_noise,new_t_noise,new_s_noise):
        self.forward_noise=float(new_f_noise)
        self.turn_noise=float(new_t_noise)
        self.sense_noise=float(new_s_noise)
    
    
    def set(self,new_x,new_y,new_orientation):
        
        if new_x<0 or new_x>=world_size:
            raise ValueError,'X coordinate out of bound'
        if new_y<0 or new_y>=world_size:
            raise ValueError, 'Y coordinate out of bout'
        if new_orientation<0 or new_orientation>=2*pi:
            raise ValueError,'Orientation must be in [0 .. 2pi]'
        
        self.x=float(new_x)
        self.y=float(new_y)
        self.orientation=float(new_orientation)
    
    def sense(self):
        Z=[]
        for i in range(len(landmarks)):
            dist=sqrt(((self.x-landmarks[i][0]))**2+(self.y-landmarks[i][1])**2)
            Z.append(dist)
        return Z
    def move(self,turn,forward):
        orientation=self.orientation+float(turn)+random.gauss(0.0,self.turn_noise)
        orientation%=2*pi
        
        dist=float(forward)+random.gauss(0.0,self.forward_noise)
        x=self.x+(cos(orientation)*dist)
        y=self.y+(sin(orientation)*dist)
        x%=world_size
        y%=world_size
        
        res=robot()
        res.set(x,y,orientation)
        res.set_noise(self.forward_noise, self.turn_noise, self.sense_noise)
        return res
    
    def Gaussian(self,mu,sigma,x):
        return exp(-((mu-x)**2)/(sigma**2)/2.0)/sqrt(2.0*pi*(sigma**2))
    def run(self):
      print "lll"
      # the code executed when the thread in run
      
    def measurement_prob(self,measurement):
        prob=1.0
        for i in range(len(landmarks)):
            dist=sqrt((self.x-landmarks[i][0])**2+(self.y-landmarks[i][1])**2)
            prob*=self.Gaussian(dist,self.sense_noise,measurement[i])
        return prob
        
    def __repr__(self):
        return '[x=%.6s y =%.6s orient=%.6s]'%(str(self.x),str(self.y),str(self.orientation))




# number of particles
N=10
# number od steps

T=100

# the particles of all steps
p_all_steps=[]

def someFunc(robot_id):
    p=[]
    myrobot=robot()

    for i in range(N):
            r=robot()
            r.set_noise(0.05, 0.05, 5.0)
            p.append(r)
            
    for t in range(T):
        myrobot=myrobot.move(0.1,0.5)
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
        
        #re-sampling
        for i in range(N):
            beta+=random.random()*2.0*mw
            while beta>w[index]:
                beta-=w[index]
                index=(index+1)%N
            p3.append(p[index])
        p=p3
            
        print robot_id,p
        
        px=[]
        py=[]
        
        for i in range(len(p)):
            px.append(p[i].x)
            py.append(p[i].y)
        p_all_steps.append([p])
        #print p_all_steps
        #plot.plot(px,py,'bo')
        #plot.pause(0.1)
    return p_all_steps
    







#  call this function each time that we want to get data
def getData(robot_id,coord):
    print coord
    p=[]
    myrobot=robot()
    for i in range(N):
            r=robot()
            r.set_noise(0.05, 0.05, 5.0)
            p.append(r)
            
    myrobot.set(coord[0],coord[1],coord[2])
    
    myrobot=myrobot.move(0.1,0.5)
    
    xr=myrobot.x
    yr=myrobot.y
    thr=myrobot.orientation
    cood=[xr,yr,thr]
    print myrobot.x
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
    
    #re-sampling
    for i in range(N):
        beta+=random.random()*2.0*mw
        while beta>w[index]:
            beta-=w[index]
            index=(index+1)%N
        p3.append(p[index])
    p=p3
        
    #print "jjjjjjjjjjjjjjjjj",robot_id,p
    
    #print p_all_steps
    #plot.plot(px,py,'bo')
    #plot.pause(0.1)
    return coord













