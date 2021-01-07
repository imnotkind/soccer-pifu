import cv2


for frame_no in range(1954, 2073):
    img_path = 'input/frame%d.jpg' % frame_no 
    label_path = 'detection/labels/frame%d.txt' % frame_no

    label_human = []

    with open(label_path, 'r') as f:
        for line in f.readlines():
            cls, x1, y1, x2, y2 = [int(x) for x in line.split()]
            if cls == 0:
                label_human.append((x1, y1, x2, y2))
    
    rect_path = 'input/frame%d_rect.txt' % frame_no
    with open(rect_path, 'w') as g:
        for (x1, y1, x2, y2) in label_human:
            w = x2 - x1
            h = y2 - y1
            cx = (x1+x2) // 2
            cy = (y1+y2) // 2

            r = max(w, h)
            g.write('%d %d %d %d\n' % (cx - r//2, cy - r//2, r, r))
            
    
    #img = cv2.imread(img_path)
    #for idx, (x1, y1, x2, y2) in enumerate(label_human):
        
        
        #crop_img = img[y1: y2, x1: x2]
        #cv2.imwrite('crop/frame%d-%d.jpg' % (frame_no, idx), crop_img)
