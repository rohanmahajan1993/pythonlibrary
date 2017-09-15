import os
import protocols_pb2
import time

BLOCK_SIZE = 8192

def process_server_directory(basefile, timestep):
     protobufobjects = protocols_pb2.ServerResponse() 
     print "the time is", time.time()
     protobufobjects.timestamp = time.time()
     tuples = os.walk(basefile) 
     for directory, _, filenames in tuples:
       print os.path.getmtime(directory)
       if os.path.getmtime(directory) > timestep: 
         protobufobject = protobufobjects.files.add()
         protobufobject.filename = directory
         protobufobject.isDirectory = True
       for filename in filenames:        
          full_name = os.path.join(directory, filename)
          if not os.path.isdir(full_name) and os.path.getmtime(full_name) > timestep:
	    protobufobject = protobufobjects.files.add()
            protobufobject.filename = full_name
            protobufobject.isDirectory = False
	    file_content = file_read(full_name)
            protobufobject.fileContent = file_content
     return protobufobjects

def process_client_directory(ServerResponse):
   files = ServerResponse.files
   for file in files:
         filename = file.filename
         clientname = os.path.join("clientdir", filename)          
         print "clientname is", clientname
	 if not os.path.exists(clientname):
           if file.isDirectory:
	      os.mkdir(clientname)
           else:
              file_write(clientname, file.fileContent)
	      print "we have a filename" + file.filename

def generate_checksum(filename):
    with open(filename, "rb") as fp:
        bytes = fp.read(BLOCK_SIZE)

def file_read(filename):
  with open(filename, "rb") as fp:
    bytes = fp.read()
    return bytes

def file_write(filename, bytes):
  with open(filename, "wb") as fp:
     fp.write(bytes)

