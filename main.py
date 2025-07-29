from FR import Start_face_recognition
from EncodeGenerator import start_Face_encoding_generation
from addDataToDatabase import add_data_to_database
import firebase_admin
from firebase_admin import credentials
from mail import send_less_attendance_email
from attendance_excel import update_attendance_excel


'''cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
            "databaseURL": "https://realtimefaceattendance-aeab9-default-rtdb.firebaseio.com/"
        })'''


#add credentials to firebase





while True:

        option = input("to start face recognition Enter '1' \nto add new attendee  Enter '2' \ninput: ")

        if option == '1':
              print("starting face recognition............")
        
              Start_face_recognition()

              update_attendance_excel()

              print("thank you for using the application")
              
        
        elif option == '2':
            add_data_to_database()
            option1 = input("If you are done with saving img!! enter '3' : ")
            if option1 == '3':
             start_Face_encoding_generation()
             
             print("thank you for using the application")


        send_less_attendance_email()


    


