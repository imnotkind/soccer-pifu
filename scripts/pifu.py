import os


#os.system("cd pifuhd/ && python apps/batch_openpose.py -d openpose/ -i C:/Users/haebin/Desktop/3d2d/crop -o C:/Users/haebin/Desktop/3d2d/crop")
os.system("cd pifuhd/ && python -m apps.simple_test --use_rect -i ../input -o ../pifu_result -r 512")
#os.system("cd pifuhd/ && python -m apps.render_turntable -f ../pifu_results/ -ww 512 -hh 512")