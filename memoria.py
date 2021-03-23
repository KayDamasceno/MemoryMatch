from ppadb.client import Client
from mss import mss
import numpy as np
import time
from PIL import Image
import cv2
import matplotlib.colors as colors
import imagehash
from random import randrange, choice

###5x4
adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices)==0:
    print('No device attached')
    quit()

dev = devices[0]
print("Start playing")
def matchImage(img1, img2):
    
    hash0 = imagehash.average_hash(img1)
    hash1 = imagehash.average_hash(img2)

    cutoff = 10
    print(hash0-hash1)
    if hash0 - hash1 < cutoff:
        print("Matched")
        return True
    else:
        print("Not Matched")
        return False

def matchImageCV(img1, img2):
    sift = cv2.SIFT_create()
    

    kp_1, desc_1 = sift.detectAndCompute(img1, None)
    kp_2, desc_2 = sift.detectAndCompute(img2, None)

    index_params = dict(algorithm = 0, trees = 5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(desc_1, desc_2, k = 2)

    good_points =[]

    for m, n in matches:
        if m.distance <= 0.6*n.distance:
            good_points.append(m)

    number_keypoints = 0

    if len(kp_1) <= len(kp_2):
        number_keypoints = len(kp_1)
    else:
        number_keypoints = len(kp_2)
    if len(good_points)!=0:
        
        if int(len(kp_1)/len(good_points)) <=3:
            print("Similarity %s"%(len(kp_1)/len(good_points)))
            return True
            

    return False
table = 20*[0]



#print(table)
cordxy = []
card = []
sct = mss()
#1
cordxy.append((99,296))
card.append({'left':274, 'top':163, 'width':88, 'height':121})
#2
cordxy.append((259,296))
card.append({'left':380, 'top':163, 'width':88, 'height':121})
#3
cordxy.append((419,296))
card.append({'left':486, 'top':163, 'width':88, 'height':121})
#4
cordxy.append((579,296))
card.append({'left':592, 'top':163, 'width':88, 'height':121})
#5
cordxy.append((99,584))
card.append({'left':274, 'top':325, 'width':88, 'height':121})
#6
cordxy.append((259,584))
card.append({'left':380, 'top':325, 'width':88, 'height':121})
#7
cordxy.append((419,584))
card.append({'left':486, 'top':325, 'width':88, 'height':121})
#8
cordxy.append((579,584))
card.append({'left':592, 'top':325, 'width':88, 'height':121})
#9
cordxy.append((99,872))
card.append({'left':274, 'top':487, 'width':88, 'height':121})
#10
cordxy.append((259,872))
card.append({'left':380, 'top':487, 'width':88, 'height':121})
#11
cordxy.append((419,872))
card.append({'left':486, 'top':487, 'width':88, 'height':121})
#12
cordxy.append((579,872))
card.append({'left':592, 'top':487, 'width':88, 'height':121})
#13
cordxy.append((99,1160))
card.append({'left':274, 'top':649, 'width':88, 'height':121})
#14
cordxy.append((259,1160))
card.append({'left':380, 'top':649, 'width':88, 'height':121})
#15
cordxy.append((419,1160))
card.append({'left':486, 'top':649, 'width':88, 'height':121})
#16
cordxy.append((579,1160))
card.append({'left':592, 'top':649, 'width':88, 'height':121})
#17
cordxy.append((99,1448))
card.append({'left':274, 'top':811, 'width':88, 'height':121})
#18
cordxy.append((259,1448))
card.append({'left':380, 'top':811, 'width':88, 'height':121})
#19
cordxy.append((419,1448))
card.append({'left':486, 'top':811, 'width':88, 'height':121})
#20
cordxy.append((579,1448))
card.append({'left':592, 'top':811, 'width':88, 'height':121})


choose = []
"""
while True:

    x = choice([i for i in range(16) if i not in choose])
    
    dev.shell('input tap %s %s'%(cordxy[x][0], cordxy[x][1]))
    time.sleep(0.2)
    img1 = sct.grab(card[x])
    img1 = Image.frombytes("RGB", img1.size, img1.bgra, "raw", "BGRX")
    table.insert(x,img1)
    flag = False
    for i in range(16):
        if table[i]!=0 and i!=x:
            if matchImage(img1, table[i]):
                print("Entrei")
                print(x, i)
                dev.shell('input tap %s %s'%(cordxy[i][0], cordxy[i][1]))
                flag = True
                choose.append(i)
                choose.append(x)
    print(table)
    if not flag:
        dev.shell('input tap %s %s'%(cordxy[0][0], cordxy[0][1]))
    


    print(x)


"""
for x in range(20):
    dev.shell('input tap %s %s'%(cordxy[x][0], cordxy[x][1]))
    time.sleep(0.2)
    img1 = sct.grab(card[x])
    img1 = Image.frombytes("RGB", img1.size, img1.bgra, "raw", "BGRX")
   # img1 = img1.save("card%s.jpg"%(x))
    table.insert(x,img1)


for i in range(20):
    time.sleep(0.2)
    for j in range(20):
        if i!=j:
            #print(i, j)
            time.sleep(0.2)
            if matchImageCV(np.array(table[i]), np.array(table[j])):
                time.sleep(1)
                
                dev.shell('input tap %s %s'%(cordxy[i][0], cordxy[i][1]))
                time.sleep(1)
                dev.shell('input tap %s %s'%(cordxy[j][0], cordxy[j][1]))
                break
"""
dev.shell('input tap %s %s'%(xySndCard[0], xySndCard[1]))
time.sleep(0.2)
img2 = sct.grab(scndCard)
img2 = Image.frombytes("RGB", img2.size, img2.bgra, "raw", "BGRX")


dev.shell('input tap %s %s'%(xyThrCard[0], xyThrCard[1]))
time.sleep(0.2)
img3 = sct.grab(thirdCard)
img3 = Image.frombytes("RGB", img3.size, img3.bgra, "raw", "BGRX")

dev.shell('input tap %s %s'%(xyfthCard[0], xyfthCard[1]))
time.sleep(0.2)
img4 = sct.grab(fourthCard)
img4 = Image.frombytes("RGB", img4.size, img4.bgra, "raw", "BGRX")

dev.shell('input tap %s %s'%(xy5Card[0], xy5Card[1]))
img5 = sct.grab(cncCard)
img5 = Image.frombytes("RGB", img5.size, img5.bgra, "raw", "BGRX")

dev.shell('input tap %s %s'%(xy6Card[0], xy6Card[1]))
time.sleep(0.2)
img6 = sct.grab(sexCard)
img6 = Image.frombytes("RGB", img6.size, img6.bgra, "raw", "BGRX")

dev.shell('input tap %s %s'%(xy7Card[0], xy7Card[1]))
time.sleep(0.2)
img7 = sct.grab(setCard)
img7 = Image.frombytes("RGB", img7.size, img7.bgra, "raw", "BGRX")

dev.shell('input tap %s %s'%(xy8Card[0], xy8Card[1]))
time.sleep(0.2)
img8 = sct.grab(oitoCard)
img8 = Image.frombytes("RGB", img8.size, img8.bgra, "raw", "BGRX")


matchImage(img2,img2)
matchImage(img2,img3)
matchImage(img2,img4)
matchImage(img2,img5)
matchImage(img2,img6)
matchImage(img2,img7)
matchImage(img2,img8)
img2.show()
img7.show()
"""
