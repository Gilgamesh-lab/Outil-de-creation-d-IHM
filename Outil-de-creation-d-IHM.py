#!/usr/bin/env python
# coding: utf-8

# In[289]:


import win32clipboard

def copier(chaine):
    
    # set clipboard data
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()    
    win32clipboard.SetClipboardText(chaine)
    win32clipboard.CloseClipboard()

def coller():
   
    try:
        # get clipboard data
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data
    
    except TypeError:
        return ""


# In[290]:


def clavier(application,page,question,x,y,s = False):
    """
    fonction: input pour pygame --> affiche du texte et permet à l'utilisateur d'y répondre
    paramètre d'entrée : question : str , ecran : interface pygame , x,y : entier (coordonnée)
    effet de bord : affiche du texte et affiche la saisie de la réponse en cours
    paramètre de sortie : renvoie la réponse de l'utilisateur
    """

    ecran = application.ecran
    afficher(question,ecran,x,y, s = False)
    z = ""
    n = ""
    t = True
    while t:
        for evenement in pygame.event.get():
            keys = pygame.key.get_pressed()
            
            
            if keys[pygame.K_a]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT] and not keys[K_BACKQUOTE] and not keys[K_CARET]:
                    z += "a"
                    
                    
                if keys[K_CARET]:
                    z += "â"
                
                if   keys[K_RSHIFT] or keys[K_LSHIFT]:
                    z += "A"
                
                
            if keys[K_0] and not keys[K_RALT] and not keys[K_LALT] :
                z += "à"
                
                
            if keys[K_0] and  keys[K_RALT] or keys[K_LALT]:
                z += "@"
                
                    
            if keys[pygame.K_b]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "b"
                else:
                    z += "B"
                
                
            if keys[pygame.K_c] and not keys[K_RCTRL] and not keys[K_LCTRL]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "c"
                if   keys[K_RSHIFT] or keys[K_LSHIFT]:
                    z += "C"
                
                
            if keys[K_9]:
                z += "ç"
                
                
            if keys[K_8]:
                z += "_"
                
                    
            if keys[pygame.K_d]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "d"
                else:
                    z += "D"
                
                
            if keys[pygame.K_e]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT] and not keys[K_BACKQUOTE] and not keys[K_CARET] :
                    z += "e"
                    
                if keys[K_BACKQUOTE]:
                    z += "è"
                    
                if keys[K_CARET]:
                    z += "ê"
                    
                if   keys[K_RSHIFT] or keys[K_LSHIFT]:
                    z += "E"
                
                    
            if keys[K_2]:
                z +="é"
                
            if keys[K_7]:
                z +="è"
                
                    
                    
            if keys[pygame.K_f]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "f"
                else:
                    z += "F"
                
                    
            if keys[pygame.K_g]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "g"
                else:
                    z += "G"
                
                    
            if keys[pygame.K_h]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "h"
                else:
                    z += "H"
                
                
            if keys[pygame.K_i]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "i"
                else:
                    z += "I"
                
                
            if keys[pygame.K_j]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "j"
                else:
                    z += "J"
                
                
            if keys[pygame.K_k]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "k"
                else:
                    z += "K"
                
                
            if keys[pygame.K_l]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "l"
                else:
                    z += "L"
                
                
            if keys[pygame.K_m]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "m"
                else:
                    z += "M"
                
                
            if keys[pygame.K_n]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "n"
                else:
                    z += "N"
                
                
            if keys[pygame.K_o]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "o"
                else:
                    z += "O"
                
                
            if keys[pygame.K_p]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "p"
                else:
                    z += "P"
                
                
            if keys[pygame.K_q]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "q"
                else:
                    z += "Q"
                
                
            if keys[pygame.K_r]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "r"
                else:
                    z += "R"
                
                
            if keys[pygame.K_s]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "s"
                else:
                    z += "S"
                
                
            if keys[pygame.K_t]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "t"
                else:
                    z += "T"
                
                
            if keys[pygame.K_u]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "u"
                else:
                    z += "U"
                
            if keys[pygame.K_v] and not keys[K_RCTRL] and not keys[K_LCTRL]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "v"
                else:
                    z += "V"
                
                
            if keys[pygame.K_w]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "w"
                else:
                    z += "W"
                
                
            if keys[pygame.K_x]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "x"
                else:
                    z += "X"
                
                
            if keys[pygame.K_y]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "y"
                else:
                    z += "Y"
                
                
            if keys[pygame.K_z]:
                if  not keys[K_RSHIFT] and not keys[K_LSHIFT]:
                    z += "z"
                else:
                    z += "Z"
                
                
            if keys[K_5] and not keys[K_RALT] and not keys[K_LALT] :
                z += "("
                
            
            if keys[K_RIGHTPAREN] and not keys[K_RALT] and not keys[K_LALT] :
                z += ")"
                
            
                
            if keys[pygame.K_KP0]:
                z += "0"
                
                
            if keys[pygame.K_KP1]:
                z += "1"
                
                
            if keys[pygame.K_KP2]:
                z += "2"
                
                
            if keys[pygame.K_KP3]:
                z += "3"
                
                
            if keys[pygame.K_KP4]:
                z += "4"
                
                
            if keys[pygame.K_KP5]:
                z += "5"
                
                
            if keys[pygame.K_KP6]:
                z += "6"
                
                
            if keys[pygame.K_KP7]:
                z += "7"
                
                
            if keys[pygame.K_KP8]:
                z += "8"
                
                
            if keys[pygame.K_KP9]:
                z += "9"
                
                
            if keys[pygame.K_KP_PERIOD]:
                z += "."
                

            
                 
            if  keys[K_RCTRL] or keys[K_LCTRL] and  keys[pygame.K_c] and s == False :
                copier(z)
            
            #if  keys[K_RCTRL] or keys[K_LCTRL] and  keys[pygame.K_x] and s == False :
                #copier(z)
                #z = ''
                
            if  keys[K_RCTRL] or keys[K_LCTRL] and  keys[pygame.K_v]:
                z += coller()
                
            if keys[pygame.K_SPACE]: 
                z += ' '
                
            
                
            if keys[K_RETURN]:
                if len(z) > 0:
                    return z
                
            if keys[pygame.K_BACKSPACE]:
                b = ""
                for k in range(len(z)-1):
                    b = b + z[k]
                z = b
                    
            
            if n != z:#pygame.draw.rect(ecran,(43, 250, 250),(x,y,cadrage(z),10))
                ecran.fill(application.getRvb(page))
                afficher(question,ecran,x,y,s = False)
                afficher(z,ecran,x,y + 30, s = s)
                n = z[:]
                pygame.event.wait()
            
            if evenement.type == QUIT:    
                pygame.quit()
                sys.exit()
            #if event.type == pygame.VIDEORESIZE:
                #scrsize = event.size
                #width   = event.w
                #hight   = event.h
                #screen = pygame.display.set_mode(scrsize,RESIZABLE)
                #changed = True
        

            
            


