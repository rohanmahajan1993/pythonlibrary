import hashlib
import os
import protocols_pb2
import time
import zlib
import file_reader

BLOCK_SIZE = 8192

# Will see if files still exists and need to be deleted
# Find out addition of 
def analyze_client_files(timestamp, clientFiles, deletedFiles, editedFiles):
    clientFileNames = dict()
    for clientFile in clientFiles:
        filename = clientFile.file.filename
        clientFileNames[filename] = clientFile.file.isDirectory
        if os.path.exists(filename) and os.path.isdir(filename) == clientFile.file.isDirectory:
           print "the filename is", filename
           last_modified_time = os.path.getmtime(filename)  
           if last_modified_time > timestamp and not clientFile.file.isDirectory:
               editedFile = editedFiles.add()
               editedFile.filename = filename
               analyze_client_file(clientFile, editedFile.fileEdits)
        else:
            deleted_file = deletedFiles.add()
            deleted_file.isDirectory = clientFile.file.isDirectory
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

def fileEditHelper(editedFiles, fileEdits, isBlockNumber, fileName, blockNumber=0, fileContent="", numBlocks=0):
    if fileEdits == None:
        editedFile = editedFiles.add()
        editedFile.fileName = fileName
        fileEdits = editedFile.fileEdits
    fileEdit = fileEdits.add()
    fileEdit.isBlockNumber = isBlockNumber
    if isBlockNumber:
        fileEdit.numBlocks = numBlocks
        fileEdit.blockNumber = blockNumber
    else:
        fileEdit.fileContent = fileContent
    return fileEdits

def analyze_client_file(clientFile, editedFiles):
    fileEdits = None
    clientHashMap = create_client_hashmap(clientFile)
    print clientFile.file.filename
    with open(clientFile.file.filename, "rb") as fp:
        new_bytes = fp.read(BLOCK_SIZE)
        current_bytes = ""
        numBlocks = 0
        previousBlock = -5
        while new_bytes != "":
           simpleHash = zlib.adler32(new_bytes) 
           foundBlockMatch = False
           if simpleHash in clientHashMap:
              complicatedServerHash = file_reader.generateComplicatedHash(bytes)
              hashList = clientHashMap[simpleHash]
              for blockNumber, complicatedHash in hashList:
                if complicatedHash == complicatedServerHash:
                    foundBlockMatch = True
                    new_bytes = fp.read(BLOCK_SIZE) 
                    if numBlocks == 0 and current_bytes != "":
                        fileEdits = fileEditHelper(editedFiles, fileEdits, clientFile.file.fileName, False, fileContent=current_bytes)
                        current_bytes = ""
                    elif blockNumber - numBlocks == previousBlock:
                        numBlocks += 1
                    else:
                        fileEdits = fileEditHelper(editedFiles, fileEdits, clientFile.file.fileName, True, blockNumber=previousBlock, numBlocks=numBlocks)
                        numBlocks = 1
                        previousBlock = blockNumber
           if not foundBlockMatch:
               if numBlocks != 0:
                  fileEdits = fileEditHelper(editedFiles, fileEdits, clientFile.file.fileName, True, blockNumber=previousBlock, numBlocks=numBlocks)
                  numBlocks = 0
                  current_bytes += new_bytes[0] 
               new_bytes = new_bytes[1:] + fp.read(1)
        if numBlocks != 0:
            fileEdits = fileEditHelper(editedFiles, fileEdits, clientFile.file.fileName, True, blockNumber=previousBlock, numBlocks=numBlocks)
        elif current_bytes != "":
            fileEdits = fileEditHelper(editedFiles, fileEdits, clientFile.file.fileName, False, fileContent=current_bytes)


#Have to handle weird case where file is deleted and directory is created with same name
#Just find new files
def analyze_server_files(basefile, clientFileNames, new_files):
    tuples = os.walk(basefile) 
    print clientFileNames
    for directory, _, filenames in tuples: 
       if directory not in clientFileNames or clientFileNames[directory] != True:
           new_file = new_files.add()
           new_file.file.filename = directory
           new_file.file.isDirectory = True
       for filename in filenames:        
          full_name = os.path.join(directory, filename)  
          if not os.path.isdir(full_name):
              if full_name not in clientFileNames or clientFileNames[full_name]:
                new_file = new_files.add()
                new_file.file.filename = full_name
                new_file.file.isDirectory = False
                file_content = file_reader.file_read(full_name)
                new_file.fileContent = file_content


def process_server_directory(clientRequest):
     serverResponse = protocols_pb2.ServerResponse() 
     serverResponse.timestamp = time.time()
     clientFileNames = analyze_client_files(clientRequest.timestamp, clientRequest.clientFiles, serverResponse.deletedFiles, serverResponse.editedFiles)
     analyze_server_files(clientRequest.directoryName, clientFileNames, serverResponse.newFiles)
     return serverResponse


