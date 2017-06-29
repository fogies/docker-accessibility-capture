#!/bin/bash

#while true
#do
#  a=2
#done
#

cp ./code/test.ini usr/local/android-sdk/platforms/android-19/skins/WQVGA400/hardware.ini

while [[ $# > 1 ]]
do
key="$1"
timestamp=$(date +"%Y.%m.%d_%H.%M.%S")
logsdir="logs/"$timestamp
echo $logsdir
mkdir $logsdir

#Google Scanner: scanner
#Accessibility Capture: capture
technique="capture"
#copy traversal file into the appropriate directory#
#cp ./data/traversal.txt $logsdir/traversal.txt
cp ./data/traversal.yaml $logsdir/traversal.yaml
cp ./code/traverse-app.py $logsdir/traverse-app.py

emulog=$logsdir"/emulog.txt"
touch $emulog
case $key in
    -e|--emulator)
    EMULATOR="$2"
    shift
    ;;
    -a|--arch)
    ARCH="$2"
    shift
    ;;
    --default)
    DEFAULT=YES
    shift
    ;;
    *)
    echo "Use \"-e android-19 -a x86\" to start Android emulator for API19 on X86 architecture.\n"
    ;;
esac
shift
done
echo EMULATOR  = "Requested API: ${EMULATOR} (${ARCH}) emulator.">>$emulog
if [[ -n $1 ]]; then
    echo "Last line of file specified as non-opt/last argument:"
    tail -1 $1
fi

# Run sshd
/usr/sbin/sshd
adb start-server

# Detect ip and forward ADB ports outside to outside interface
ip=$(ifconfig  | grep 'inet addr:'| grep -v '127.0.0.1' | cut -d: -f2 | awk '{ print $1}')
socat tcp-listen:5037,bind=$ip,fork tcp:127.0.0.1:5037 &
socat tcp-listen:5554,bind=$ip,fork tcp:127.0.0.1:5554 &
socat tcp-listen:5555,bind=$ip,fork tcp:127.0.0.1:5555 &

# Set up and run emulator
if [[ $ARCH == *"x86"* ]]
then 
    EMU="x86"
else
    EMU="arm"
fi


echo "no" | /usr/local/android-sdk/tools/android create avd -f -n test -t ${EMULATOR} --skin WQVGA400 --abi default/${ARCH} >>$emulog
echo "no" | /usr/local/android-sdk/tools/emulator64-${EMU} -memory 2000 -avd test -noaudio -no-window -gpu off -verbose -qemu -usbdevice tablet -vnc :0 &
#adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > ./$logsdir/screen11.png
echo "Waiting for emulator to start..." >>$emulog

bootanim=""
failcounter=0
counter=0
until [[ "$bootanim" =~ "stopped" ]]; do
   
   bootanim=`adb -e shell getprop init.svc.bootanim 2>&1`
   if [[ "$bootanim" =~ "not found" ]]; then
      let "failcounter += 1"
      if [[ $failcounter -gt 3 ]]; then
        echo "  Failed to start emulator" >>$emulog
        exit 1
      fi
   fi
   #if [[ $(($counter % 10)) -eq 0 ]]; then
      #adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > ./logs/screen$counter.png
   #fi
   let "counter +=1"
   echo "waiting $counter">>$emulog
   sleep 1
done

#install accessibility analysis tool
accessibility_app=""
if [[ "$technique" = "scanner" ]] 
then
  echo "Google Scanner" >> $emulog
  accessibility_app="./code/scanner/Accessibility_Scanner_v1.1.1.apk"
fi
if [[ "$technique" = "capture" ]] 
then
  echo "Accessibility Capture">> $emulog
  accessibility_app="./code/app_v19.apk" 
fi
echo "installing accessibility service" >>$emulog
adb install $accessibility_app >>$emulog

#install app
echo "installing app">>$emulog
adb install ./data/app.apk >>$emulog


#for snapshots from turning on accessibility service
mkdir ./$logsdir/accessSettings



#turn on accessibility service
echo "here"
file=""
if [[ "$technique" = "scanner" ]] 
then
  echo "Google Scanner" >> $emulog
  file="./code/scanner/accessScannerSettingsTraversal.yaml"
fi
if [[ "$technique" = "capture" ]] 
then
  echo "Accessibility Capture">> $emulog
  file="./code/accessSettingsTraversal.yaml" 
fi
echo "file ${file}">>$emulog
#to unlock phone
adb shell input keyevent 82
#open accessibility setting menu
adb shell am start -a android.settings.ACCESSIBILITY_SETTINGS
#turn on accessibility service
monkeyrunner ./code/traverse-app.py -l $logsdir/accessSettings -t $file -access >>$emulog
echo "after"

#while true
#do
 # a=1
#done

#to unlock phone
adb shell input keyevent 82
#adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > ./logs/screenunlock.png
#echo "mainscreen complete" >>$emulog
echo "traversing app" >>$emulog
traversalFilepath="./$logsdir/traversal.yaml"
packageInfoFile="./data/packageInfo.txt"
monkeyrunner ./code/traverse-app.py -l $logsdir -t $traversalFilepath -i $packageInfoFile >>$emulog
echo "complete">>$emulog
echo "getting logs" >>$emulog
#adb logcat -d *:I | grep TREE_RESULT > ./${logsdir}/tree.txt
adb logcat -d > ./$logsdir/allLog.txt
echo "complete" >>$emulog

