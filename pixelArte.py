# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

imagem = cv.imread('Fruta/fruta7.jpg')


imagem = cv.resize(imagem,(800,800))


def pixel_face(imagemParam,blocos):
    (h,w) = imagemParam.shape[:2]
    xSteps = np.linspace(0,w,blocos+1, dtype='int')
    ySteps = np.linspace(0,h,blocos+1, dtype='int')
    
    for i in range(1,len(ySteps)):
        for j in range(1,len(xSteps)):
            startX = xSteps[j - 1]
            startY = ySteps[i - 1]
            endX = xSteps[j]
            endY = ySteps[i]
    
            roi = imagemParam[startY:endY,startX:endX]
            (B,G,R) = [int(x) for x in cv.mean(roi)[:3]]
            cv.rectangle(
                imagemParam,
                (startX,startY),
                (endX,endY),
                (B,G,R),
                -1        
                )
    return imagemParam



rodape = np.full((50,800,3),(0,0,0),dtype = np.uint8)
cv.putText(rodape,'Mine Frame: Heron TF Gomes',(450,25),cv.FONT_HERSHEY_SCRIPT_SIMPLEX ,0.8,(190,190,190),1,cv.LINE_AA )
cv.putText(rodape,'13/11/2020',(690,45),cv.FONT_HERSHEY_SCRIPT_SIMPLEX ,0.5,(190,190,190),1,cv.LINE_AA )

imagemQuadro = pixel_face(imagem,90)

final = cv.vconcat([imagemQuadro,rodape])

final = cv.copyMakeBorder(final,10,10,10,10,cv.BORDER_REPLICATE)

cv.imshow('Pixel',final)
cv.waitKey()



cv.imwrite('Fruta\mineQuadroFruta7.jpg',final)

cv.destroyAllWindows()

