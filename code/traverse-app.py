from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
#import com.android.provider.Settings
import time, sys
device = MonkeyRunner.waitForConnection()
count=1
logsdir=sys.argv[1]
filename="screen"
f = open('./'+logsdir+'/traversal.txt', 'r')
for line in f:
	coord = line.split(",")
	print "coord: x="+coord[0]+" y="+coord[1]
	device.touch(int(coord[0]),int(coord[1]),'DOWN_AND_UP')
	time.sleep(10)
	screenShot = device.takeSnapshot()
	print "writing to : ./"+logsdir+"/"+filename+str(count)+".png"
	screenShot.writeToFile('./'+logsdir+'/'+filename+str(count)+".png",'png')
	count=count+1

print "traversal complete"