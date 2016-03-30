#!/usr/bin/env bash
directory="$(pwd)/apps/"
rootdirectory="$(pwd)"
echo "logging to $gen_log"
gen_log=$rootdirectory"/run-log.out"
echo "logging to $gen_log"
echo "starting makePackageInfo ">>$gen_log
echo "directory $directory" >> $gen_log
for d in $directory*/ ; do
	echo "dir: $d" >> $gen_log
	#dirname=${PWD##*/}          # to assign to a variable
	#echo "$dirname"
	filename=$d"packageInfo.txt"
	echo "file: $filename" >> $gen_log
	cd $d
	package="$(aapt dump badging app.apk | grep package | awk '{print $2}' | sed s/name=//g | sed s/\'//g)"
	activity="$(aapt dump badging app.apk | grep launchable-activity | awk '{print $2}' | sed s/name=//g | sed s/\'//g)"
	echo "writing packgeInfo in "$d>>$gen_log
	echo "package:"$package > $filename
	echo "activity:"$activity >>$filename
done 
#create package info for accessibility service
accessServiceDir=$rootdirectory"/code/"
cd $accessServiceDir
filename=$accessServiceDir"accessPackageInfo.txt"
package="$(aapt dump badging access.apk | grep package | awk '{print $2}' | sed s/name=//g | sed s/\'//g)"
activity="$(aapt dump badging access.apk | grep launchable-activity | awk '{print $2}' | sed s/name=//g | sed s/\'//g)"
echo "writing packgeInfo in "$d>>$gen_log
echo "package:"$package > $filename
echo "activity:"$activity >>$filename