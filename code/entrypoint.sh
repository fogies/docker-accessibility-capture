#!/bin/bash

while [[ $# > 1 ]]
do
key="$1"
emulog="logs/emulog.txt"
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


echo "no" | /usr/local/android-sdk/tools/android create avd -f -n test -t ${EMULATOR} --abi default/${ARCH} >>$emulog
echo "no" | /usr/local/android-sdk/tools/emulator64-${EMU} -avd test -noaudio -no-window -gpu off -verbose -qemu -usbdevice tablet -vnc :0 &
adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > ./logs/screen11.png
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
echo "installing">>$emulog
adb install ./data/app.apk >>$emulog
#adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > ./logs/screen2.png
#ls /usr/local/android-sdk/build-tools/
echo "getting main screenshot" >>$emulog
#dos2unix /usr/local/android-sdk/build-tools/22.0.1/*
#package="$(/usr/local/android-sdk/build-tools/22.0.1/aapt dump badging /stuff/app.apk | grep package | awk '{print $2}' | sed s/name=//g | sed s/\'//g)"
#package="$(/usr/local/android-sdk/build-tools/22.0.1/aapt.exe dump badging /stuff/app.apk | grep package | awk '{print $2}' | sed s/name=//g | sed s/\'//g)"
#package="$(./usr/local/android-sdk/build-tools/22.0.1/aapt dump badging /stuff/app.apk | grep package | awk '{print $2}' | sed s/name=//g | sed s/\'//g)"

#package="com.a1.quiz.ged.free"
#activity="com.a1.quiz.ged.free.MainActivity"
#echo "pkg: " $package >>$emulog
#activity="$(aapt dump badging /data/app.apk | grep launchable-activity | awk '{print $2}' | sed s/name=//g | sed s/\'//g)"
#echo "activity: "  $activity >>$emulog
#to unlock phone
adb shell input keyevent 82
#adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > ./logs/screenunlock.png
monkeyrunner ./code/screenshot.py $package $activity