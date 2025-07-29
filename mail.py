def send_less_attendance_email():
    import smtplib as s
    from firebase_admin import db
    import datetime

    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart


    email_detail = db.reference('Last_mail').get()
    
    email_ref = db.reference('Last_mail')

    last_attendance_time = datetime.datetime.strptime(email_detail['time'], "%Y-%m-%d %H:%M:%S") 

    seconds = (datetime.datetime.now() - last_attendance_time).total_seconds()

    if seconds > 432000:  # 5 days in seconds
            print("Sending attendance alert emails...")
    
    
            server = s.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("CoolStuff1712@gmail.com","vtqo rify nsxc psti")

            detail = db.reference('attendee').get()
            ref = db.reference('attendee')

            for attendee_id, data in detail.items():
                name = data['name']
                
                
                date_now = int(datetime.datetime.now().strftime("%d"))

                attendance_percentage = (data['total_attendance']*100)/date_now
                
                
                # Check if attendance percentage is below threshold
                if attendance_percentage < 75.0:

                    msg = MIMEMultipart()

                    msg['Subject'] = "Attendance Alert"


                    body = f"Dear {name},\n\nYour attendance percentage is {attendance_percentage:.2f}% which is below 75%.\nPlease ensure to attend classes regularly.\n\nBest regards,\nAttendance System"

                    msg.attach(MIMEText(body, 'plain'))
                
                    server.sendmail("CoolStuff1712@gmail.com", data['contact']['email'], msg.as_string())
            
    
     
   
            last_mail_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            email_ref.child('time').set(last_mail_time)
            server.quit()    
            print("Attendance alert emails sent successfully.")