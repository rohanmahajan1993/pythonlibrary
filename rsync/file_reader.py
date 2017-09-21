import hashlib
import os
import protocols_pb2
import time
import zlib

BLOCK_SIZE = 5

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
Wrapper for file reading
"""
def file_read(filename):
  with open(filename, "rb") as fp:
    bytes = fp.read()
    return bytes
"""
Wrapper for file writing
"""
def file_write(filename, bytes):
  with open(filename, "wb") as fp:
     fp.write(bytes)
