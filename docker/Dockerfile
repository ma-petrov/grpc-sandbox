FROM continuumio/anaconda3
EXPOSE 8080
RUN pip3 install grpcio
RUN pip3 install grpcio-tools
RUN mkdir /opt/grpc-server
CMD python3 /opt/grpc-server/server.py