from mtcnn import MTCNN
import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
def crop_image(image_path):
    detector = MTCNN() 
    img=cv2.imread(image_path)
    data=detector.detect_faces(img)
    print(data)
    for faces in data:
        box=faces['box']            
        box[0]= 0 if box[0]<0 else box[0]
        box[1]= 0 if box[1]<0 else box[1]
        img=img[box[1]: box[1]+box[3],box[0]: box[0]+ box[2]] 
        img= cv2.resize(img, (224, 224)) 
        cv2.imwrite('m2.jpg', img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert from bgr to rgb
        
        
    return img 
image_path='r.jpg'
img=crop_image(image_path)
plt.imshow(img)