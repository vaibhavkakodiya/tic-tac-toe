from pygame import image, transform, font
import os 

ASSET_DIR = 'assets'

#background
bg_path = os.path.join(ASSET_DIR,"background.jpg")
background = image.load(bg_path)

font.init()

#X
x = font.SysFont("freesansbold.ttf",300)
x = x.render('X',True,(255,0,0))


#o
o = font.SysFont('freesansbold.ttf',300)
o = o.render('O',True,(0,0,255))

#win 'karumbi'
win = font.SysFont('Z003,Medium Italic',400)
win = win.render('Win',True,(225,0,255))

#lost
lost = font.SysFont('Z003,Medium Italic',400)
lost = lost.render('Lost',True,(225,0,255))

#draw 
draw = font.SysFont('Z003,Medium Italic',400)
draw = draw.render('Draw',True,(225,0,225))