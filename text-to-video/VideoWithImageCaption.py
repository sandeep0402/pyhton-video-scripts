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
			if !entry.startswith'.':
				files.append(entry)
	return files

def divideAndJoinText(s, n):
    i = 0
    result = []
    s = s.strip()
    lenght = len(s)
    endReached = 0
    while i < lenght and endReached==0:
        start = i
        end = i+n
        if end > lenght:
            end = lenght
        str = s[start:end]
        
        #print('i: ',i, ' i+n:', i+n, ' lenght:',lenght, 'start: ',start,' end: ',end, ' str: ',str)
        if end != lenght: 
            lastIndex = i + str.rindex(' ')
            #print('lastIndex: ',lastIndex)
            if lastIndex < end :
                end = lastIndex
                str = s[start:end]
            

        #print('str : ',str)
        #print('end: ',end)
        result.append(str.strip())
        i = end
        if end >= lenght:
            endReached = 1
        #print(i)
        #if i>40:
            #break
    #print('\n'.join(result))
    return '\n'.join(result)

install()
console = Console()

clip_length = 10
dir= str(pathlib.Path().absolute())
output= dir +"/output"
isExist = os.path.exists(output)
# Read video files 
videos = getFileList(dir +"/videos" )
musics = getFileList(dir +"/music" )
musicFunny = getFileList(dir +"/musicFunny" )
tempImagePath = dir + "/temp-img.png"
color_clip_bg = [(0, 255, 255),(255, 0, 255),(255, 255, 0),(0, 0, 255),(255, 0, 0),(0, 255, 0),]
opacity = 40
color_img_clip_bg = [(0, 255, 255, opacity),(255, 0, 255, opacity),(255, 255, 0, opacity),(0, 0, 255, opacity),(255, 0, 0,opacity),(0, 255, 0,opacity),]

if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(output)
   print("The output directory is created!")

console.log("Processing...")
#print(TextClip.list('font'))
lines = pathlib.Path(dir+"/quotes.txt").read_text().splitlines()
for ind, line in enumerate(lines):
	musicMode = 1;
	if line.startswith('fun:'):
		line = line[4:]
		musicMode = 2

	index = str(ind+1)
	#line = line.upper()
	line = divideAndJoinText(line, 16)
	console.log(index , " Processing: " + line) 
	imgHeight = 120 * (line.count('\n')+1)

	#select random video
	videoSelected = str(videos[random.randrange(len(videos))].absolute())
	console.log("videoSelected=" +videoSelected)
	#select random color bg
	color_clip_selected = color_img_clip_bg[random.randrange(len(color_img_clip_bg))]
	#select random music
	musicsSelected = str(musics[random.randrange(len(musics))].absolute())
	console.log("musicsSelected=" +musicsSelected)
	#select random funny music
	if musicMode==2:
		musicFunnySelected = str(musicFunny[random.randrange(len(musicFunny))].absolute())
		console.log("musicFunnySelected=" +musicFunnySelected)

	with Image.new('RGBA', (980, imgHeight), color_clip_selected) as image:
	    font = ImageFont.truetype('/Users/adda247/Downloads/comici.ttf', 100)

	    with Pilmoji(image) as pilmoji:
	        pilmoji.text((20, 50), line.strip(), 'white', font)

	    image.save(tempImagePath, 'PNG')
	    #image.show()

	# loading video dsa gfg intro video 
	clip = VideoFileClip(videoSelected) 
	# getting video for only starting 10 seconds 
	clip = vfx.loop(clip, duration=500)
	clip = clip.subclip(0, clip_length) 
	# Reduce the audio volume (volume x 0.8) 
	clip = clip.volumex(0.8) 

	# Generate a text clip 
	#txt_clip = TextClip(line, font="Arial-Bold",fontsize = 75, color = 'white', method='caption', size=clip.size) 
	txt_clip  = ImageClip(tempImagePath).set_start(0).set_duration(clip_length).set_pos(("center","center"))

	# Overlay the text clip on the first video clip 
	video = CompositeVideoClip([clip, txt_clip]) 
	    

	clip_duration = video.duration

	audioclip = AudioFileClip(musicsSelected)#.set_duration(clip_duration)
	new_audioclip = afx.audio_loop(audioclip, duration=clip_duration)
	videoclip = video.set_audio(new_audioclip.set_start(0))


	if musicMode==2:
		videoclip1= videoclip.fx( volumex, 0.2)
		audioclipFunny = AudioFileClip(musicFunnySelected).set_duration(clip_length)
		new_audioclip = CompositeAudioClip([videoclip1.audio, audioclipFunny])
		videoclip.audio = new_audioclip
		#audioclipFunny = AudioFileClip(musicFunnySelected).set_duration(clip_length)
		#new_audioclip = CompositeAudioClip([videoclip.audio, audioclipFunny])
		#videoclip.audio = new_audioclip
		
	videoclip.write_videofile(output+"/test"+index+".mp4", verbose= False, logger= None, codec='libx264', audio_codec="aac")
	clip.close()
console.log("Done processing")
