import hashlib
import os
import protocols_pb2
import time
import zlib

BLOCK_SIZE = 8192
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

