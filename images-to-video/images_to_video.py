# Import everything needed to edit video clips 
import requests,json,os,time,re
import random 
from random import choice
import inquirer
from pystyle import *
import os
from moviepy.editor import * 
import colorama
from colorama import *
from rich.traceback import install
from rich.console import Console
from requests_html import HTMLSession
import requests_random_user_agent
import pathlib 
import random
from PIL import Image, ImageDraw, ImageFont
from pilmoji import Pilmoji

def getFileList(path):
    files = []
    d = pathlib.Path(path)
    # iterate directory
    for entry in d.iterdir():
        # check if it a file
        if entry.is_file():
            files.append(entry)
    return files

install()
console = Console()

clip_length = 15
dir= str(pathlib.Path().absolute())
output= dir +"/output"
isExist = os.path.exists(output)
# Read video files 
images = getFileList(dir +"/images" )
musics = getFileList(dir +"/bg_music" )
musicFunny = getFileList(dir +"/funny_sound" )
tempImagePath = dir + "/temp-img.png"
videoSelected = dir+"/sea1.mp4"
musicsSelectedPath = dir+"/funny_sound/laugh.mp3"
musicsSelectedMode = 1 #1. fix path,  2. Random path

if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(output)
   print("The output directory is created!")

console.log("Processing...")
#print(TextClip.list('font'))
for ind, img in enumerate(images):
    image = str(images[ind].absolute())
    index = str(ind+1)
    console.log(index , " Processing: " , image) 

    #select random video
    console.log("videoSelected=" +videoSelected)
    #select random music
    if mode==1:
        musicsSelected = str(musics[random.randrange(len(musics))].absolute())
    else:
        musicsSelected = musicsSelectedPath
    console.log("musicsSelected=" +musicsSelected)
    #select random funny music
    musicFunnySelected = str(musicFunny[random.randrange(len(musicFunny))].absolute())
    console.log("musicFunnySelected=" +musicFunnySelected)

    # loading video dsa gfg intro video 
    clip = VideoFileClip(videoSelected) 
    # getting video for only starting 10 seconds 
    clip = vfx.loop(clip, duration=500)
    clip = clip.subclip(0, clip_length) 
    # Reduce the audio volume (volume x 0.8) 
    clip = clip.volumex(0.8) 

    # Generate a text clip 
    image_clip  = ImageClip(image).set_start(0).set_duration(clip_length).set_pos(("center","center"))

    # Overlay the text clip on the first video clip 
    videoclip = CompositeVideoClip([clip, image_clip]) 
        
    clip_duration = videoclip.duration

    musicsSelectedClip = AudioFileClip(musicsSelected)#.set_duration(clip_duration)
    musicsSelectedClip = afx.audio_loop(musicsSelectedClip, duration=clip_duration)

    musicFunnySelectedClip = AudioFileClip(musicFunnySelected).set_duration(clip_length)
    new_audioclip = CompositeAudioClip([musicsSelectedClip.volumex(0.2), musicFunnySelectedClip])
    videoclip.audio = new_audioclip
        
    videoclip.write_videofile(output+"/test"+index+".mp4", verbose= False, logger= None, codec='libx264', audio_codec="aac")
    clip.close()
    image_clip.close()
    musicsSelectedClip.close()
    musicFunnySelectedClip.close()
console.log("Done processing")


