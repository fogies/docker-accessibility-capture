from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
#import com.android.provider.Settings
import time, sys
device = MonkeyRunner.waitForConnection()
screenshot = "Access1"

runComponent='com.android.settings/.Settings'
#runComponent='com.android.settings.accessibility/com.android.settings.accessibility.AccessibilitySettings'
#device.press('KEYCODE_ENTER',MonkeyDevice.DOWN_AND_UP)

device.press('KEYCODE_HOME',MonkeyDevice.DOWN_AND_UP)
time.sleep(10)

device.startActivity(component=runComponent)
time.sleep(10)
#device.wake()d

#device.wake()d

for i in range(0,15):
	device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)
	time.sleep(5)
#device.press('KEYCODE_DPAD_UP', MonkeyDevice.DOWN_AND_UP)
#device.press('KEYCODE_DPAD_UP', MonkeyDevice.DOWN_AND_UP)
#device.wake()
time.sleep(10)
screenShot = device.takeSnapshot()
print "writing to : ./logs/"+"SettingsScreen.png"
screenShot.writeToFile('./logs/'+"SettingsScreen.png",'png')
device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)

time.sleep(20)

"""
#device.wake()d

#device.press('KEYCODE_ENTER',MonkeyDevice.DOWN_AND_UP)
time.sleep(5)
#device.press('KEYCODE_DPAD_UP', MonkeyDevice.DOWN_AND_UP)
#time.sleep(10)
#Turn on accessibility service
#device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
#time.sleep(5)
#device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
#time.sleep(5)
"""
screenShot = device.takeSnapshot()
print "writing to : ./logs/"+screenshot+"Screen.png"
screenShot.writeToFile('./logs/'+screenshot+'Screen.png','png')
#device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
#time.sleep(5)
#screenShot = device.takeSnapshot()
#print "writing to : ./logs/Access1Screen.png"
#screenShot.writeToFile('./logs/Access1Screen.png','png')
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
#print "writing to : ./logs/Access2Screen.png"
#screenShot.writeToFile('./logs/AccessScreen.png','png')