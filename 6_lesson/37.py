time=input('Please enter your time:')
time_list = (time.split(':'))

am_pm = 'AM'
english_time = time_list[0]

if int(time_list[0]) > 12:
    english_time = int(time_list[0]) % 12
    am_pm = 'PM'

print ('Converted to English: ',str(english_time)+' : '+time_list[1], am_pm )
