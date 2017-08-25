import os
import datetime

def modification_date(filename):
    t = os.path.getmtime(filename)
    print t
modification_date("sampledir")
