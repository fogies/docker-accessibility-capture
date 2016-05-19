from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time, sys
device = MonkeyRunner.waitForConnection()

device.touch(100, 100, 'DOWN_AND_UP')
time.sleep(10)

screenShot = device.takeSnapshot()
print "writing to : ./logs/firstClick.png"
screenShot.writeToFile('./logs/firstClick.png','png')