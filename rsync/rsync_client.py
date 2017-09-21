import grpc

import client_helper
import protocols_pb2
import protocols_pb2_grpc
import os

def run(clientPrefix, requestedFilename):
  channel = grpc.insecure_channel('localhost:50051')
  stub = protocols_pb2_grpc.RsyncServiceStub(channel)
  clientRequest = protocols_pb2.ClientRequest(directoryName=requestedFilename)
  client_helper.generate_client_hashes(clientPrefix, requestedFilename, clientRequest)
  response = stub.RsyncMethod(clientRequest)
  client_helper.process_client_directory(clientPrefix, response)
  print("Client succesfully finished")
run("clientprefix", "data")
