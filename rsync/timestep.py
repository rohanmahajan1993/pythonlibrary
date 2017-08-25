import os
import datetime
def modification_date(filename):
    t = os.path.getmtime(filename)
    print "the timestep is", type(t)
    return datetime.datetime.fromtimestamp(t)

