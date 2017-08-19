import cv2
import keyboard
import numpy as np

video = cv2.VideoCapture(0)
#classificadorFace = cv2.CascadeClassifier('cascades\\Hand.Cascade.1.xml')
classificadorFace = cv2.CascadeClassifier('cascades\\sign_language-C-classifier.xml')
classificadorA = cv2.CascadeClassifier('cascades\\sign_language-A-Classifier.xml')
classificadorB = cv2.CascadeClassifier('cascades\\sign_language-B-Classifier.xml')
classificadorD = cv2.CascadeClassifier('cascades\\sign_language-D-classifier.xml')
classificadorR = cv2.CascadeClassifier('cascades\\sign_language-F-Classifier.xml')
classificadorF = cv2.CascadeClassifier('cascades\\sign_language-R-Classifier.xml')


while True:
    Na,frame= video.read()
   #print(conectado)



    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    p=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #b = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #d = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #r = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #f = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #FacesDectadas= classificadorFace.detectMultiScale(frameCinza,scaleFactor=1.13,minNeighbors=5)
    A=classificadorA.detectMultiScale(p,minSize=(20,20))
    #B = classificadorB.detectMultiScale(p, minNeighbors=5)
    #D = classificadorD.detectMultiScale(p,scaleFactor=1.08,minNeighbors=5,minSize=(50,50))
    #R = classificadorR.detectMultiScale(p, minNeighbors=5)
    #F = classificadorF.detectMultiScale(p)
    #, minSize=(20,20)
    #,minNeighbors=5,scaleFactor=1.08 alterar os valores em diferentes lugares

    for(x,y,l,a) in A:
        cv2.rectangle(frame, (x,y),(x +l, y +a), (0,0,255), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'A', (100, 400), font, 4, (255, 0, 0), 2)
        if keyboard.is_pressed('a'):
            meunome = 'A'
            arq = open("\Users\wstro\Documents\ForcaBRAS 0.1\ForcaBRAS\\teste.txt", "w")
            arq.write(meunome)
            arq.close()

    #for(w,q,u,o) in A:
        #cv2.rectangle(a, (w, q), (w + u, q + o), (0, 0, 255), 2)
       # font = cv2.FONT_HERSHEY_SIMPLEX
       # cv2.putText(frame, 'A', (100, 400), font, 4, (255, 0, 0), 2)


    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break




video.release()
cv2.destroyAllWindows()