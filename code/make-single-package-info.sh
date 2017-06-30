#!/usr/bin/env bash

if [[ $# < 1 ]] 
then
	echo "make-single-package-info.sh <directory of app> \n app must be named app.apk"
else
	directory="$1"
	log=$directory"/package-log.out"
	echo "logging to $log"
	echo "starting makePackageInfo ">>$log
	filename=$directory"/packageInfo.txt"
	echo "file: $filename" >> $log
	cd $directory
	package="$(aapt dump badging app.apk | grep package | awk '{print $2}' | sed s/name=//g | sed s/\'//g)"
	activity="$(aapt dump badging app.apk | grep launchable-activity | awk '{print $2}' | sed s/name=//g | sed s/\'//g)"
	echo "writing packgeInfo in "$directory>>$log
	echo "package:"$package > $filename
	echo "activity:"$activity >>$filename
fi
