import cv2

classificador= cv2.CascadeClassifier('cascades\\haarcascade_frontalface_default.xml')
classificadorOlhos= cv2.CascadeClassifier('cascades\\haarcascade_eye.xml')

imagem = cv2.imread('pessoas\\pessoas4.jpg')
imagemCinza= cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDectadas= classificador.detectMultiScale(imagemCinza)


for (x,y,l,a) in facesDectadas:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
    regiao = imagem[y:y + a, x:x + l]
    regiaoCinzaOlho= cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
    olhosDetec= classificadorOlhos.detectMultiScale(regiaoCinzaOlho, scaleFactor=1.1, minNeighbors=10)
    print(olhosDetec)

    for( ax,ay,al, aa) in olhosDetec:
        cv2.rectangle(regiao,(ax,ay), (ax + al, al + aa), (255,0,255),2)


cv2.imshow("agoora", imagem)
cv2.waitKey()