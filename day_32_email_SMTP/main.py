import smtplib

my_email = 'nyelrugosibakugan@gmail.com'
my_password = 'macskafasza'


# connection = smtplib.SMTP('smtp.gmail.com')
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs='huba0ferencz@gmail.com',
#                     msg='Subject:szewasz bazmeg\n\nkutyaidat setaltatod?')
# connection.close()
# alternative below

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs='huba0ferencz@gmail.com',
                        msg='Subject:szewasz bazmeg\n\nkutyaidat setaltatod?')
