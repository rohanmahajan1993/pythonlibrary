import grpc

import protocols_pb2
import protocols_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = protocols_pb2_grpc.RsyncServiceStub(channel)
  response = stub.RsyncMethod(protocols_pb2.ClientRequest(filename='you'))
  print("Greeter client received: " + response.filename)
run()
