# arguments: package, main activity
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time, sys
device = MonkeyRunner.waitForConnection()

#pass as arguments the activity and package name pulled from the apk
print "num args: ", len(sys.argv)
print "args: ", str(sys.argv)
f = open('./data/packageInfo.txt', 'r')
package = f.readline().split(":")[1]
#remove new line
package = package[:-1]
print package
activity = f.readline().split(":")[1]
activity = activity[:-1]
print activity
f.close()
#package = sys.argv[1]
#activity = sys.argv[2]
#package = 'aapt dump badging /tmp/EduGame.apk' | grep package | awk '{print $2}' | sed s/name=//g | sed s/\'//g'

#activity = 'com.zodinplex.main.MainScreen'
#com.example.android.EduGae.MainActivity'

#package=`aapt dumps badging /tmp/EduGame.apk | grep package | awk '{print $2}' | sed s/name=//g | sed s/\'//g`
#package='com.zodinplex.abc.kids.letters.educational.sounds.baby'
#activity=`aapt dump badging /tmp/EduGame.apk | grep Activity | awk '{print $2}' | sed s/name=//g | sed s/\'//g`
runComponent = package + '/' + activity
#device.installPackage('./stuff/app-debug.apk')
#device.installPackage('./data/app.apk')
#time.sleep(20)
print "1"
device.wake()
homeScreen = device.takeSnapshot()
#homeScreen = result.writeToFile('./logs/homeScreen.png','png')
#device.wake();
# Runs the component
device.startActivity(component=runComponent)
print "app installed"
#time.sleep(10)
print "runComponent: "+runComponent
# Presses the Menu button
#device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)
print "3"

time.sleep(20)
screenShot = device.takeSnapshot()
print "writing to : ./logs/mainScreen.png"
screenShot.writeToFile('./logs/mainScreen.png','png')

#apOpen = False
#waitCount = 0
#while not apOpen and waitCount < 10:
	#device.wake();
#	print "4"
#	screenShot = device.takeSnapshot()
#	print "waiting for launch"
	#if not screenShot.sameAs(homeScreen,0.8):
	#	apOpen = True
#		print "writing to : ./logs/mainScreen.png"
#		screenShot.writeToFile('./logs/mainScreen.png','png')
#	else:
#		time.sleep(10)
#	waitCount = waitCount + 1


