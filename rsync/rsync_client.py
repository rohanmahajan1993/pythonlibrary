import grpc

import file_reader
import protocols_pb2
import protocols_pb2_grpc

def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = protocols_pb2_grpc.RsyncServiceStub(channel)
  requested_filename = 'serverdir'
  response = stub.RsyncMethod(protocols_pb2.ClientRequest(filename=requested_filename))
  file_reader.process_client_directory(response)
  print("Client succesffully finished")
run()
