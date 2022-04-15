import sys, grpc, time
sys.path.append('/opt/grpc-server/grpc')
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from hello_pb2 import SayHelloReply
from hello_pb2_grpc import SayHelloServicer, add_SayHelloServicer_to_server
from count_pb2 import CountReply
from count_pb2_grpc import CounterServicer, add_CounterServicer_to_server

class ServerCounter():
    def count(self):
        while (True):
            time.sleep(1)
            self.counter += 1

    def __init__(self):
        self.counter = 0
        Thread(target=self.count).start()

    def get_counter(self):
        return self.counter

class Greeter(SayHelloServicer):
    def SayHello(self, request, context):
        return SayHelloReply(message='Hello, {}!'.format(request.name))

class Counter(CounterServicer):
    def __init__(self, server_counter):
        super(Counter, self).__init__()
        self.is_reply = False
        self.server_counter = server_counter
        self.is_reply = False

    def Count(self, request, countext):
        while True:
            yield CountReply(counter=self.server_counter.get_counter())
            time.sleep(1)      

def run():
    server_counter = ServerCounter()
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_SayHelloServicer_to_server(Greeter(), server)
    add_CounterServicer_to_server(Counter(server_counter), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    run()