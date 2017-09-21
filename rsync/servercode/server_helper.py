import file_reader
import protocols_pb2

import hashlib
import os
import time
import zlib

"""
This library handles most of the core logic for the rsync server.
"""

"""
This library is responsible for creating the edited and deleted files.
If a file is found in the client and not in the server, we assume that
the file has to be deleted. If a file is found in both, we analyze it to be deleted.
Some tricky situations involve a directory being deleted and new a file with the same being
created and vice-versa.
"""
def analyze_client_files(timestamp, clientFiles, deletedFiles, editedFiles):
    clientFileNames = dict()
    for clientFile in clientFiles:
        filename = clientFile.file.filename
        clientFileNames[filename] = clientFile.file.isDirectory
        if os.path.exists(filename) and os.path.isdir(
                filename) == clientFile.file.isDirectory:
            print "the filename is", filename
            last_modified_time = os.path.getmtime(filename)
            if last_modified_time > timestamp and not clientFile.file.isDirectory:
                analyze_client_file(clientFile, editedFiles)
        else:
            deleted_file = deletedFiles.add()
            deleted_file.isDirectory = clientFile.file.isDirectory
            deleted_file.filename = filename
    return clientFileNames

"""
This method is used to create a hash map
which maps the clientSimpleHashes to their block number and complicatedHash.
This format is used to generate the diffs between files.
"""

def create_client_hashmap(clientFile):
    clientHashMap = dict()
    blockNumber = 0
    for clientHash in clientFile.clientHashes:
        hashList = clientHashMap.get(clientHash.simpleHash, [])
        hashList.append((blockNumber, clientHash.complicatedHash))
        blockNumber += 1
    return clientHashMap

"""
This method first allows an easy method to create the editedFile protobuf.
Protobufs can't be passed parameters in their creation, so this helps reduce
verbosity. Additionally, this method adds a check to creat and editedFile if it 
is not created before. This awkard structure is to ensure we don't have editedFiles,
which consist of zero changes.
"""

def fileEditHelper(editedFiles,
                   fileEdits,
                   isBlockNumber,
                   fileName,
                   blockNumber=0,
                   fileContent="",
                   numBlocks=0):
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

"""
This method is responsible for creating the diff between the clientFile and 
the serverFile. We use the same algorithm that rysnc uses. We first compare the
simple checksum and see if matches. We then see if a more complicated checksum matches.
We assume that if two complicated checksums match, the blocks are equivalent.
We try to ensure conesecutive changes of the same kind are grouped together in the fileEdit structure.
For instance, instead of having two fileEdits that both contain raw bytes, we instead one raw byte structure.
"""
def analyze_client_file(clientFile, editedFiles):
    fileEdits = None
    clientHashMap = create_client_hashmap(clientFile)
    print clientFile.file.filename
    with open(clientFile.file.filename, "rb") as fp:
        new_bytes = fp.read(file_reader.BLOCK_SIZE)
        current_bytes = ""
        numBlocks = 0
        previousBlock = -5
        while new_bytes != "":
            simpleHash = zlib.adler32(new_bytes)
            foundBlockMatch = False
            if simpleHash in clientHashMap:
                complicatedServerHash = file_reader.generateComplicatedHash(
                    bytes)
                hashList = clientHashMap[simpleHash]
                for blockNumber, complicatedHash in hashList:
                    if complicatedHash == complicatedServerHash:
                        foundBlockMatch = True
                        new_bytes = fp.read(file_reader.BLOCK_SIZE)
                        if numBlocks == 0 and current_bytes != "":
                            fileEdits = fileEditHelper(
                                editedFiles,
                                fileEdits,
                                clientFile.file.fileName,
                                False,
                                fileContent=current_bytes)
                            current_bytes = ""
                        elif blockNumber - numBlocks == previousBlock:
                            numBlocks += 1
                        else:
                            fileEdits = fileEditHelper(
                                editedFiles,
                                fileEdits,
                                clientFile.file.fileName,
                                True,
                                blockNumber=previousBlock,
                                numBlocks=numBlocks)
                            numBlocks = 1
                            previousBlock = blockNumber
            if not foundBlockMatch:
                if numBlocks != 0:
                    fileEdits = fileEditHelper(
                        editedFiles,
                        fileEdits,
                        clientFile.file.fileName,
                        True,
                        blockNumber=previousBlock,
                        numBlocks=numBlocks)
                    numBlocks = 0
                    current_bytes += new_bytes[0]
                new_bytes = new_bytes[1:] + fp.read(1)
        if numBlocks != 0:
            fileEdits = fileEditHelper(
                editedFiles,
                fileEdits,
                clientFile.file.fileName,
                True,
                blockNumber=previousBlock,
                numBlocks=numBlocks)
        elif current_bytes != "":
            fileEdits = fileEditHelper(
                editedFiles,
                fileEdits,
                clientFile.file.fileName,
                False,
                fileContent=current_bytes)
"""
This method find all the new files, files that exist on the server
but not on the client. Once again this is made tricky by cases such
as deleting a directory and creating a file with the same name.
"""
def find_new_files(basefile, clientFileNames, new_files):
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

"""
This is the root parent method and is responsible for finding all the edited, deleted, and new files.
"""
def process_server_directory(clientRequest):
    serverResponse = protocols_pb2.ServerResponse()
    serverResponse.timestamp = time.time()
    clientFileNames = analyze_client_files(
        clientRequest.timestamp, clientRequest.clientFiles,
        serverResponse.deletedFiles, serverResponse.editedFiles)
    find_new_files(clientRequest.directoryName, clientFileNames,
                         serverResponse.newFiles)
    return serverResponse
