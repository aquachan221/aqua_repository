import winsound

i=600

def soundmake():
    global i
    while i:
        winsound.Beep(i, 200)
        i+= 50
        soundmake()

soundmake()