#workies!
#to change pic size revise: resized_image = cv2.resize(image, (100,100))
#will dump pics in folder: pos or neg  (these need to be manually created)
import cv2
import numpy as np
import os

#Inputs
vidCam = 0 # 0 or 1
pos_or_neg = 'pos' #'pos' or 'neg'

# Directory setup & file enumeration
curpath = os.getcwd()
if os.path.exists(os.getcwd() + "/" + pos_or_neg):
    print('path exists')
    path, dirs, files = next(os.walk(os.getcwd()+'/'+pos_or_neg))
# create pos/neg folder if not already existing
elif not os.path.exists(os.getcwd() + "/" + pos_or_neg):
    os.mkdir(os.getcwd() + "/" + pos_or_neg)
    print('Created directory: ' + os.getcwd() + '\\' + pos_or_neg)

def generate_dataset(img, id, img_id):
    #image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = img

    path = 'pos/' if pos_or_neg == 'pos' else 'neg/'
    outfile = 'pos.txt' if pos_or_neg == 'pos' else 'bg.txt'
	
    # image = cv2.resize(image, (128,96))
    cv2.imwrite(path+str(img_id)+'.jpg', image)
    f = open(path + outfile, "a")
    f.write(path + str(img_id) +'.jpg 1 0 0 w h' + "\n")
    f.close()
	
	
    # # uncomment to take neg pics
    # image = cv2.resize(image, (128,96))
    # cv2.imwrite('neg/'+str(img_id)+'.jpg', image)
    # f = open("neg/bg.txt", "a")
    # f.write('neg/' + str(img_id) + '.jpg' + '\n')
    # f.close()
    
    # # uncomment to take positive pics
    # # image = cv2.resize(image, (128,96))
    # cv2.imwrite('pos/'+str(img_id)+'.jpg', image)
    # f = open("pos/pos.txt", "a")
    # f.write('pos/' + str(img_id) +'.jpg 1 0 0 w h' + "\n")
    # f.close()
    print('file num saved:'+str(img_id))

video_capture = cv2.VideoCapture(vidCam)

#initialize variables to use for pic filenaming
img_id = 0
user_id = 1

while True:
    ret, img = video_capture.read()
    cv2.imshow('img', img)
    img_id += 1
    generate_dataset(img, user_id, img_id)
    #terminate when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()
