import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

options = {
        'model': 'cfg/yolov2-tiny.cfg',
        'load': 'bin/yolov2-tiny.weights',
        'threshold': 0.5,
        'gpu': 0.65
    }

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(5)]

def yolo(frame):
    
    results = tfnet.return_predict(frame)
    for result in results:
        tl = (result['topleft']['x'], result['topleft']['y'])
        br = (result['bottomright']['x'], result['bottomright']['y'])
        label = result['label']
        confidence = result['confidence']
        text = '{}: {:.0f}%'.format(label, confidence * 100)

        if label == 'car':                                           				
            color = colors[0] 
            classType = 2

        elif label == 'truck' or  label == 'bus':    						
            color = colors[1]
            classType = 3

        elif label == 'bicycle' or  label == 'motorbike' or label == 'person':               	
            color = colors[2]
            classType = 1

        else: continue

        frame = cv2.rectangle(frame, tl, br, color, 5)
        frame = cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
    cv2.imshow('frame', frame)

capture = cv2.VideoCapture('videos/test_video/motor_s.mp4')


while True:
    stime = time.time()
    ret, frame = capture.read()
    frame = cv2.resize(frame, (960, 540), interpolation = cv2.INTER_AREA)

    yolo(frame)
        
    print('FPS {:.1f}'.format(1 / (time.time() - stime)))
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
