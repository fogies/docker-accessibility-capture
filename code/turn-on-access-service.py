from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
#import com.android.provider.Settings
import time, sys
device = MonkeyRunner.waitForConnection()
count=1
logsdir=sys.argv[1]

device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)
time.sleep(6)
screenShot = device.takeSnapshot()
print "writing to : ./"+logsdir+"/accessSettings/"+str(count)+"Screen.png"
screenShot.writeToFile('./'+logsdir+'/accessSettings/'+str(count)+'AccessScreen.png','png')
count=count+1
device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)
time.sleep(6)
screenShot = device.takeSnapshot()
print "writing to : ./"+logsdir+"/accessSettings/"+str(count)+"Screen.png"
screenShot.writeToFile('./'+logsdir+'/accessSettings/'+str(count)+'AccessScreen.png','png')
count=count+1
device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
time.sleep(10)
screenShot = device.takeSnapshot()
print "writing to : ./"+logsdir+"/accessSettings/"+str(count)+"Screen.png"
screenShot.writeToFile('./'+logsdir+'/accessSettings/'+str(count)+'AccessScreen.png','png')
count=count+1
device.press('KEYCODE_TAB', MonkeyDevice.DOWN_AND_UP)
time.sleep(6)
device.press('KEYCODE_TAB', MonkeyDevice.DOWN_AND_UP)
time.sleep(6)
device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
time.sleep(15)
screenShot = device.takeSnapshot()
print "writing to : ./"+logsdir+"/accessSettings/"+str(count)+"Screen.png"
screenShot.writeToFile('./'+logsdir+'/accessSettings/'+str(count)+'AccessScreen.png','png')
count=count+1
device.press('KEYCODE_TAB', MonkeyDevice.DOWN_AND_UP)
time.sleep(6)
screenShot = device.takeSnapshot()
print "writing to : ./"+logsdir+"/accessSettings/"+str(count)+"Screen.png"
screenShot.writeToFile('./'+logsdir+'/accessSettings/'+str(count)+'AccessScreen.png','png')
count=count+1
device.press('KEYCODE_TAB', MonkeyDevice.DOWN_AND_UP)
time.sleep(6)
screenShot = device.takeSnapshot()
print "writing to : ./"+logsdir+"/accessSettings/"+str(count)+"Screen.png"
screenShot.writeToFile('./'+logsdir+'/accessSettings/'+str(count)+'AccessScreen.png','png')
count=count+1
device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
time.sleep(10)

screenShot = device.takeSnapshot()
print "writing to : ./"+logsdir+"/accessSettings/"+str(count)+"Screen.png"
screenShot.writeToFile('./'+logsdir+'/accessSettings/'+str(count)+'AccessScreen.png','png')
count=count+1