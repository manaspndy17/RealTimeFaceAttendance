
def Start_face_recognition():
      import cv2
      import os
      import pickle
      import face_recognition
      import numpy as np
      import cvzone
      import datetime
      import keyboard

      

      
      from firebase_admin import db

    

   

      cap = cv2.VideoCapture(0)


      imgBackground = cv2.imread('resources\\Background.png')

      foldermodepath = 'resources\\modes'


      modepathlist = os.listdir(foldermodepath)

      imgmodelist =[]

      for path in modepathlist:
          
          imgmodelist.append(cv2.imread(os.path.join(foldermodepath,path)))
          
          
          
          


      file = open("encode.p","rb")
      encodeListKnownWithId = pickle.load(file)
      file.close
      encodeListKnown,personId = encodeListKnownWithId






      count = 0

      
      while (1) :
          
          
          
          key = cv2.waitKey(1) & 0xFF
          if key == 27:  # ESC key
            print("ESC key pressed. Returning to main menu...")
            cap.release()
            cv2.destroyAllWindows()
            return
          
          
          success , img = cap.read()
          
          
          imgs = cv2.resize(img,(0,0),None,0.25,0.25)
          imgs = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
          
          faceCurr = face_recognition.face_locations(imgs)
          faceEncode = face_recognition.face_encodings(imgs,faceCurr)
        
          
          imgResized = cv2.resize(img, (460, 370))
          
          imgBackground[145:145+370 , 58:58+460]=imgResized
          imgBackground[0:0+556, 576:576+375 ]=imgmodelist[0]
          
          
          for encodeface , faceLoc in zip(faceEncode , faceCurr):
              
              matches = face_recognition.compare_faces(encodeListKnown , encodeface )
              faceDIst = face_recognition.face_distance(encodeListKnown , encodeface)
              
              imgIndex = np.argmin(faceDIst)
              matchFoundId = personId[imgIndex]
              if(matches[imgIndex]):
                  
                  
              
                  
                
                
                y1,x2,y2,x1 = faceLoc
                if x1-25 > 58 and y1+80>145 and x1-25<(515-(x2-x1)) and y1+80<(518-(y2-y1)):
                
                
                
                    bbox =  x1-25, y1+80, x2-x1, y2-y1
                
                
                
                  
                    imgBackground = cvzone.cornerRect(imgBackground,bbox,rt=0 )
                  
                
                attendee_id = personId[imgIndex]
                
                
                #updating the attendance number and date time
                
                if count ==0 :
                  detail = db.reference(f'attendee/{attendee_id}').get()
                  ref = db.reference(f'attendee/{attendee_id}')
                  
                  
                  
        
                  
                  last_attendance = datetime.datetime.strptime(detail['last_attendance_time'], ("%Y-%m-%d %H:%M:%S"))
                  
                  seconds=(datetime.datetime.now()-last_attendance).total_seconds()
                  
                  
                    
                  
                  if seconds>86400:
                      
                    if int(datetime.datetime.now().strftime('%d'))==1:
                      detail['total_attendance'] = 0
                      ref.child('total_attendance').set(detail['total_attendance'])  
                    
                      
                  

                  
                  
                
                  
                count+=1
                  
                  
                
                if count<=5:
                    
                
                    
                  imgBackground[0:0+556, 576:576+375 ]=imgmodelist[1]
                  
                
                  
                  attendee_image= cv2.imread(detail['img_url'])
                
                
                  cv2.putText(imgBackground,str(detail['total_attendance']),(650,79),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                  cv2.putText(imgBackground,str(detail['name']),(690,337),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)
                  cv2.putText(imgBackground,str(detail['major']),(710,387),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)

                  date_now = int(datetime.datetime.now().strftime("%d"))

                  attendance_percentage = (detail['total_attendance']*100)/date_now
                  
                  
                  if (attendance_percentage>75.0):

                    detail['Standing']='G'
                    ref.child('Standing').set(detail['Standing'])
                  else:
                    detail['Standing']='B'
                    ref.child('Standing').set(detail['Standing'])
                  
                  cv2.putText(imgBackground,str(detail['Standing']),(690,490),cv2.FONT_HERSHEY_SIMPLEX,0.5,(100,180,100),2)

                  
                  year =  int(datetime.datetime.now().strftime("%Y")) - detail['starting_year'] 
                  detail['year'] = year 
                  ref.child('year').set(year)

                  cv2.putText(imgBackground,str(year),(780,487),cv2.FONT_HERSHEY_SIMPLEX,0.5,(100,180,100),2)
                  cv2.putText(imgBackground,str(detail['starting_year']),(865,487),cv2.FONT_HERSHEY_SIMPLEX,0.5,(100,180,100),2)
                  imgBackground[134:134+131 , 682:682+154 ]= attendee_image
                
            
                if count>5 and count <11:
                    
                    if seconds<86400:
                      imgBackground[0:0+556, 576:576+375 ]=imgmodelist[3]
                    else:
                      imgBackground[0:0+556, 576:576+375 ]=imgmodelist[2]
                      if count==6:
                        detail['total_attendance']+=1   
                        ref.child('total_attendance').set(detail['total_attendance'])
                        currTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        detail['last_attendance_time']=currTime
                         
                        ref.child('last_attendance_time').set(detail['last_attendance_time'])

                    
                    
                if count==11:
                    count = 0
                    
                    
              
          
              break


          
          cv2.imshow("face attendance", imgBackground)
          key = cv2.waitKey(1) & 0xFF
          if key == 27:  # ESC key
            print("ESC key pressed. Returning to main menu...")
            cap.release()
            cv2.destroyAllWindows()
            return