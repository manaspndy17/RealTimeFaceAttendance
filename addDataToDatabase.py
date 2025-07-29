
def add_data_to_database():

        import datetime
    
        from firebase_admin import db
        import os


        



        ref = db.reference("attendee")

        name=input("Enter name: ")
        major=input("Enter major: ")        
        call=input("Enter contact number: ")
        email=input("Enter email: ")    
        address=input("Enter address: ")


        id = "FA"+str(name[0:2].upper())+str(call[-2:])

        folder_path = os.path.abspath(f'H:\project\FaceAttendance\images')
        print(f'save attendee img in {folder_path} with name {id}.jpg')


        '''data={
        "FAMO01":{
            "name":"Naredra Modi",
            "major":"PM of India",
            "contact":{
                    "call":"0000000001",
                    "email":"CoolStuff1712@gmail.com",
                    "address":"Gujrat"
                
            },
            "starting_year":2014,
            "total_attendance":0,
            "Standing":"G",
            "year":1,
            "last_attendance_time":"2025-07-13 15:54:49",
            
            "img_url":"images/FAMO01.jpg"
            
            
        } ,
        "FAMO02":{
            "name":"ELon Musk",
            "major":"CEO of SpaceX",
            "contact":{
                    "call":"0000000002",
                    "email":"CoolStuff1712@gmail.com",
                    "address":"US"
            
            },
            "starting_year":2020,
            "total_attendance":0,
            "Standing":"G",
            "year":1,
            "last_attendance_time":"2025-07-13 15:54:49",
            
            "img_url":"images/FAEL02.jpg"
            
            
        } ,"FAVI03":{
            "name":"Virat Kohli",
            "major":"Cricketer",
            "contact":{
                    "call":"0000000003",
                    "email":"CoolStuff1712@gmail.com",
                    "address":"Delhi"
                
            },
            "starting_year":2025,
            "total_attendance":0,
            "Standing":"G",
            "year":1,
            "last_attendance_time":"2025-07-13 15:54:49",
            
            "img_url":"images/FAVI03.jpg"
            
            
        } 
        }'''
        data={id:{
            "name":name,
            "major":major,
            "contact":{
                    "call":call,
                    "email":email,
                    "address":address
                
            },
            "starting_year":int(datetime.datetime.now().year),
            "total_attendance":0,
            "Standing":"NA",
            "year":0,
            "last_attendance_time":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            
            "img_url":f'images/{id}.jpg'
            
            
        }}
        for key,value in data.items():
            ref.child(key).set(value)
        print("Data added successfully!")



