import grpc

import file_reader
import protocols_pb2
import protocols_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = protocols_pb2_grpc.RsyncServiceStub(channel)
  requested_filename = 'sampledir'
  produced_filename = 'sampledirtester'
  response = stub.RsyncMethod(protocols_pb2.ClientRequest(filename=requested_filename))
  file_reader.file_write(produced_filename, response.response)
  print("Greeter client received: " + response.filename)
run()