# In[291]:


def afficher(z,ecran,x,y, taille = 12, rvb = (0, 0, 0), police = "broadway",s = False):
    """
    affiche un caractère passé en paramètre lettre par lettre
    z le caractère à afficher, x et y les cordonnées , s pour cacher le contenue, t = pour ne pas raffraichir l'écran et h
    pour afficher le bouton home
    """
            
    if s == True:
        for k in range(len(z)):
            i = '*'
            font=pygame.font.SysFont(police,taille,bold=False,italic=False)# réglage de la police,gras et italique
            text=font.render(i,1,rvb)# définition couleur
            ecran.blit(text,(x,y ))
            t = font.get_height()
            g = font.get_linesize()
            r = font.size(i)
            x += r[0]
            if x >= 690:
                x = 0
                y += 10
        pygame.display.flip()#mise à jou
    else:
        for k in range(len(z)):
            i = z[k]
            font=pygame.font.SysFont(police,taille,bold=False,italic=False)# réglage de la police,gras et italique
            text=font.render(i,1,rvb)# définition couleur
            ecran.blit(text,(x,y ))
            t = font.get_height()
            g = font.get_linesize()
            r = font.size(i)
            x += r[0]
            if x >= 690:
                x = 0
                y += 10
        pygame.display.flip()#mise à jour


# In[303]:


import pygame
from pygame.locals import*
import sys
from time import sleep

class Application:
    def __init__(self, taille: tuple = (700, 700), rvb: tuple = (43, 250, 250)):
        self.taille = taille
        pygame.init()
        self.ecran = pygame.display.set_mode((self.taille[0], self.taille[1]))
        self.rvb = rvb
        self.pageParDefaut = Page(rvb)
        self.listeTexte = []
        self.quitter = False

    def afficher(self, page = None, timeToSleep = None):
        if page == None:
            page = self.pageParDefaut
        self.ecran.fill(self.getRvb(page))
        pygame.display.flip()

        if page.listeTexte != []:
            for k in range(len(page.listeTexte)):
                texte = page.listeTexte[k]
                afficher(texte.contenue, self.ecran, texte.x, texte.y, texte.taille , texte.rvb, texte.police)
                
        if self.listeTexte != []:
            for k in range(len(self.listeTexte)):
                texte = self.listeTexte[k]
                afficher(self.contenue, self.ecran, self.x, self.y, self.taille , self.rvb, self.police)

        if timeToSleep == None :
            while self.quitter == False :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quitter = True
                        pygame.quit()
            
        else:
            sleep(timeToSleep)

    def close(self):
        self.quitter = True
        pygame.quit()
        

    def getRvb(self, page):
        if(page.rvb != None ) :
            return page.rvb
        else:
            return self.rvb

    def input(self, question, x, y, page = None,taille = 12, rvb = (0,0,0), police = "broadway", cacher = False):
        if page == None:
            page = self.pageParDefaut 
        self.ecran.fill(self.getRvb(page))
        return clavier(self, page, question, x, y, cacher)

    def ajouterTexte(self, texte):
        self.listeTexte.append(texte)


# In[304]:


class Page:
    def __init__(self, rvb: tuple = None):
        self.rvb = rvb
        self.listeTexte = []

    def ajouterTexte(self, texte, i = None):
        if i == None or len(self.listeTexte) <= i :
            self.listeTexte.append(texte)
        else:
            if len(self.listeTexte) > i :
                self.listeTexte[i] = texte
        
    


# In[305]:


class Texte:
    def __init__(self, contenue, x, y, taille = 12, rvb = (0,0,0), police = "broadway"):
        self.contenue = contenue
        self.x = x
        self.y = y
        self.taille = taille
        self.rvb = rvb
        self.police = police


# In[307]:


application = Application()
pageBienvenue = Page()
nom = application.input( "Bonjour, quel est votre prénom ?", 50, 100)
texteBienvenue = Texte(f"Bonjour {nom}, enchanté de te rencontrer !", 50, 100)
pageBienvenue.ajouterTexte(texteBienvenue, 0)
application.afficher(pageBienvenue, 5)
application.close()


# In[ ]:





# In[ ]:





# In[ ]:




