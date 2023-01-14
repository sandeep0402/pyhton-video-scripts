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

dir= str(pathlib.Path().absolute())
output= dir +"/output"
isExist = os.path.exists(output)
# Read video files 
videos = getFileList(dir +"/videos" )
musics = getFileList(dir +"/music" )
color_clip_bg = [(0, 255, 255),(255, 0, 255),(255, 255, 0),(0, 0, 255),(255, 0, 0),(0, 255, 0),]

if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(output)
   print("The output directory is created!")

console.log("Processing...")
#print(TextClip.list('font'))
lines = pathlib.Path(dir+"/quotes.txt").read_text().splitlines()
for ind, line in enumerate(lines):
	index = str(ind+1)
	line = line.upper()
	console.log(index , " Processing: " + line) 

	#select random video
	videoSelected = str(videos[random.randrange(len(videos))].absolute())
	console.log("videoSelected=" +videoSelected)
	#select random music
	musicsSelected = str(musics[random.randrange(len(musics))].absolute())
	console.log("musicsSelected=" +musicsSelected)
	#select random color bg
	color_clip_selected = color_clip_bg[random.randrange(len(color_clip_bg))]
	#console.log("color_clip_selected=" +color_clip_selected)

	# loading video dsa gfg intro video 
	clip = VideoFileClip(videoSelected) 
		# getting video for only starting 10 seconds 
	clip = clip.subclip(0, 10) 
	# Reduce the audio volume (volume x 0.8) 
	clip = clip.volumex(0.8) 

	# Generate a text clip 
	#txt_clip = TextClip(line, font="Arial-Bold",fontsize = 75, color = 'white', method='caption', size=clip.size) 
	txt_clip = TextClip(line.encode('utf-8'), font = 'FreeMono', fontsize = 75, color = 'white', method='caption',  size=(.8*clip.size[0], 0), interline=100) 
	#txt_clip = TextClip(line, font = 'Segoe-UI-Emoji', fontsize = 75, color = 'white', method='caption',  size=(.8*clip.size[0], 0), interline=100) 
	#txt_clip = TextClip(line.encode('utf-8'), font = 'FreeMono',  fontsize = 75)

	im_width, im_height = txt_clip.size
	color_clip = ColorClip(size=(int(im_width*1.1), int(im_height*1.4)),
                       color=color_clip_selected)
	color_clip = color_clip.set_opacity(.4)
	txt_clip1 = CompositeVideoClip([color_clip, txt_clip.set_pos('center')])

	    
	# setting position of text in the center and duration will be 10 seconds 
	txt_clip = txt_clip1.set_pos('center').set_duration(10) 
	    
	# Overlay the text clip on the first video clip 
	video = CompositeVideoClip([clip, txt_clip]) 
	    

	clip_duration = video.duration

	audioclip = AudioFileClip(musicsSelected)#.set_duration(clip_duration)
	new_audioclip = afx.audio_loop(audioclip, duration=clip_duration)

	clip1 = video.set_audio(new_audioclip.set_start(1))

	clip1.write_videofile(output+"/test"+index+".mp4", verbose= False, logger= None, codec='libx264', audio_codec="aac")
	clip.close()
console.log("Done processing")
