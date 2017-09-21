import file_reader
import protocols_pb2

import os
import shutil

import zlib

"""
This module is responsible for the rsync client.
The first part is used to generate the client request
and the second part is to analyze the server response.
"""

#Generating Client Request

"""
This method is responsible for generating the checksums for a specific file.
"""
def generate_checksum(filename, clientHashes):
    with open(filename, "rb") as fp:
        bytes = fp.read(file_reader.BLOCK_SIZE)
        while bytes != "":
           clientHash = clientHashes.add()
           simpleHash = zlib.adler32(bytes) 
           clientHash.simpleHash = simpleHash
           clientHash.complicatedHash = file_reader.generateComplicatedHash(bytes)
           bytes = fp.read(file_reader.BLOCK_SIZE) 

"""
This method recursively goes through every file and directory and creates the checksums.
We do not create checksums for directory and just include the name.
"""
def generate_client_hashes(prefix, basefile, clientRequest):
     clientName = os.path.join(prefix, basefile)
     tuples = os.walk(clientName) 
     for directory, _, filenames in tuples:
       clientFile = clientRequest.clientFiles.add()
       clientFile.file.isDirectory = True
       clientFile.file.filename = os.path.relpath(directory, prefix)
       for filename in filenames:        
          full_name = os.path.join(directory, filename)
          if not os.path.isdir(full_name):
	    clientFile = clientRequest.clientFiles.add()
            clientFile.file.filename = os.path.relpath(full_name, prefix)
            generate_checksum(full_name, clientFile.clientHashes)

# Analyzing Server Response

"""
This method is responsible for handling the server response and using it to update the client workspace. The three components are deleting files, creating new files, and editing files.
"""

def process_client_directory(prefix, serverResponse):
    base_iterator(serverResponse.deletedFiles, simple_name_extractor, prefix, handle_deleted_file)
    base_iterator(serverResponse.newFiles, complicated_name_extractor, prefix, handle_new_file)
    base_iterator(serverResponse.editedFiles, simple_name_extractor, prefix, handle_edited_file)

"""
Method that iterates through all of the files, regardless of type, and adds
the prefix and calls the designated handler.
"""
def base_iterator(files, filenameExtractor, prefix, handler):
    for file in files:
        filename = filenameExtractor(file)
        clientname = os.path.join(prefix, filename)
        handler(clientname, file)
"""
This handler stuff is slightly unelegant because we have to have two different
name extractor. This is because editedFiles can not be a directory and for deletedFiles
we don't care if it is a directory, but for newFiles they can be a directory. The 
tradeoff was mode for logical reasoning about the types versus the inlegance of the code.

"""
def simple_name_extractor(file):
    return file.filename

def complicated_name_extractor(file):
    return file.file.filename 

"""
This method either creates new directories or new files with the appropriate content.
We don't worry about initializing the directories with the appropriate list of files
because this happends automatically when we create the files. Additionally, we don't have
to worry about any weird out of order issues based on the order we process the files on the server.
"""
def handle_new_file(filename, newFile):
    print "the new file name is", filename
    if newFile.file.isDirectory:
	os.mkdir(filename)
    else:
        file_reader.file_write(filename, newFile.fileContent)
"""
This method deletes files and directories, that were found on the client but not on the server. If we are deleting a directory, we delete everything inside of it because we do not efficiently
handle directory renames. This is also why we have the os.path.exists check in case we already
deleted a file.
"""
def handle_deleted_file(filename, deletedFile):
        if os.path.exists(filename):
            print "the deleted file name is", filename
            if deletedFile.isDirectory: 
                shutil.rmtree(filename)
            else:
                os.remove(filename)
"""
This method uses the diff to construct a new file. Because we need the oldFile,
we create a new file called temp.txt, while still using the oldFile, and once 
we're done, rename this tempfile to the appropriate fileName.
"""
def handle_edited_file(filename, editedFile):
        print "the edited filename is", filename
        with open(".TEMP", "wb") as newFile:
            with open(filename, "rb") as oldFile:
                for fileEdit in editedFile.fileEdits:
                    if fileEdit.isBlockNumber:
                         oldFile.seek(fileEdit.blockNumber)
                         bytes = oldFile.read(file_reader.BLOCK_SIZE * fileEdit.numBlocks)
                    else:
                         bytes = fileEdit.fileContent
                    newFile.write(bytes)
        os.rename(".TEMP", filename) 
