from __future__ import unicode_literals

import youtube_dl

from cfonts import render

import time

import sys
import os 

#banner artwork
banner = render("YT-MP3", colors=['green', 'yellow'], align='center')
print(banner)

print("################################################")
print("\n")

print("**************** Author = Sumit ****************")

print("\n")
print("################################################")

#main code
url=input("\nPaste YouTube video link here & press enter ==> ")


print("loading your content:")

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.3)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")


#https://youtu.be/DiYOFlkxat0
#apt-get install ffmpeg

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    
print("\n\nYour mp3 file downloaded successfully!! Thanks for using ...")
    
    
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    answer = input("\n [-] Do you want to start again ?(y/n) ")
    if answer.lower().strip() in "y".split():
        restart_program()    