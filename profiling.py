import cProfile
import time
import gc
import globals

print globals()

def a():
  i = i + 5

def tester():
   counter = 0
   for i in range(1000000000):
	counter = i + 1
	a()
#These profile function use exec 
#This is the recommended function
#cProfile.run("tester")

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print(endTime - startTime,'ms')
        return result
    return wrapper

# You don't want to average timing samples
# You want to take the minimum
# Theres no real variability in python time; its whether some other python code gets involved
def multiple_timers(method):
    num_samples = 1000   
    gc.disable() #disabling garbage collection
    def wrapper(*args, **kw):
        time_measurement = float("inf")
        for i in range(num_samples):
          startTime = time.time()
          result = method(*args, **kw)
          endTime = time.time()
          difference = (endTime - startTime) * 1000
	  #dont take average this wayaverage = (average * counter + difference) / (counter + 1)
	  time_measurement = min(difference, time_measurement)  
	print "time measurement", time_measurement
	return result
    return wrapper

@multiple_timers
def func1(a,b,c = 'c',sleep = 1):
    print(a,b,c)

func1(1,2,3)

