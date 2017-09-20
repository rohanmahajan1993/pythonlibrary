import file_reader
import os
import protocols_pb2
import zlib

def generate_checksum(filename, clientHashes):
    with open(filename, "rb") as fp:
        bytes = fp.read(file_reader.BLOCK_SIZE)
        while bytes != "":
           clientHash = clientHashes.add()
           simpleHash = zlib.adler32(bytes) 
           clientHash.simpleHash = simpleHash
           clientHash.complicatedHash = file_reader.generateComplicatedHash(bytes)
           bytes = fp.read(file_reader.BLOCK_SIZE) 

def generate_client_hashes(basefile, clientRequest):
     print "the basefile is", basefile
     tuples = os.walk(basefile) 
     for directory, _, filenames in tuples:
       clientFile = clientRequest.clientFiles.add()
       clientFile.file.isDirectory = True
       clientFile.file.filename = directory
       print "key values", directory
       for filename in filenames:        
          full_name = os.path.join(directory, filename)
          print "key values", full_name
          if not os.path.isdir(full_name):
	    clientFile = clientRequest.clientFiles.add()
            clientFile.file.filename = full_name
            generate_checksum(full_name, clientFile.clientHashes)

def process_client_directory(ServerResponse):
    handle_deleted_files(ServerResponse.deletedFiles)
    handle_new_files(ServerResponse.newFiles)
    handle_edited_files(ServerResponse.editedFiles)

def handle_new_files(new_files):
   for newFile in new_files:
         filename = newFile.file.filename
         print "the new filenames", filename
         if newFile.file.isDirectory:
	      os.mkdir(filename)
         else:
              file_reader.file_write(filename, newFile.fileContent)

def handle_deleted_files(deletedFiles):
    for deletedFile in deletedFiles:
        clientFileName = deletedFile.filename
        print "the deleted fileNames", clientFileName
        if deletedFile.isDirectory: 
            os.rmdir(clientFileName)
        else:
            os.remove(clientFileName)

def handle_edited_files(editedFiles):
    for editedFile in editedFiles:
        filename = editedFile.filename
        print "the editedfilename", filename
        with open("temp.txt", "wb") as newFile:
            with open(filename, "rb") as oldFile:
                for fileEdit in editedFile.fileEdits:
                    if fileEdit.isBlockNumber:
                         oldFile.seek(fileEdit.blockNumber)
                         bytes = oldFile.read(file_reader.BLOCK_SIZE * fileEdit.numBlocks)
                    else:
                         bytes = fileEdit.fileContent
                    newFile.write(bytes)

