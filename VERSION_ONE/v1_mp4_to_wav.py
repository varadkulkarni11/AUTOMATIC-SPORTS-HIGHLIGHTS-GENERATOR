import subprocess

command = "ffmpeg -i D:/BEPROJECT/match.mp4 -ab 160k -ac 2 -ar 44100 -vn main_audio.wav"

subprocess.call(command, shell=True)
