from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
#import com.android.provider.Settings
import time, sys, os.path
print sys.path
sys.path.append(os.path.join('/usr/lib/python2.7/dist-packages/'))
print sys.path
import yaml

def yaml_loader(filepath):
	file_descriptor = open(filepath, "r")
	data = yaml.load(file_descriptor)
	return data

def start_app(device):
	f = open('./data/packageInfo.txt', 'r')
	package = f.readline().split(":")[1]
	#remove new line
	package = package[:-1]
	print package
	activity = f.readline().split(":")[1]
	activity = activity[:-1]
	print activity
	f.close()
	runComponent = package + '/' + activity
	device.wake()
	device.startActivity(component=runComponent)

if __name__ == "__main__":
	print "traversing"
	device = MonkeyRunner.waitForConnection()
	count=1
	logsdir=sys.argv[1]
	filename="screen"
	traversal_filepath = './'+logsdir+'/traversal.yaml'
	#traversal_filepath = './data/traversal.yaml'
	traversal_file_data = yaml_loader(traversal_filepath)
	print "traversal data: "
	print traversal_file_data
	#start app
	start_app(device)
	traversal_info = traversal_file_data['traversal']
	for traversal_info_key, traversal_info_value in traversal_info.iteritems():
		print "key"
		print traversal_info_key 
		print "\nvalue:"
		print traversal_info_value
		if(traversal_info_key == "commands"):
			for traversal_step in traversal_info_value:
				#if traversal_value == "action":
				#	action = traversal_value
				if traversal_step['type'] == "click":
					coord = traversal_step['coords']
					print "coords: "+str(traversal_step['coords']) 
					device.wake()
					device.touch(int(coord[0]),int(coord[1]),'DOWN_AND_UP')
				elif traversal_step['type'] == "wait":
					time.sleep(traversal_step['time'])
				##########################
				#if traversal_key == "capture":
				#	capture = traversal_value
				if traversal_step['type'] == "screenshot":
					device.wake()
					screenShot = device.takeSnapshot()
					print "writing to : ./"+logsdir+"/"+filename+str(count)+".png"
					screenShot.writeToFile('./'+logsdir+'/'+filename+str(count)+".png",'png')
					count=count+1
	print "just traversal_info:"
	print traversal_info
	print "\nend traversal"
'''

	f = open('./'+logsdir+'/traversal.txt', 'r')
	for line in f:
		coord = line.split(",")
		print "coord: x="+coord[0]+" y="+coord[1]
		device.touch(int(coord[0]),int(coord[1]),'DOWN_AND_UP')
		time.sleep(60)
		screenShot = device.takeSnapshot()
		print "writing to : ./"+logsdir+"/"+filename+str(count)+".png"
		screenShot.writeToFile('./'+logsdir+'/'+filename+str(count)+".png",'png')
		count=count+1
	f.close()
	print "traversal complete"
'''