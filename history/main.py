# download all tiktok video from user
# edit video from entire directory using moviepy
# Created by HengSok

import time, os, inquirer
from pystyle import *
from moviepy.editor import * 
from colorama import *
from rich.traceback import install
from rich.console import Console

install()
console = Console()
init()

while True:
    try:
        
        #Edit Video Class
        class editVideo:

            #init Function
            def __init__(self):

                #Directory 
                
                clip_list = []
                #clip_list = os.listdir(file_list)
                def get_clip_list(file_list):
                    clip_list_input = []  
                    for file in file_list:
                        if file.endswith(".mp4") or file.endswith(".MP4") or file.endswith(".mkv"):
                            clip_list_input.append(file)
                    return clip_list_input

                #Edit Video Function
                def process(input, output):

                    #print(path_name_list)
                    clip = VideoFileClip(input)
                    #audio = AudioFileClip(input)
                    clip = clip.fx(vfx.mirror_x)
                    name = clip.filename
                    clip.write_videofile(output, verbose= False, logger= None, codec='libx264', audio_codec="aac")
                
                #Main 
                if __name__ == "__main__":
                    os.system('cls')
                    banner = f"""{Fore.MAGENTA}
        ███████╗██████╗░██╗████████╗  ██╗░░░██╗██╗██████╗░███████╗░█████╗░
        ██╔════╝██╔══██╗██║╚══██╔══╝  ██║░░░██║██║██╔══██╗██╔════╝██╔══██╗
        █████╗░░██║░░██║██║░░░██║░░░  ╚██╗░██╔╝██║██║░░██║█████╗░░██║░░██║
        ██╔══╝░░██║░░██║██║░░░██║░░░  ░╚████╔╝░██║██║░░██║██╔══╝░░██║░░██║
        ███████╗██████╔╝██║░░░██║░░░  ░░╚██╔╝░░██║██████╔╝███████╗╚█████╔╝
        ╚══════╝╚═════╝░╚═╝░░░╚═╝░░░  ░░░╚═╝░░░╚═╝╚═════╝░╚══════╝░╚════╝░
                            Created by HengSok{Fore.YELLOW}
                    """
                    print(Center.XCenter(banner))

                    try:
                        # Get input directory
                        print(f'{Fore.GREEN}')
                        print(Box.DoubleCube(r"Example: C:\Users\Name\Desktop\Folder\Video"))
                        video_folder = input(f"{Fore.YELLOW}Enter folder:{Fore.WHITE} ")

                        # check if the folder exists or not
                        if os.path.exists(video_folder):

                            # Get input files
                            file_list = os.listdir(video_folder)
                            clip_list = get_clip_list(file_list)

                            # Number of files found
                            console.log(f"[cyan][File][/cyan] {Fore.WHITE}Found {Fore.GREEN}{len(clip_list)}{Fore.WHITE} videos")
                            # Process status
                            console.log(f'[cyan][File][/cyan] {Fore.LIGHTYELLOW_EX}Start processing the video...')
                            counter = 0

                            # status or waiting
                            with console.status('[cyan] Processing the video...', spinner='aesthetic') as status:
                                
                                if not clip_list:
                                    pass
                                else:
                                    # make a new folder with counter += 1 everytime it runs.
                                    while True:
                                        counter += 1
                                        dir = "Video{}".format(counter)
                                        if os.path.isdir(dir):
                                            pass
                                        else:
                                            os.makedirs(dir)
                                            break

                                # Process files
                                for file in clip_list:
                                    output = dir + "/" + file[:-4] + "_edited.mp4"

                                    # Check if output exists in folder. If exists then skip else process
                                    if os.path.exists(output) == True:
                                        console.log(f'[cyan][File][/cyan] {Fore.LIGHTGREEN_EX}{file}{Fore.WHITE} already exist, skip...')
                                        # function skip
                                        clip_list.remove(file)
                                    else:
                                        process(video_folder + "/" + file, output)
                                        console.log(f'[cyan][File][/cyan] {Fore.LIGHTGREEN_EX}{file}{Fore.WHITE} has been created.')
                            console.log(f'[cyan][File][/cyan] Processed {Fore.LIGHTGREEN_EX}{len(clip_list)}{Fore.WHITE} videos successfully.')
                            time.sleep(1)
                            print(input(f"{Fore.CYAN}[Programs] {Fore.YELLOW}[Status] {Fore.WHITE}Press enter to continue.."))
                        else:
                            console.log("[red][Folder][/red] No such directory")
                            time.sleep(3)
                    except FileNotFoundError:
                        console.log("[red][Error][/red] Please Choose the Folder")
                        time.sleep(3)

        
        # Download Video From Tiktok
        class downTik:
            print("test")


        if __name__ == "__main__":
            os.system("cls" if os.name == "nt" else "clear"); os.system("title MMO by @HengSok" if os.name == "nt" else "")
            txt = f"""{Fore.MAGENTA}
    ███╗░░░███╗███╗░░░███╗░█████╗░░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░
    ████╗░████║████╗░████║██╔══██╗░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
    ██╔████╔██║██╔████╔██║██║░░██║█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░
    ██║╚██╔╝██║██║╚██╔╝██║██║░░██║╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
    ██║░╚═╝░██║██║░╚═╝░██║╚█████╔╝░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
    ╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░╚════╝░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
                            Created by HengSok
                  """
            
            print(Center.XCenter(txt))
            print(f'{Fore.GREEN}')
            print(Box.DoubleCube("Use arrow key to select the options"))
            questions = [inquirer.List('list', message=f"{Fore.YELLOW}Select Tools{Fore.WHITE}", choices=[' Edit Video', ' Download Tiktok Video', ' Download Douyin Video'],),]   
            answers = inquirer.prompt(questions)

            if answers['list'] == ' Edit Video':
                editVideo()
            elif answers['list'] == ' Download Tiktok Video':
                dsf = input("Test: ")
                #downTik()
                
            elif answers['list'] =='Download IG Video':
                pass
    except:
        console.log("[red][Error][/red] Program Interupted!")
        time.sleep(2)
