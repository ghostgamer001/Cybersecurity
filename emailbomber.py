import smtplib

mail = smtplib.SMTP("smtp.gmail.com",25)

mail.starttls()

mail.login(abc@gmail.com,password)

message = "Hi "

mail.sendmail("abc@gmail.com","xyz@gmail.com",message)

mail.quit()