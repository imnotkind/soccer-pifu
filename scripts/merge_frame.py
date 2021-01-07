import os


cmd = 'ffmpeg -framerate 10 -start_number 1954 -i overlay/frame%d.jpg -vcodec libx264 -y -pix_fmt yuv420p -refs 16 overlay_slow.mp4'

cmd = 'ffmpeg -framerate 10 -start_number 1954 -i son/frame%d.jpg -vcodec libx264 -y -pix_fmt yuv420p -refs 16 son_slow.mp4'
os.system(cmd)