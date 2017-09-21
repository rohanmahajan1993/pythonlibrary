import hashlib
import os
import protocols_pb2
import time
import zlib

BLOCK_SIZE = 8192

"""
Wrapper for creating the complicated hash.
We choose to use sha1, but this can easily swapped out.
"""
def generateComplicatedHash(bytes):
    sha_object = hashlib.sha1()
    complicatedHashObject = sha_object.update(bytes)
    complicatedHash = sha_object.digest()
    return complicatedHash

"""
Wrapper for reading file
"""
def file_read(filename):
  with open(filename, "rb") as fp:
    bytes = fp.read()
    return bytes
"""
Wrapper for file friting
"""
def file_write(filename, bytes):
  with open(filename, "wb") as fp:
     fp.write(bytes)
