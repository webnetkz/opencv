import cv2
import numpy as np

pathImg = "./monitor-1.png"
nameImgSave = 'grayUdv.png'

cap = cv2.VideoCapture(pathImg)

def loading_displaying_saving(pathImg, nameImgSave):
    img = cv2.imread(pathImg, cv2.IMREAD_GRAYSCALE) # Конвертирует изображение в оттенки серого ... cv2.IMREAD_COLOR - в RBG палитре

    cv2.imshow(pathImg, img) # Отображение изображения
    cv2.waitKey(0) # Держит открытым изображение до нажатия клавиши
    cv2.imwrite('./imgs/'+nameImgSave, img) # Сохраняем файл
    return img


def accessing_and_manipulating(img):
    print("Высота:"+str(img.shape[0]))
    print("Ширина:" + str(img.shape[1]))
    #print("Количество каналов:" + str(img.shape[2]))
    (b, g, r) = img[0, 0]
    print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))
    img[0, 0] = (255, 0, 0)
    (b, g, r) = img[0, 0]
    print("Красный: {}, Зелёный: {}, Синий: {}".format(r, g, b))


img = loading_displaying_saving(pathImg, nameImgSave)
accessing_and_manipulating(img)