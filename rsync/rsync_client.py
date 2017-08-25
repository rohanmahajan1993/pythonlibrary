import grpc

import file_reader
import protocols_pb2
import protocols_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = protocols_pb2_grpc.RsyncServiceStub(channel)
  requested_filename = 'notes.txt'
  produced_filename = 'actual.txt'
  response = stub.RsyncMethod(protocols_pb2.ClientRequest(filename='notes.txt'))
  file_reader.file_write(produced_filename, response.response)
  print("Greeter client received: " + response.filename)
run()
