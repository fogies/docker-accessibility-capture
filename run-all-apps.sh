#!/usr/bin/env bash
directory="$(pwd)/apps/"
rootdirectory="$(pwd)"
echo "logging to $gen_log"
gen_log=$rootdirectory"/run-log.out"
echo "logging to $gen_log"
echo "starting run-all-apps.sh ">>$gen_log
#rootdirectory="C:/Users/ansross/Documents/Research/Android_Accessability_Capture/Code/dockerEmu/Android-Ap-Crawler/"
rootdockercompose="$rootdirectory""/docker-compose.yml"
echo "directory $directory" >> $gen_log
echo "root $rootdockercompose" >> $gen_log
for d in $directory*/ ; do
	echo "dir: $d" >> $gen_log
	#dirname=${PWD##*/}          # to assign to a variable
	#echo "$dirname"
	filename=$d"docker-compose.yml"
	echo "file: $filename" >> $gen_log
	localdockercompose="$d""local-docker-compose.yml"
	echo "local: $localdockercompose" >> $gen_log
	dcao-merge -o $filename $rootdockercompose $localdockercompose
	cd $d
	local_log=$d"/log.out"
	echo "current dirctory: " >> $gen_log
	pwd >> $gen_log
	echo "build start">>$gen_log
	echo "build log: $local_log"
	echo "build log begin ">>$local_log
	docker-compose build >> $local_log
	echo "build complete">>$gen_log
	echo "build complete">>$local_log
	echo "docker-compose up start">>$gen_log
	echo "up log : $local_log" >>$gen_log
	echo "docker-compose up start">>$local_log
	docker-compose up >> $local_log
	echo "run complete">>$gen_log
	echo "run complete">>$local_log
done 
