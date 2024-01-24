import time  #imports the time module, which provides various time-related functions.




def countdown(t) :
    while t:  #while loop that continues execution as long as t is non-zero (or truthy).
        mins, secs  = divmod(t, 60)        #divides t by 60 and returns a tuple containing the quotient and the remainder. The quotient represents the number of minutes, and the remainder represents the number of seconds.
        timer = '{:02d}:{:02d}'.format(mins, secs)   #creates a string with two digits for minutes ({:02d}) and two digits for seconds ({:02d}).
        print(timer, end='\r')   #(end='\r'). This causes the subsequent print statements to overwrite the previous output, creating a countdown effect.
        time.sleep(1)     # pauses the execution for 1 second, creating a one-second delay between each countdown update.
        t -= 1        #decrements the value of t by 1, effectively counting down

    print('Your time is up!!!')

t = input('Enter time in seconds: ')
countdown(int(t))



def timer_count(k):
    while k:
        hours, mins = divmod(k, 3600)
        mins, secs = divmod(k, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end='\r')
        time.sleep(2)
        k -=2

    print('Your timer is completed!')
k = input('Enter time in seconds: ')
timer_count(int(k))


def timer_count(mins):
    t = mins * 60
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print('Yoooh , your time is up!!')

mins = int(input('Enter time in minutes: '))
timer_count(mins)



def timer_count(hours):
    k = int(hours) * 3600  # Convert hours to seconds
    while k:
        hours, mins = divmod(k, 3600)
        mins, secs = divmod(k, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(int(hours), int(mins), int(secs))
        print(timer, end='\r')
        time.sleep(1)
        k -= 1

    print('Your timer is completed!')

hours = input('Enter time in hours: ')
timer_count(hours)


