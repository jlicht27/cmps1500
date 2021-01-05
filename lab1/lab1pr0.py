'''This program converts any amount of seconds into
hours, minutes, and seconds'''

time = int(input('Please enter the number of seconds: '))
seconds = time % 60
time = time//60
minutes = time % 60
hours = time//60

result = ''

if hours > 0:
    if hours == 1:
        result = result + str(hours) + ' hour'
    else: result = result + str(hours) + ' hours'

if minutes > 0:
    if hours > 0:
        if minutes == 1:
            result = result + ' ' + str(minutes) + ' minute'
        else:
            result = result + ' ' + str(minutes) + ' minutes'
    else:
        if minutes == 1:
            result = result + str(minutes) + ' minute'
        else:
            result = result + str(minutes) + ' minutes'

if seconds > 0:
    if minutes or hours > 0:
        if seconds == 1:
            result = result + ' ' + str(seconds) + ' second'
        else:
            result = result + ' ' + str(seconds) + ' seconds'
    else:
        if seconds == 1:
            result = result + str(seconds) + ' second'
        else:
            result = result + str(seconds) + ' seconds'

print(result)
