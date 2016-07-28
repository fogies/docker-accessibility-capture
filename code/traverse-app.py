from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
#import com.android.provider.Settings
import time, sys, os.path
import subprocess #for running monkey command to start app with package name alone
print sys.path
sys.path.append(os.path.join('/usr/lib/python2.7/dist-packages/'))
print sys.path
import yaml

def yaml_loader(filepath):
	file_descriptor = open(filepath, "r")
	data = yaml.load(file_descriptor)
	return data

def start_app(device, package_info):
	f = open(package_info, 'r')
	package = f.readline().split(":")[1]
	#remove new line
	package = package[:-1]
	print "package:"
	print package
	activity = f.readline().split(":")[1]
	activity = activity[:-1]
	print "activity: "
	print activity
	f.close()

	bashCommand = "adb shell monkey -p "+package+" -c android.intent.category.LAUNCHER 1"
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]
	print "output: "
	print output
	#runComponent = package + '/' + activity
	#device.wake()
	#print runComponent
	#runComponent = 'com.skype.raider/.Main'
	#device.startActivity(component=runComponent)

def check_valid_screen(compImage):
	refFailScreensDir = './logs/failScreens'
	ref_x=0
	ref_y=20
	ref_w=240
	ref_h=3
	ACCEPTANCE = 1.0
	for refFile in os.listdir(refFailScreensDir):
		subScreen = compImage.getSubImage(ref_x, ref_y,ref_w,ref_h)
		failScreen =  MonkeyImage.loadFromFile(refFile)
		if subScreen.sameAs(reference, ACCEPTANCE):
			print "matched failScreen: " + str(refFile)
			return 1
	print "didn't match a fail screen from: " + str(refFailScreensDir)
	return 0

if __name__ == "__main__":
	print "here"
	#parse command line paramenters
	traversal_filepath = ''
	package_info = "./data/packageInfo.txt"
	logsdir=''
	num_args = len(sys.argv)
	arg_iter = 1
	is_access_service = False
	while (arg_iter < num_args):
		print "arg ", arg_iter, ": ", str(sys.argv[arg_iter])
		if sys.argv[arg_iter] == "-l":
			arg_iter += 1
			logsdir = str(sys.argv[arg_iter])
		elif sys.argv[arg_iter] == "-i":
			arg_iter += 1
			package_info = sys.argv[arg_iter]
		elif sys.argv[arg_iter] == "-t":
			arg_iter += 1
			traversal_filepath = sys.argv[arg_iter]#"C:\Users\\ansross\Documents\Research\Android_Accessability_Capture\Code\dockerEmu\\android-emulator-access\code\1traversal.yaml"
			#traversal_filepath = "code/accessSettingsTraversal.yaml"#str(sys.argv[arg_iter])
		elif sys.argv[arg_iter] == "-access":
			is_access_service = True
		else:
			print "unknown parameter flag " + sys.argv[arg_iter]
		arg_iter +=1 
	
	print "traversal filepath:", traversal_filepath
	print "logsdir:", logsdir
	print " package_info:",package_info
	print "traversing"
	device = MonkeyRunner.waitForConnection()
	count=1
	#logsdir=sys.argv[1]
	filename="screen"
	#traversal_filepath = './code/1traversal.yaml'
	#traversal_filepath = './'+'code'+'/traversal.yaml'
	#traversal_filepath = './data/traversal.yaml'
	traversal_file_data = yaml_loader(traversal_filepath)
	print "traversal data: "
	print traversal_file_data
	#start app
	#package_info = sys.argv[2]
	if not is_access_service:
		start_app(device, package_info)
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
				## CLICK ###############
				if traversal_step['type'] == "click":
					coord = traversal_step['coords']
					print "coords: "+str(traversal_step['coords']) 
					device.wake()
					device.touch(int(coord[0]),int(coord[1]),'DOWN_AND_UP')
				elif traversal_step['type'] == "text_entry":
					text = traversal_step['text']
					device.type(text)
				## WAIT ################
				elif traversal_step['type'] == "wait":
					time.sleep(traversal_step['time'])
				##########################
				## DRAG #####
				elif traversal_step['type'] == "drag":
					start = traversal_step['coords_start']
					end = traversal_step['coords_end']
					device.wake()
					device.drag(start, end, float(traversal_step['duration']), 5)

				## SCREENSHOT ##########
				elif traversal_step['type'] == "screenshot":
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