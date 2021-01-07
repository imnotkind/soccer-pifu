import cv2
import numpy as np
import os

for frame_no in range(1954, 2073):
    img_path = 'frame/frame%d.jpg' % frame_no 
    rect_path = 'input/frame%d_rect.txt' % frame_no

    label_human = []
    with open(rect_path, 'r') as f:
        for line in f.readlines():
            x1, y1, r1, r2 = [int(x) for x in line.split()]
            label_human.append((x1, y1, r1, r2))
    
    img = cv2.imread(img_path)
    for idx, (x1, y1, r1, r2) in enumerate(label_human):
        projection_path = 'object_projections/frame%d_%d.jpg' % (frame_no, idx)
        if not os.path.exists(projection_path):
            continue
        proj_img = cv2.imread(projection_path)

        x2 = x1 + r1
        y2 = y1 + r2

        overlay = img.copy()

        dx1 = 0
        dx2 = r1
        dy1 = 0
        dy2 = r1
        
        # let's just pass for boxes that go out of the screen
        if x1 < 0:
            continue
            dx1 = -x1
            x1 = 0
        if y1 < 0:
            continue
            dy1 = -y1
            y1 = 0
        if x2 >= 7680:
            continue
            x2 = 7669
        if y2 >= 4320:
            continue
            y2 = 4319
        #############
        

        print(x1, y1, x2, y2, overlay.shape)
        print(dx1, dy1, dx2, dy2)

        overlay[y1: y2, x1: x2] = proj_img[ dy1: dy2, dx1: dx2 ]



        img = cv2.addWeighted(img, 0.3, overlay, 0.7, 0)

    overlay_path = 'overlay/frame%d.jpg' % (frame_no)
    cv2.imwrite(overlay_path, img)
    print(overlay_path)

