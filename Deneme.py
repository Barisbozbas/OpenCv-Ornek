import os
from re import S
import cv2
import glob
import numpy as np
from moviepy.editor import *
import time
import pickle

def video_olustur(folders):
    #Amacım .mp4 formatından biten videoların tespiti ve bunların  jpg formatına çevirerek 
    # (1920,1080) ve 5 fps formatlarında output videosu oluşturmak. 
  videonames_list = []
  for folder in folders:
    for f in glob.glob(folder+'/*.mp4'):
      videonames_list.append(f)
      print(f)

  print('There are {} videos in Folder'.format(len(videonames_list)))

  count = 0
  for i in range(0,len(videonames_list)):
   video_data = videonames_list[i]
   video = cv2.VideoCapture(video_data)
   success = True
   while success:
    success,image = video.read()
    name = 'C:/Users/DELL/Desktop/Ornek/Resim/'+str(count)+'.jpg'
    if success == True:
      cv2.imwrite(name,image)
      print('Frame {} Extracted Successfully'.format(count))
      count+=1
    else:
      i = i+1  
    i = i+1
  print('\n\n\nVideo {} Extracted Successfully\n\n\n'.format(video_data)) 


  image_folder = 'Resim'
  video_name = 'video.avi'

  images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
  frame = cv2.imread(os.path.join(image_folder, images[0]))
#   height, width, layers = frame.shape

#Video oluşturuyoruz
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  video=cv2.VideoWriter('output6.avi',fourcc, 5, (1920,1080))

  for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))
  return video

if __name__ == "__main__":
   
    yol=glob.glob('C:/Users/DELL/Desktop/Ornek')
    folder=video_olustur(yol)
    time.sleep(10)
    cap = cv2.VideoCapture('C:/Users/DELL/Desktop/Ornek/output6.avi')  # 0 olarak değiştirildi
    frame=[]
    color2=[]
    my_dict=dict()
   
    #number of frames 670
    for frame_indx in range(670) :
      while (cap.isOpened()):
       ret, frame = cap.read()
       if ret==True:
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape

        cx = int(width / 2)
        cy = int(height / 2)

     # Pick pixel value
        pixel_center = hsv_frame[cy, cx]
        hue_value = pixel_center[0]
    
   
        i=0
        color = "Undefined"
        if hue_value < 5:
          color = "KIRMIZI"
          color2.append(color)

        elif hue_value < 78:
          color = "YEŞİL"
          #print('Yeşil')
          color2.append(color)
       
        elif hue_value < 131:
           color = "MAVi"
           color2.append(color)  
        
        else:
           color = "KIRMIZI"
          # print('Kırnızı')
   
      
    # print(color2)
    
        # pixel_center_bgr = frame[cy, cx]
        # b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

        # cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
        # cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
        # cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
          break
        else:
          
          break
      
#Bu kısımda color2 listesini dictionary çeviriyorum 
    for index,value in enumerate(color2):
       my_dict[index] = value
    print(my_dict)
   
    with open('renk.pickle', 'wb') as handle:
       pickle.dump(my_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('renk.pickle', 'rb') as handle:
       b = pickle.load(handle)

    print(my_dict == b)
    cap.release()
# video.release()
    cv2.destroyAllWindows()
    

