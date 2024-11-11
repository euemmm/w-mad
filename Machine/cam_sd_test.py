
#import esp
#from Wifi import Sta
#import socket as soc
import camera
#from time import sleep
import time
import uos
import machine
from sdcard import SDCard

cam = False
while cam == False:
    cam = camera.init() # Camera
print('cam')
#camera.init()
img = camera.capture()
print('img captured')
camera.deinit()
print('camera deinit')
#sd = machine.SDCard()
try:
    sd = SDCard(machine.SPI(3), machine.Pin(10))
    print('SD')
except:
    print('errorrr')
'''
uos.mount(sd, "/sd")
print('mounted')
now_file = '-'.join([ str(x) for x in time.localtime()[:6] ]) + '.jpg'
print(now_file)
imgFile = open("/sd/" + now_file, "wb")
print('imgopen')
imgFile.write(img)
print('written')
imgFile.close()
print('closed')
uos.umount("/sd")
print('unmounted')
'''
