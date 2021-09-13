import glob
import sys
import os
import collections
import shutil

dir = sys.argv[1]
HDRdir = os.path.join(dir,"HDR")
os.makedirs(HDRdir, exist_ok=True)
JPGdir = os.path.join(dir,"JPG")
os.makedirs(JPGdir, exist_ok=True)


jpg_paths = glob.glob(dir+"/*.jpg")
cr3_paths = glob.glob(dir+"/*.cr3")

jpg_files = [os.path.splitext(os.path.basename(i))[0] for i in jpg_paths]
cr3_files = [os.path.splitext(os.path.basename(i))[0] for i in cr3_paths]

for file in jpg_files:
    if not file in cr3_files:
        new_path = shutil.move(os.path.join(dir,file+".JPG"), JPGdir)
        os.rename(new_path,os.path.join(JPGdir,file+"-HDR.JPG"))
        for i in range(1,4):
            shutil.move(os.path.join(dir,file[:4]+str(int(file[4:8])-i)+".JPG"), JPGdir)
            shutil.move(os.path.join(dir,file[:4]+str(int(file[4:8])-i)+".CR3"), HDRdir)