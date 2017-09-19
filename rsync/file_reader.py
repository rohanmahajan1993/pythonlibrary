import hashlib
import os
import protocols_pb2
import time
import zlib

BLOCK_SIZE = 8192

# Will see if files still exists and need to be deleted
# Find out addition of 
def analyze_client_files(timestamp, clientFiles, deletedFiles, editedFiles):
    clientFileNames = dict()
    for clientFile in clientFiles:
        filename = clientFile.file.filename
        clientFileNames[filename] = clientFile.file.isDirectory
        if os.path.exists(filename) and os.path.isdir(filename) == clientFile.isDirectory:
           last_modified_time = os.path.getmtime(filename)  
           if last_modified_time > timestamp:
               editedFile = editedFiles.add()
               editedFile.filename = filename
               analyze_client_file(clientFile, editedFile.fileEdit)
        else:
            deleted_file = deletedFiles.add()
            deleted_file.isDirectory = clientFile.isDirectory
            deleted_file.filename = filename
    return clientFileNames


def create_client_hashmap(clientFile):
    clientHashMap = dict()
    blockNumber = 0
    for clientHash in clientFile.clientHashes:
        hashList = clientHashMap.get(clientHash.simpleHash, [])
        hashList.append((blockNumber, clientHash.complicatedHash))
        blockNumber += 1
    return clientHashMap

def analyze_client_file(clientFile, fileEdits):
    clientHashMap = create_client_hashmap(clientFile)
    with open(clientFile.file.filename, "rb") as fp:
        new_bytes = fp.read(BLOCK_SIZE)
        current_bytes = ""
        numBlocks = 0
        previousBlock = -5
        while new_bytes != "":
           simpleHash = zlib.adler32(new_bytes) 
           foundBlockMatch = False
           if simpleHash in clientHashMap:
              complicatedServerHash = generateComplicatedHash(bytes)
              hashList = clientHashMap[simpleHash]
              for blockNumber, complicatedHash in hashList:
                if complicatedHash == complicatedServerHash:
                    foundBlockMatch = True
                    if numBlocks == 0 and current_bytes != "":
                        fileEdit = fileEdits.add()
                        fileEdit.isBlockNumber = False
                        fileEdit.fileContent = current_bytes
                        current_bytes = ""
                    elif blockNumber - numBlocks == previousBlock:
                        numBlocks += 1
                    else:
                        fileEdit = fileEdits.add()
                        fileEdit.isBlockNumber = True
                        fileEdit.blockNumber = previousBlock
                        fileEdit.numBlocks = numBlocks
                        numBlocks = 1
                        previousBlock = blockNumber
           if not foundBlockMatch:
               if numBlocks != 0:
                  fileEdit = fileEdits.add()
                  fileEdit.isBlockNumber = True
                  fileEdit.blockNumber = previousBlock
                  fileEdit.numBlocks = numBlocks
                  numBlocks = 0
               current_bytes += new_bytes[0] 
           new_bytes = new_bytes[1] + fp.read(1) 
        if numBlocks != 0:
            fileEdit = fileEdits.add()
            fileEdit.isBlockNumber = True
            fileEdit.blockNumber = previousBlock
            fileEdit.numBlocks = numBlocks
        elif current_bytes != "":
            fileEdit = fileEdits.add()
            fileEdit.isBlockNumber = False
            fileEdit.fileContent = current_bytes

            



#Have to handle weird case where file is deleted and directory is created with same name
#Just find new files
def analyze_server_files(basefile, clientFileNames, new_files):
    tuples = os.walk(basefile) 
    for directory, _, filenames in tuples:
       if directory not in clientFileNames or clientFileNames[directory] != True:
           new_file = new_files.add()
           new_file.file.filename = directory
           new_file.file.isDirectory = True
       for filename in filenames:        
          if not os.path.isdir(filename):
              if filename not in clientFileNames or clientFileNames[filename]:
                full_name = os.path.join(directory, filename)  
                new_file = new_files.add()
                new_file.file.filename = full_name
                new_file.file.isDirectory = False
                file_content = file_read(full_name)
                new_file.fileContent = file_content


def process_server_directory(clientRequest):
     serverResponse = protocols_pb2.ServerResponse() 
     serverResponse.timestamp = time.time()
     clientFileNames = analyze_client_files(clientRequest.timestamp, clientRequest.clientFiles, serverResponse.deletedFiles, serverResponse.editedFiles)
     analyze_server_files(clientRequest.directoryName, clientFileNames, serverResponse.newFiles)

def handle_new_files(new_files):
   for new_file in new_files:
         filename = new_file.file.filename
         clientname = os.path.join("clientdir", filename)          
         if new_file.file.isDirectory:
	      os.mkdir(clientname)
         else:
              file_write(clientname, new_file.fileContent)

def handle_deleted_files(deletedFiles):
    for deleted_file in deletedFiles:
        clientFileName = os.path.join("clientdir", deleted_file.filename)
        if deleted_file.isDirectory: 
            os.rmdir(clientFileName)
        else:
            os.remove(clientFileName)

def generate_client_hashes(basefile, clientRequest):
     tuples = os.walk(basefile) 
     for directory, _, filenames in tuples:
       clientFile = clientRequest.clientFile.add()
       clientFile.file.isDirectory = True
       clientFile.file.filename = directory
       for filename in filenames:        
          full_name = os.path.join(directory, filename)
          if not os.path.isdir(full_name):
	    clientFile = clientRequest.clientFile.add()
            clientFile.filefilename = full_name
            generate_checksum(full_name, clientFile.clientHashes)

def generate_checksum(filename, clientHashes):
    with open(filename, "rb") as fp:
        bytes = fp.read(BLOCK_SIZE)
        while bytes != "":
           clientHash = clientHashes.add()
           simpleHash = zlib.adler32(bytes) 
           clientHash.simpleBlockHash = simpleHash
           clientHash.complicatedHash = generateComplicatedHash(bytes)
           bytes = fp.read(BLOCK_SIZE) 

def generateComplicatedHash(bytes):
    sha_object = hashlib.sha1()
    complicatedHashObject = sha_object.update(bytes)
    complicatedHash = sha_object.digest()
    return complicatedHash

def file_read(filename):
  with open(filename, "rb") as fp:
    bytes = fp.read()
    return bytes

def file_write(filename, bytes):
  with open(filename, "wb") as fp:
     fp.write(bytes)

