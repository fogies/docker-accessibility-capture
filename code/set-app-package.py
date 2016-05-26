from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
#import com.android.provider.Settings
import time, sys
refFile = './logs/passedScreens/ServiceScreen/serviceScreen'
ref_x=0
ref_y=20
ref_w=240
ref_h=380
ACCEPTANCE = 1.0
device = MonkeyRunner.waitForConnection()
count=1
logsdir=sys.argv[1]
filename="ServiceScreen/serviceScreen"
#device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)

#runComponent='com.android.settings/.Settings'
#runComponent='com.android.settings/com.android.settings.ACCESSIBILITY_SETTINGS'

#open accessibility service
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
count=1
# Runs the component
device.startActivity(component=runComponent)
#time.sleep(10)
print "runComponent: "+runComponent
time.sleep(10)
#compare to correct
#reference = MonkeyRunner.loadImageFromFile(refFile+str(count)+".png")
#reference = reference.getSubImage(ref_x, ref_y,ref_w,ref_h)
screenShot = device.takeSnapshot()
#subScreen = screenshot.getSubImage(ref_x, ref_y,ref_w,ref_h)
failcount = 0;
#print "comparing to " + refFile+str(count)+".png"
#try three times to get correct screenshot before giving up
#while subScreen.sameAs(reference, ACCEPTANCE) and failCount<2:
#	print "compare failed"
#	print "writing to ./"+logsdir+"/"+filename+str(count)+"_fail"+str(failCount)+".png"
#	screenShot.writeToFile('./'+logsdir+"/"+filename+str(count)+"_fail"+str(failCount)+".png",'png')
#	failCount=failCount+1
#	#give extra time in case it's just slow to load
#	time.sleep(10)
#	screenShot=device.takeSnapshot()
#	subScreen=subScreen = screenshot.getSubImage(ref_x, ref_y,ref_w,ref_h)
#if never succeeded, quit, else continue
#if failCount == 2:
#	print "FAIL!"
print "writing to : ./"+logsdir+"/"+filename+str(count)+".png"
screenShot.writeToFile('./'+logsdir+'/'+filename+str(count)+".png",'png')
count=count+1
#navigate to filling in app package name
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP)
time.sleep(5)
screenShot = device.takeSnapshot()
#check if screenshot matches correct screenshot
print "writing to : ./"+logsdir+"/"+filename+str(count)+".png"
screenShot.writeToFile('./'+logsdir+'/'+filename+str(count)+".png",'png')
count=count+1

#find and fill in package info
f = open('./data/packageInfo.txt', 'r')

appPackage = f.readline().split(":")[1]
#delete new line
appPackage = appPackage[:-1]
f.close() 
device.type(appPackage)
#delete new line
#device.press('KEYCODE_DEL',MonkeyDevice.DOWN_AND_UP)
time.sleep(5)
screenShot = device.takeSnapshot()
print "writing to : ./"+logsdir+"/"+filename+str(count)+".png"
screenShot.writeToFile('./'+logsdir+'/'+filename+str(count)+".png",'png')
count=count+1



#set package
device.press('KEYCODE_DPAD_DOWN',MonkeyDevice.DOWN_AND_UP)
time.sleep(6)
device.press('KEYCODE_ENTER',MonkeyDevice.DOWN_AND_UP)
time.sleep(5)
screenShot = device.takeSnapshot()
print "writing to : ./"+logsdir+"/"+filename+str(count)+".png"
screenShot.writeToFile('./'+logsdir+'/'+filename+str(count)+".png",'png')
count=count+1
