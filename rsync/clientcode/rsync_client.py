# Sys hacks that would not be needed if file was in systems libraries
import sys
sys.path.append('../')
import grpc

import client_helper
import protocols_pb2
import protocols_pb2_grpc
import os

def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = protocols_pb2_grpc.RsyncServiceStub(channel)
  requested_filename = 'serverdir'
  clientRequest = protocols_pb2.ClientRequest(directoryName=requested_filename)
  client_helper.generate_client_hashes(requested_filename, clientRequest)
  response = stub.RsyncMethod(clientRequest)
  client_helper.process_client_directory(response)
  print("Client succesfully finished")
run()
