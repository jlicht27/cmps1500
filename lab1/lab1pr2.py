initial_date = str(input('Please enter date in MM/DD/YYYY format: '))

if initial_date[5] != '/': #if days or months is messed up
    if initial_date[2] != '/': #if months is 1
        month = initial_date[0:1]
        month = '0' + month
        if initial_date[4] != '/': #if months is 1 and day is 1
            day = initial_date[2:3]
            day = '0' + day
            year = initial_date[4:8]
        else: #                     if months is 1 and days is 2 
            day = initial_date[2:4]
            year = initial_date[5:9]
    else: #                         if months is 2
        month = initial_date[0:2]
        if initial_date[5] != '/': # if months is 2 and days is 1
            day = initial_date[3:4]
            day = '0' + day
            year = initial_date[5:9]
        else: #                         if months is 2 and days is 2
            day = initial_date[3:5]
            year = initial_date[6:10]
else:
    month = initial_date[0:2]
    day = initial_date[3:5]
    year = initial_date[6:10]

formatted_date = day + '.' + month + '.' + year

print('Here is the formatted date:', formatted_date)
