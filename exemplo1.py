import cv2

classificadorC= cv2.CascadeClassifier('cascades\haarcascade_frontalface_default.xml')

imagem= cv2.imread('pessoas\\pessoas3.jpg')
ImagemCinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

facesDectadas = classificador.detectMultiScale(ImagemCinza, scaleFactor=1.1,minNeighbors=9,minSize=(9,10))

print(len(facesDectadas))

print(facesDectadas)

for(x,y,l, a) in facesDectadas:
    print(x,y,l,a)
    cv2.rectangle(imagem,(x,y), (x+l, y +a),(0,0,255),2 )



cv2.imshow("Faces encontradas",imagem)
cv2.waitKey()
