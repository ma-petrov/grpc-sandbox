from os import system
from subprocess import check_output

def is_proto_file_type(f):
    return f[-6:] == '.proto'

system('mkdir app/grpc')
files = check_output(['ls', 'app/proto'])
for f in files.decode('utf-8').split('\n')[:-1]:
    if is_proto_file_type(f):
        system(f'python3 -m grpc_tools.protoc -I./app/proto --python_out=./app/grpc --grpc_python_out=./app/grpc ./app/proto/{f}')