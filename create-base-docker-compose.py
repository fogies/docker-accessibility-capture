import os, sys

if len(sys.argv) != 2:
	print ("usage: \n python create-docker-compose.py <root_directory_path> \n if root directory is current directory use .")
else:
	rootdir = sys.argv[1]
	if rootdir == ".":
		rootdir = os.getcwd()
	fullfilename = rootdir+'/'+"docker-compose.yml"
	print("writing file:")
	print (fullfilename)
	f = open(fullfilename, 'w')
	f.write(
		"apcrawler: \n"+
		"    build: "+rootdir+"\n"+
		"    volumes: \n"+
		"        - " + rootdir +"/code:/code\n"
		)
	f.close()