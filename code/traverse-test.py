import yaml
import time, sys
def yaml_loader(filepath):
	file_descriptor = open(filepath, "r")
	data = yaml.load(file_descriptor)
	return data

if __name__ == "__main__":
	#device = MonkeyRunner.waitForConnection()
	count=1
	#logsdir=sys.argv[1]
	filename="screen"
	#traversal_filepath = './'+logsdir+'/traversal.txt'
	traversal_filepath = './data/traversal.yaml'
	traversal_file_data = yaml_loader(traversal_filepath)

	print traversal_file_data
	traversal = traversal_file_data['traversal']
	for traversal_key, traversal_value in traversal.iteritems():
		print traversal_key, traversal_value
		if traversal_key == "action":
			action = traversal_value
			if action['type'] == "click":
				print "coords: "+str(action['coords']) 
	print "just traversal"
	print traversal 
	print "end traversal"