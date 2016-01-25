
# docker-accessibility-capture
Definitely need a renaming :)

# Docker Android Ap Crawler

## dependencies:

* docker https://www.docker.com/
...docker-compose https://docs.docker.com/compose/install/
...'pip install docker-compose'
...compose-addons https://github.com/dnephin/compose-addons:
...pip install compose-addons


## directory structure:

	root:
	 - run-all-apps.sh
	 - create-base-docker-compose.py
	 - create-docker-compose.py
	 - Dockerfile

	 - Directory: code
	   -- screenshot.py
	   -- start-emulator

	 - Directory: apps
	   -- Directory: <APP1>
	      --- app.apk
	   -- Directory: <APP2>
	      --- app.apk
	 etc

 the directory name for each app can be anything
 the apk within that directory *must* be named app.apk


after installing dependencies run:
python create-base-docker-compose.py <root_directory_path>

## scripts
### create-base-docker-compose.py

`python create-docker-compose.py <root_directory_path>`

 if root directory is current directory use .

 creates the base docker-compose file in root directory that each app's docker-compose file is merged with. This should be run once to get base and then can be modified for any local additions as needed.

 Dockerfile location is specified here

### create-docker-compose.py

`python create-docker-compose.py <root_directory_path>`

if root directory is current directory use .

creates individual docker-compose files for each app in that app's directory. It will mount the approprate directories for getting the code and apk to the emulator as well as the log files to get the output from the virtual machine.

this file will be merged with the base docker-compose file

this should be run any time another app is added or the base docker-compose is modified. *It will overwrite existing individual docker-compose files.* If an app's docker-compose is individually modified, it should be preserved before rerunning create-docker-compose  

### run-all-apps.sh
`bash run-all-apps.sh`

must be run in the root directory

will merge individual app's docker-compose with base docker-compose. will then build and run a container for each app in succession. These are not parallel. If one app's run hang, the app's after it will not be built and run




