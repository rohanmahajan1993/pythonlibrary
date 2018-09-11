import grpc
import time
import file_reader

import protocols_pb2
import protocols_pb2_grpc

from concurrent import futures

class Rsync(protocols_pb2_grpc.RsyncServiceServicer):
   def RsyncMethod(self, request, context):
     return file_reader.process_server_directory(request.filename, request.timestamp)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  protocols_pb2_grpc.add_RsyncServiceServicer_to_server(Rsync(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(10000)
  except KeyboardInterrupt:
    server.stop(0)
serve()