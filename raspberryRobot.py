#!/usr/bin/env python
# coding=UTF-8
#
#author:chenke
#mail:lingqi1818@gmail.com
#
import web
from raspberryDriver import rp5
import time
class Robot:
    #移动
    #前进x=0,y=0
    #后退x=1,y=1
    #左转弯x=1,y=0
    #右转弯x=0,y=1
    def move(self,x,y):
        if x==0 and y==0:
            rp5.forward()
        if x==1 and y==1:
            rp5.back()
        if x==1 and y==0:
            rp5.left()
        if x==0 and y==1:
            rp5.right()
        time.sleep(1)
        rp5.stop()
    #停止逻辑
    def stop(self):
        rp5.stop()
    
    #摄像截图
    def capture(self,flag):
        print "capture"
    
    #探测逻辑
    def detect(self,flag):
        print "探测"

    #听力逻辑
    def listen(self,data):
        print "listen",data
    
    #说话逻辑
    def say(self,data):
        print "say",data

myrobot=Robot()
#myrobot.move(1,2)
#myrobot.detect(1)
#myrobot.capture(1)
urls = ('/console', 'Console')
app = web.application(urls, globals())
class Console:        
   def GET(self):
       param = web.input()
       if param=={}:
            print "param is null"
       else:
            action = param.action
            if action=="forward":
                myrobot.move(0,0)
            if action=="back":
                myrobot.move(1,1)
            if action=="left":
                myrobot.move(1,0)
            if action=="right":
                myrobot.move(0,1)
       console = web.template.frender('console.html')
       return console()

if __name__ == "__main__":
    app.run()

