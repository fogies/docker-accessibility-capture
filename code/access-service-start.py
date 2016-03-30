# arguments: package, main activity
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time, sys
device = MonkeyRunner.waitForConnection()

#pass as arguments the activity and package name pulled from the apk
f = open('./code/accessPackageInfo.txt', 'r')
package = f.readline().split(":")[1]
#remove new line
package = package[:-1]
print package
activity = f.readline().split(":")[1]
activity = activity[:-1]
print activity
f.close()

runComponent = package + '/' + activity

print "1"
device.wake()
homeScreen = device.takeSnapshot()

# Runs the component
device.startActivity(component=runComponent)
print "app installed"
#time.sleep(10)
print "runComponent: "+runComponent

#Turn on accessibility service
#device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)

#navigate to fill in package
#f = open('./data/packageInfo.txt', 'r')

#appPackage = f.readline().split(":")[1]
#f.close() 
#device.type(appPackage)
time.sleep(10)
screenShot = device.takeSnapshot()
print "writing to : ./logs/accessServicesScreen.png"
screenShot.writeToFile('./logs/accessServicesScreen.png','png')
#device.press('KEYCODE_ENTER',MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DPAD_UP', MonkeyDevice.DOWN_AND_UP)
time.sleep(20)
device.press('KEYCODE_ENTER',MonkeyDevice.DOWN_AND_UP)
time.sleep(20)
#device.press('KEYCODE_ENTER',MonkeyDevice.DOWN_AND_UP)
#time.sleep(20)
screenShot = device.takeSnapshot()
print "writing to : ./logs/Access"+"4"+"Screen.png"
screenShot.writeToFile('./logs/Access'+"4"+'Screen.png','png')
#'tab' past other two accessibility services
#device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)
#open our accessibility service
#device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
#prompt to turn on accessibility service
#device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
#navigate to 'OK'
#device.press('KEYCODE_TAB', MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_TAB', MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)

#screenShot = device.takeSnapshot()
#print "writing to : ./logs/accessOnScreen.png"
#screenShot.writeToFile('./logs/accessOnScreen.png','png')

#back to main page of accessibility service
#device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)

#navigate to fill in package
#f = open('./data/packageInfo.txt', 'r')

#appPackage = f.readline().split(":")[1]
#f.close() 
#device.type(appPackage)

#navigate to set package button
#device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)

# Presses the Menu button
#device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
#print "3"

#time.sleep(20)

#screenShot = device.takeSnapshot()
#print "writing to : ./logs/completeAccessScreen.png"
#screenShot.writeToFile('./logs/completeAccessScreen.png','png')




