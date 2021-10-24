# import smtplib
#
# my_email = 'nyelrugosibakugan@gmail.com'
# my_password = 'macskafasza'
#
#
# # connection = smtplib.SMTP('smtp.gmail.com')
# # connection.starttls()
# # connection.login(user=my_email, password=my_password)
# # connection.sendmail(from_addr=my_email,
# #                     to_addrs='huba0ferencz@gmail.com',
# #                     msg='Subject:szewasz bazmeg\n\nkutyaidat setaltatod?')
# # connection.close()
# # alternative below
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs='huba0ferencz@gmail.com',
#                         msg='Subject:szewasz bazmeg\n\nkutyaidat setaltatod?')

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=2004, month=12, day=20)

print(date_of_birth)
print(date_of_birth)
print(date_of_birth)
print(date_of_birth)