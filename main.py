#coding:utf-8
import pygame
from pygame.locals import *

tex,tey=500,800
pygame.init()
fenetre=pygame.display.set_mode([tex,tey])
pygame.display.set_caption("test joystick")
font=pygame.font.SysFont("Arial",20)

nb_joysticks = pygame.joystick.get_count()
if nb_joysticks > 0:
	mon_joystick = pygame.joystick.Joystick(0)
	mon_joystick.init()
else:
    print("Vous n'avez pas de manettes branchées")
    exit()

encour=True
while encour:
    for event in pygame.event.get():
        if event.type==QUIT: exit()
    
    #aff
    fenetre.fill((255,255,255))
    yy=60
    fenetre.blit( font.render("nom : "+mon_joystick.get_name(),20,(0,0,0)) , [50,20] )
    fenetre.blit( font.render("nombre axes : "+str(mon_joystick.get_numaxes()),20,(0,0,0)) , [50,40] )
    for x in range(mon_joystick.get_numaxes()):
        aa=float(mon_joystick.get_axis(x))
        if aa > 0: aa=1
        elif aa < -0.5 : aa=-1
        else: aa=0  
        fenetre.blit( font.render("etat axes "+str(x)+" : "+str(aa),20,(0,0,0)) , [60,yy] )
        yy+=20
    fenetre.blit( font.render("nombre boutons : "+str(mon_joystick.get_numbuttons()),20,(0,0,0)) , [50,yy] )
    yy+=20
    for x in range(mon_joystick.get_numbuttons()):
        fenetre.blit( font.render("etat bouton "+str(x)+" : "+str(mon_joystick.get_button(x)),20,(0,0,0)) , [60,yy] )
        yy+=20
    fenetre.blit( font.render("nombre hats : "+str(mon_joystick.get_numhats()),20,(0,0,0)) , [50,yy] )
    yy+=20
    for x in range(mon_joystick.get_numhats()):
        fenetre.blit( font.render("etat hat "+str(x)+" : "+str(mon_joystick.get_hat(x)),20,(0,0,0)) , [60,yy] )
        yy+=20
    fenetre.blit( font.render("nombre balls : "+str(mon_joystick.get_numballs()),20,(0,0,0)) , [50,yy] )
    yy+=20
    for x in range(mon_joystick.get_numballs()):
        fenetre.blit( font.render("etat ball "+str(x)+" : "+str(mon_joystick.get_ball(x)),20,(0,0,0)) , [60,yy] )
        yy+=20
    pygame.display.flip()





