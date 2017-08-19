import cv2

video = cv2.VideoCapture(0)
#classificadorFace = cv2.CascadeClassifier('cascades\\Hand.Cascade.1.xml')
classificadorFace = cv2.CascadeClassifier('cascades\\sign_language-C-classifier.xml')
classificadorA = cv2.CascadeClassifier('cascades\\sign_language-A-Classifier.xml')
classificadorB = cv2.CascadeClassifier('cascades\\sign_language-B-Classifier.xml')
classificadorD = cv2.CascadeClassifier('cascades\\sign_language-D-classifier.xml')
classificadorR = cv2.CascadeClassifier('cascades\\sign_language-F-Classifier.xml')
classificadorF = cv2.CascadeClassifier('cascades\\sign_language-R-Classifier.xml')


while True:
    conectado, frame= video.read()
   #print(conectado)

    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    FacesDectadas= classificadorFace.detectMultiScale(frameCinza,minSize=(20,20))
    #, minSize=(20,20)
    #,minNeighbors=5,scaleFactor=1.08 alterar os valores em diferentes lugares

    for(x,y,l,a) in FacesDectadas:
        cv2.rectangle(frame, (x,y),(x +l, y +a), (0,0,255), 2)



    if cv2.waitKey(1) == ord('q'):
        cv2.imshow('video', frame)
        meunome = "c"

        arq = open("c.txt", "w")
        arq.write(meunome)
        arq.close()
        break



video.release()
cv2.destroyAllWindows()