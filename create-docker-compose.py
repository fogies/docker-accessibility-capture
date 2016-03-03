import os, sys

if len(sys.argv) != 2:
	print ("usage: \n python create-docker-compose.py <root_directory_path> \n if root directory is current directory use .")
else:
	rootdir = sys.argv[1]
	if rootdir == ".":
		rootdir = os.getcwd()
	print("rootdir:"+rootdir)
	appsdir = rootdir +"/apps"
	for subdir in os.listdir(appsdir):
			#print (subdir)
			filepath=appsdir + '/' + subdir 
			#print (filepath)
			filename = "local-docker-compose.yml"
			fullfilename = filepath+'/'+filename
			print("writing file:")
			print (fullfilename)
			f = open(fullfilename, 'w')
			f.write(
				"apcrawler: \n"+
				"    volumes: \n"+
	    		"        - " + rootdir +"/code:/code\n" +
	    		"        - "+ filepath +":/data \n" +
				"        - " + filepath +"/logs:/logs \n"
				)
			f.close()
			#for file in files:
				#filepath = subdir + os.sep +file
				#p#rint (filepath)


