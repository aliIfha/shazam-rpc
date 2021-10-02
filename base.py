# made by ali#1000
# https://github.com/aliisverymad/shazam-rpc

import asyncio
from tkinter import Tk
from shazamio import Shazam
from pydub import AudioSegment
from pypresence import Presence
import keyboard
from tkinter.filedialog import askopenfilename
import os
import time
import ctypes

AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\bin\\ffprobe.exe"

def cls():
    os.system('cls')

async def main():
    ctypes.windll.user32.MessageBoxW(0, "Please select a MP3 File to send to the Shazam API!", "Select a MP3 File")
    Tk().withdraw()
    mp3select = askopenfilename()
    shazam = Shazam()
    global out
    global trackname
    out = await shazam.recognize_song(mp3select)
    trackname = out['track']['title']
    print("""
    Made by ali#1000
    https://github.com/aliisverymad/shazam-rpc (proof of concept)
    Press Q to quit

    Detected:
    """)
    print(trackname)
    print("Displayed on your Discord Profile")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

start_time=time.time()
client_id = '893869794154131506'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop
RPC.update(buttons=[{"label": "View the Source Code!", "url": "https://github.com/aliisverymad/shazam-rpc"}], details="Now playing", state=trackname, large_text="Made by ali#1000 :)", large_image="shazamlogo", start=start_time) # Set the presence
while True:
    keyboard.wait('q')
    keyboard.send('ctrl+c')