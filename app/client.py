from threading import Thread
from queue import Queue
from functools import partial
import sys, grpc, time
sys.path.append('/Users/petrov/Repositories/grpc-sandbox/app/grpc')
from hello_pb2 import SayHelloRequest
from hello_pb2_grpc import SayHelloStub
from count_pb2 import CountRequest, CountStreamRequest
from count_pb2_grpc import CounterStub
from observer import Observer, Observable

class CounterService(Observable):
    def _run(self):
        with grpc.insecure_channel('localhost:8070') as channel:
            for response in CounterStub(channel).Count(CountRequest()):
                self.notify(response)

    def run(self):
        Thread(target=self._run).start()

class ConsoleObserver(Observer):
    def update(self, data):
        print(f'{self.name}: {str(data)[:-1]}')

if __name__ == '__main__':
    client = CounterService()
    client.attach(ConsoleObserver('Observer'))
    client.run()
