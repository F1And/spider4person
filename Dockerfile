FROM python:3.7

MAINTAINER juqiang@tezign.com

USER root

ADD . /spider4person/

WORKDIR /spider4person/

ADD requirements.txt requirements.txt

ENV PATH=/usr/local/python3/bin:$PATH

RUN pip install --upgrade pip && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD python3 run.py