from datetime import datetime
import pandas
from random import choice
import smtplib

my_email = 'name@mail.com'
passw = '123456'

today = datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv('data.csv')
# print(data)
new_dict={(data_row['month'],data_row['day']):data_row for (index,data_row) in data.iterrows()}
if today_tuple in new_dict:
    birthday_person = new_dict[today_tuple]
    # print(birthday_person)
    letters = ['letter01.text', 'letter02.text', 'letter03.text']
    final_letter = choice(letters)
    with open(final_letter) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]',birthday_person['name'])
    
