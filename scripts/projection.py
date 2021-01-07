import cv2
import math
import numpy as np
import sys
import os


from pifuhd.lib.render.mesh import load_obj_mesh, compute_normal
from pifuhd.lib.render.camera import Camera
from pifuhd.lib.render.gl.geo_render import GeoRender
from pifuhd.lib.render.gl.color_render import ColorRender
import trimesh


for frame_no in range(1954, 2073):
    img_path = 'frame/frame%d.jpg' % frame_no 
    rect_path = 'input/frame%d_rect.txt' % frame_no

    label_human = []
    with open(rect_path, 'r') as f:
        for line in f.readlines():
            x1, y1, r1, r2 = [int(x) for x in line.split()]
            
            label_human.append((x1, y1, r1, r2))
    
    for idx, (x1, y1, r1, r2) in enumerate(label_human):
        obj_path = 'pifu_result/result_frame%d_%d.obj' % (frame_no, idx)
        
        height, width = 512, 512

        renderer = ColorRender(width=width, height=height)
        cam = Camera(width=1.0, height=height/width)
        cam.ortho_ratio = 1
        cam.near = -100
        cam.far = 10
        
        mesh = trimesh.load(obj_path)
        vertices = mesh.vertices
        faces = mesh.faces

        # vertices = np.matmul(vertices, R.T)
        bbox_max = vertices.max(0)
        bbox_min = vertices.min(0)

        # notice that original scale is discarded to render with the same size
        vertices -= 0.5 * (bbox_max + bbox_min)[None,:]
        vertices /= bbox_max[1] - bbox_min[1]

        normals = compute_normal(vertices, faces)
        
        geo = False
        if geo:
            renderer.set_mesh(vertices, faces, normals, faces)
        else:
            renderer.set_mesh(vertices, faces, 0.5*normals+0.5, faces) 
            
        cnt = 0
        j = 0
        cam.center = np.array([0, 0, 0])
        cam.eye = np.array([0, 0, 1])

        renderer.set_camera(cam)
        renderer.display()
        
        img = renderer.get_color(0)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGRA)

        projection_path = 'object_projections/frame%d_%d.jpg' % (frame_no, idx)

        resized_img = cv2.resize(255*img, (r1, r2))
        
        cv2.imwrite(projection_path, resized_img)

        print(projection_path)
