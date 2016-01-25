# Start with ubuntu 12.04 (i386).
FROM toopher/ubuntu-i386:12.04

RUN echo "here"
# Specially for SSH access and port redirection
ENV ROOTPASSWORD android

# Expose ADB, ADB control and VNC ports
EXPOSE 22
EXPOSE 5554
EXPOSE 5555
EXPOSE 5900

ENV DEBIAN_FRONTEND noninteractive
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-set-selections


# First, install add-apt-repository, sshd and bzip2
RUN apt-get -y update && \
	apt-get -y install \
	bzip2 \
	gcc-multilib \
	python-software-properties \
	ssh \
	&& \
	apt-get clean


# Add oracle-jdk7 to repositories
RUN add-apt-repository ppa:webupd8team/java

# Make sure the package repository is up to date
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list

# Update apt 
# Install oracle-jdk7
RUN apt-get update && \
	apt-get -y install \
	oracle-java7-installer:i386\
    && \
    apt-get clean


# Install android sdk
RUN wget http://dl.google.com/android/android-sdk_r23-linux.tgz
RUN tar -xvzf android-sdk_r23-linux.tgz
RUN mv android-sdk-linux /usr/local/android-sdk

# Add android tools and platform tools to PATH
ENV ANDROID_HOME /usr/local/android-sdk
ENV PATH $PATH:$ANDROID_HOME/tools


# Some preparation before update
RUN chown -R root:root /usr/local/android-sdk/
# install platform-tools for adb
RUN echo "y" | android update sdk --filter tools --no-ui --force
#platform-tools with adb
RUN echo "y" | android update sdk --filter 2 --no-ui --force
RUN echo "y" | android update sdk --filter platform --no-ui --force
RUN echo "y" | android update sdk --filter build-tools-22.0.1 --no-ui -a
#RUN echo "y" | android update sdk --filter sys-img-x86-android-9 --no-ui -a
RUN echo "y" | android update sdk --filter sys-img-x86-android-10 --no-ui -a
#RUN echo "y" | android update sdk --filter sys-img-x86-android-16 --no-ui -a
#RUN echo "y" | android update sdk --filter sys-img-x86-android-18 --no-ui -a
#RUN echo "y" | android update sdk --filter sys-img-x86-android-19 --no-ui -a
RUN echo "y" | android update sdk --filter sys-img-x86-android-21 --no-ui -a
#RUN echo "y" | android update sdk --filter sys-img-x86-android-22 --no-ui -a

#for adb
ENV PATH $PATH:$ANDROID_HOME/platform-tools
#aapt
ENV PATH $PATH:$ANDROID_HOME/build-tools/22.0.1


#COPY test/app.apk /tmp/

RUN apt-get update && \
	apt-get install -y \ 
	dos2unix \
	&& \
	apt-get clean


RUN android list targets

#ADD ./code /code
#RUN dos2unix /code/*
#RUN chmod +x /code/*
#ADD ./apps/GEDPracticeTest /test
#RUN dos2unix /test/*
#RUN chmod +x /test/*

#RUN echo 'n' | android create avd --force -n droid-9 -t android-9 --abi default/x86
RUN echo 'n' | android create avd --force -n droid-10 -t android-10 --abi default/x86
#RUN echo 'n' | android create avd --force -n emu -t android-16 --abi default/x86
#RUN echo 'n' | android create avd --force -n droid-18 -t android-18 --abi default/x86
#RUN echo 'n' | android create avd --force -n droid-19 -t android-19 --abi default/x86
RUN echo 'n' | android create avd --force -n droid-21 -t android-21 --abi default/x86

#RUN echo 'n' | android create avd --force -n droid-22 -t android-22 --abi default/x86

#RUN echo 'n' | android create avd --force -n test -t android-21 --abi default/x86
CMD ["bash", "./code/start-emulator"]
#RUN ls
#RUN adb devices


# add .apk
#RUN adb install tmp/EduGame.apk

