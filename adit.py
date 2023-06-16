import pytesseract
import cv2
import pyttsx3

#-- Set up untuk library pytessseract dan pyttsx3
#-- Start
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"
img = cv2.imread('000.jpg')
engine = pyttsx3.init()
engine.setProperty("rate", 130)  # kecepatan
engine.setProperty("volume", 1.0)  # Volume level (0.0 to 1.0)
voices = engine.getProperty('voices') #change
engine.setProperty('voice', voices[1].id) 
url = ""
#-- End

imgH, imgW, _ = img.shape

boxes = pytesseract.image_to_boxes(img)
# print(boxes)

#-- Mengambil satu per satu huruf yang nantinya akan dimasukan ke sebuah variabel
a= ""
for box in boxes.splitlines():
    box = box.split(' ')
    # print(box)
    # print(box)
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    name = box[0]
    cv2.rectangle(img, (x, imgH-y), (w, imgH-h), (100,100,255), 1)
    cv2.putText(img, name, (x, imgH-y+25), cv2.FONT_HERSHEY_PLAIN, 1, (100,100,255), 2)
    a += box[0]

#-- Menampilkan Visual dan Audio teks yang sudah di deteksi
def running():
    cv2.imshow('Netra Assist', img)
    engine.say("expired on" + a)
    engine.runAndWait()
    key = cv2.waitKey(0)

