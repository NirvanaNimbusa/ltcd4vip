FROM python:2.7
LABEL author="Jiateng Liang"
MAINTAINER jiateng.liang@nyu.edu
ENV DOCKYARD_SRC=.
ENV DOCKYARD_SRCHOME=/repos
ENV DOCKYARD_SRCPROJ=/repos/ltcd4vip

RUN mkdir /repos
RUN mkdir repos/ltcd4vip
RUN mkdir repos/log
RUN mkdir repos/log/ltcd4vip

COPY $DOCKYARD_SRC $DOCKYARD_SRCPROJ
WORKDIR $DOCKYARD_SRCPROJ

RUN pip install -r requirements.txt

EXPOSE 12580



