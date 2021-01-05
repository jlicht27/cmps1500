import time #import a module for working with time

#START THE PROGRAM
t = time.time() #read current time, in seconds since the begining of time
print(t)


t_nice = time.ctime(t) # convert time reading into human format
print(t_nice)



time.sleep(1) #pause execution for 1 second, just for the sake of example



#END THE PROGRAM
t1 = time.time() #read current time, in seconds since the begining of time
print(t1)

t1_nice = time.ctime(t1) # convert new time reading into humane format
print(t1_nice)



time_difference = t1 - t # calculate difference between starting and ending time
print("Your program ran",  time_difference, "seconds")
print("Your program ran", round(time_difference, 6), "seconds")
