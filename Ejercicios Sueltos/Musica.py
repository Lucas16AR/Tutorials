from pygame import mixer
file = '.mp3'
mixer.init()
mixer.music.load(file)
mixer.music.play()