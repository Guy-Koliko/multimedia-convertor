#!/usr/bin/python

import os
import shutil
import time
import subprocess


#this are the variables to use
src_dir = './'
dst_dir = './test/'
#this is the main program

def main():
    ext_one = input("what is the extention of the file [mp3,mp4,avi...] ")
    ext_two = input("what file format do you want to convert file to [mpeg,mp4 ..]")

    ex_1 = '.'+ext_one
    ex_2 = '.'+ext_two


    watch_dog(ex_1,ex_2,src_dir)

#this is the part converter

def convert_tool(ex1,ex2):
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            prefix, suffix = os.path.splitext(f)
            if ex1 == suffix:
                abspath_in = root + '/' + f
                dir_out = root.replace(src_dir,dst_dir)
                if not os.path.exists(dir_out):
                    os.makedirs(dir_out)
                abspath_out = dir_out + '/' + prefix + ex2
                subprocess.call(['ffmpeg','-i',abspath_in,'-y',abspath_out])

#this is the watchdog
def watch_dog(ex1,ex2,dir_name='.'):
    old_files = set(os.listdir(dir_name))
    old_stat = os.stat(dir_name)
    
    while 1:
        time.sleep(1)
        new_stat = os.stat(dir_name)
        if new_stat == old_stat:
            continue
        new_files = set(os.listdir(dir_name))
        diff = new_files - old_files               
        if diff:
            print("New file or files found ", diff)
            convert_tool(ex1,ex2)
            break
       
        old_stat = new_stat
        old_files = new_files

main()