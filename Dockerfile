FROM ubuntu
RUN apt-get update
RUN printf 'Y\n' | apt-get install python3-pip 
RUN apt-get install python3-dev 
RUN printf 'Y\n' | apt-get install python3-venv
RUN printf 'Y\n' | apt-get install autoconf 
RUN apt-get install libssl-dev 
ENV TZ=Africa/Johannesburg
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN printf 'Y\n' | apt-get install libxml2-dev 
RUN printf 'Y\n' | apt-get install libxslt1-dev 
RUN printf 'Y\n' | apt-get install libjpeg-dev 
RUN apt-get install libffi-dev 
RUN apt-get install libudev-dev 
RUN apt-get install zlib1g-dev 
RUN printf 'Y\n' | apt-get install pkg-config
RUN printf 'Y\n' | apt-get install libavformat-dev 
RUN apt-get install libavcodec-dev 
RUN printf 'Y\n' | apt-get install libavdevice-dev 
RUN apt-get install libavutil-dev 
RUN apt-get install libswscale-dev 
RUN printf 'Y\n' | apt-get install libavresample-dev 
RUN apt-get install libavfilter-dev
RUN apt-get install nano
WORKDIR /usr/src
COPY ./ ./
RUN python3 setup.py install
RUN pip install -r requirements_all.txt
