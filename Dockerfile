FROM ubuntu:22.04

RUN useradd user

RUN apt-get update
RUN apt-get install -y python3 python3-pip gcc g++ make cmake

RUN pip3 install requests rich

COPY ./yorn.py /bin/yorn
RUN chmod +x /bin/yorn
COPY ./core/ /bin/core/

RUN mkdir /app/
RUN chown user:user /app/

USER user

WORKDIR /app/

ENTRYPOINT [ "/bin/yorn" ]