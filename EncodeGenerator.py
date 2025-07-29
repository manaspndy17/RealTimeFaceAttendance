def start_Face_encoding_generation():
        import cv2
        import face_recognition
        import os
        import pickle

        filepath = 'images'

        filepathlist = os.listdir(filepath)

        imglist = []
        personId=[]

        for img in filepathlist:
            imglist.append(cv2.imread(os.path.join(filepath,img)))
            personId.append(os.path.splitext(img)[0])
        print(personId)


        def findEncoding(imageslist):
            
            encodingList =[]
            
            for img in imageslist:
                
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                
                encodingList.append(encode)
                
            return encodingList

        print("encoding started.....")
        encodeListKnown = findEncoding(imglist)   
        encodeListKnownWithId = [encodeListKnown,personId] 
        print("encoding completed")


        file = open("encode.p" , "wb")

        pickle.dump(encodeListKnownWithId,file)

        file.close()

        print("file saved")


