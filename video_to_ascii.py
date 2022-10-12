import cv2
import sys
import numpy as np

#The Coding Train youtube kanalında js kodunun pythona uyarlanması
#kaynak video: https://www.youtube.com/watch?v=55iwMYv8tGI
#Katkılarından ve yardımlarından dolayı Teşekkürler Samed; https://github.com/SamedZirhlioglu

#webcamden gelen görüntünün dönüştürüleceği karakterler

#density = '▓▒░█▄:.        '[::-1]
density = "Ñ@#W$9876543210?!abc;:+=-,._"
#density = '       .:-i|=+%O#@'
#density = '        .:░▒▓█'

#density dizisinin indexlenmesi
def indexer(index):
    new = int(round(index / len(density), 0))
    if new < 0:
        new = 0
    elif len(density) <= new:
        new = len(density) - 1
    
    return density[new]

#kamera-görüntü kontrolü 0-1-2-3... tercih edilebilir
capture = cv2.VideoCapture(3)
if not capture.isOpened():
    raise IOError("Cannot open webcam")

#görüntünün dönüştürülmesi
#visiual studio code terminal çözünürlüğü için 18x18 seçildi, ekran 1080p
while True:
    ret, frame = capture.read()
    cv2.imshow('WebCam', frame)
    frame = cv2.resize(frame, (18,18),fx=0, fy=0,interpolation=cv2.INTER_CUBIC)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    ravel = gray.ravel()
    ravel = np.resize(ravel, (1, 324))[0]

    #tek boyutlu dizinin density ile karşılaştırılması indexlenmesi
    #bu dizinin densitye dönüştürülmesi
    oneDimension = [indexer(val) for val in ravel]
    oneDimension = np.resize(oneDimension, (18,18))

    #parantezilerin ve boşlukların kaldırılması
    print(str(oneDimension).replace('[', '').replace(']', '').replace('\n ', '\n').replace('\'', ''))
    
    #asci kodu ile ekrana sürekli print etme
    sys.stdout.write("\033[18F")
    
    #döngünün durdurulması ctrl+c de kullanılabilir
    c = cv2.waitKey(1)
    if c == 27:
        break
capture.release()
cv2.destroyAllWindows()
